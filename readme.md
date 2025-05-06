# Carteirinha Furiosa

Sistema de cadastro, personalização e validação de fãs, com integração a redes sociais e validação automática de documentos via OpenAI.

---

## **Sumário**

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Integrações](#integrações)
- [Validação de Perfil com OpenAI](#validação-de-perfil-com-openai)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Visão Geral

O **Carteirinha Furiosa** é uma plataforma Django para cadastro de fãs, escolha de preferências (jogos, pro players, streamers), vinculação de redes sociais (Instagram, Twitter) e validação automática de identidade por upload de documento, usando IA da OpenAI.

---

## Funcionalidades

- Cadastro de fãs com foto de perfil
- Escolha de preferências personalizadas
- Vinculação de Instagram e Twitter
- Upload e armazenamento de documento para validação
- Validação automática de nome e CPF via OpenAI (GPT-4o)
- Interface de perfil com status de validação
- Painel administrativo Django

---

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/rflMandell/Carteirinha-Furiosa
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv/Scripts/activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o arquivo `.env`:**
   Crie um arquivo `.env` na raiz do projeto com:
   ```
   OPENAI_API_KEY=sua_chave_openai_aqui
   ```

5. **Aplique as migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crie um superusuário (opcional para acessar os dados dos usuarios):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Rode o servidor:**
   ```bash
   python manage.py runserver
   ```

---

## Configuração

- **Variáveis de ambiente:**  
  O projeto usa o pacote `python-dotenv` para carregar variáveis do arquivo `.env`.
- **Arquivos de mídia:**  
  Certifique-se de que as configurações de `MEDIA_URL` e `MEDIA_ROOT` estão corretas no `settings.py`.

---

## Uso

- Acesse `http://localhost:8000/` para usar o sistema.
- Cadastre-se como fã, escolha preferências, vincule redes sociais e envie documento para validação.
- O status de validação aparece no perfil.
- O admin está disponível em `/admin/`.

---

## Estrutura do Projeto

```
know-your-fan/
├── fans/                # App principal
│   ├── models.py        # Modelos: Fan, Preferências, etc.
│   ├── views.py         # Lógicas de cadastro, perfil, validação, etc.
│   ├── forms.py         # Formulários
│   ├── templates/fans/  # Templates HTML
│   └── ...
├── core/                # Configuração do projeto Django
├── media/               # Arquivos enviados (fotos, documentos)
├── static/              # Arquivos estáticos (CSS, ícones)
├── requirements.txt
├── .env
└── manage.py
```

---

## Integrações

- **OpenAI:**  
  Utilizado para validação automática de documentos (nome e CPF).
- **Redes Sociais:**  
  Vinculação de Instagram e Twitter no perfil do fã.

---

## Validação de Perfil com OpenAI

- O usuário faz upload de um documento (PDF ou TXT).
- O sistema extrai apenas as linhas relevantes (nome e CPF).
- O texto é enviado para o modelo GPT-4o da OpenAI.
- O resultado da validação é salvo e exibido no perfil.

---

## Contribuição

1. Fork este repositório
2. Crie uma branch: `git checkout -b minha-feature`
3. Faça suas alterações e commit: `git commit -m 'Minha feature'`
4. Push para sua branch: `git push origin minha-feature`
5. Abra um Pull Request

---

## Licença

Este projeto está sob a licença MIT.
