import schedule
import time
import requests
from datetime import datetime
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

def enviar_notificacao(whatsapp_number, message):
    """Envio de notificação real via Twilio WhatsApp API."""
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_PHONE_NUMBER')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=twilio_number,
        to=f'whatsapp:{whatsapp_number}'
    )

    print(f"Mensagem enviada para {whatsapp_number}: {message.body}")

# Função que consulta dados atualizados sobre jogos e envia notificações
def agendar_notificacao():
    """Agendar notificações personalizadas para os usuários com base em suas preferências."""
    # Aqui estamos apenas simulando um cenário de notificação.
    usuarios = [
        {"whatsapp_number": "71996233756", "preferencia": "FURIA vs Team1", "hora": "15:00"},
    ]
    
    for usuario in usuarios:
        message = f"Olá! Não perca o jogo {usuario['preferencia']} às {usuario['hora']}!"
        enviar_notificacao(usuario['whatsapp_number'], message)

# Agendando a execução da notificação diariamente às 10:00 (exemplo)
schedule.every().day.at("10:00").do(agendar_notificacao)

def rodar_agendamentos():
    """Fica rodando os agendamentos em loop."""
    while True:
        schedule.run_pending()
        time.sleep(60)
