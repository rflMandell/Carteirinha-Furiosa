# Know Your Fan

Projeto desenvolvido para o teste técnico da FURIA.

## Descrição

O "Know Your Fan" é uma solução web para coleta, validação e análise de dados de fãs de esports.  
O sistema permite:
- Cadastro de informações pessoais e preferências.
- Upload de documentos e validação via OCR e OpenCV.
- Vinculação de redes sociais e plataformas de esports.
- Envio de conteúdo personalizado via WhatsApp.

## Tecnologias Utilizadas

- **Backend:** Django
- **Frontend:** HTML5, CSS3 (Bootstrap 5), JavaScript (ES6+)
- **Banco de Dados:** SQLite3
- **OCR e Análise de Imagens:** Pytesseract, OpenCV
- **Integrações de APIs:** Twitter, Instagram, Twitch, YouTube
- **Agendamento de Tarefas:** Schedule
- **Envio de Mensagens:** Integração com API do WhatsApp Business (simulada ou real)

## Instalação e Execução

1. Clone o repositório:
    ```bash
    git clone https://github.com/SEU_USUARIO/Know-Your-Fan.git
    cd Know-Your-Fan
    ```

2. Crie e ative o ambiente virtual:
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute as migrações do Django (após a criação do projeto Django):
    ```bash
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Autor

Desenvolvido por Rafael Mandel.
