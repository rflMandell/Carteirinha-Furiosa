import os
import django
import time
import schedule
from dotenv import load_dotenv

# Setup do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'know_your_fan.settings')
django.setup()

from .models import Usuario
from .services.notificacao_service import enviar_notificacao

load_dotenv()

def buscar_informacoes_esports(usuario):
    """Simulação de busca de informações de esports para o usuário."""
    # mensagem de exemplo
    return f"Olá {usuario.nome}, hoje seu time favorito tem jogo! Não perca! 🏆"

def enviar_notificacoes():
    """Busca usuários e envia notificações personalizadas."""
    usuarios = Usuario.objects.all()

    for usuario in usuarios:
        if usuario.numero_whatsapp:
            mensagem = buscar_informacoes_esports(usuario)
            enviar_notificacao(usuario.numero_whatsapp, mensagem)

def iniciar_agendamento():
    """Agendamento periódico para envio de notificações."""
    # Agenda o envio a cada 1 hora
    schedule.every(1).hours.do(enviar_notificacoes)

    print("Agendamento iniciado. Aguardando execução das tarefas...")
    while True:
        schedule.run_pending()
        time.sleep(1)
