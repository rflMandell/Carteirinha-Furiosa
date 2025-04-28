import time
from fans.services.notificacao_service import rodar_agendamentos

if __name__ == "__main__":
    # Inicia o agendamento em background
    rodar_agendamentos()
