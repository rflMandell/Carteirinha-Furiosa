├── .gitignore
├── core
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-311.pyc
    │   ├── settings.cpython-311.pyc
    │   ├── urls.cpython-311.pyc
    │   └── wsgi.cpython-311.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
├── db.sqlite3
├── fans
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-311.pyc
    │   ├── admin.cpython-311.pyc
    │   ├── apps.cpython-311.pyc
    │   └── models.cpython-311.pyc
    ├── admin.py
    ├── agendador.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_rename_telefone_fan_numero_whatsapp_remove_fan_cpf_and_more.py
    │   ├── 0003_fan_cpf_fan_endereco.py
    │   ├── __init__.py
    │   └── __pycache__
    │   │   ├── 0001_initial.cpython-311.pyc
    │   │   └── __init__.cpython-311.pyc
    ├── models.py
    ├── services
    │   ├── esports_service.py
    │   ├── notificacao_service.py
    │   └── rede_sociais
    │   │   ├── instagram_service.py
    │   │   └── twitter_service.py
    ├── templates
    │   ├── fans
    │   │   ├── base.html
    │   │   ├── cadastro_fan.html
    │   │   ├── cadastro_finalizado.html
    │   │   ├── cadastro_redes_sociais.html
    │   │   ├── home.html
    │   │   ├── instagram_info.html
    │   │   ├── perfil_esports_valido.html
    │   │   ├── twitter_info.html
    │   │   ├── vincular_perfil_esports.html
    │   │   └── vincular_twitter.html
    │   └── partials
    │   │   ├── footer.html
    │   │   └── navbar.html
    ├── tests.py
    ├── urls.py
    └── views.py
├── manage.py
├── readme.md
├── requirements.txt
├── scheduler.py
└── static
    └── images
        ├── banner-furia.jpg
        ├── furia-logo.png
        ├── furia-torcida.jpg
        ├── furia-torcida2.jpg
        ├── insta-logo.avif
        └── logo-furia.svg


/.gitignore:
--------------------------------------------------------------------------------
 1 | # Ignorar o arquivo .env (credenciais e tokens)
 2 | .env
 3 | 
 4 | # Ignorar arquivos de banco de dados SQLite
 5 | .sqlite3
 6 | 
 7 | # Ignorar diretórios de cache
 8 | __pycache__/
 9 | .pyc
10 | 
11 | # Ignorar ambientes virtuais
12 | venv/


--------------------------------------------------------------------------------
/core/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/core/__init__.py


--------------------------------------------------------------------------------
/core/__pycache__/__init__.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/core/__pycache__/__init__.cpython-311.pyc


--------------------------------------------------------------------------------
/core/__pycache__/settings.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/core/__pycache__/settings.cpython-311.pyc


--------------------------------------------------------------------------------
/core/__pycache__/urls.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/core/__pycache__/urls.cpython-311.pyc


--------------------------------------------------------------------------------
/core/__pycache__/wsgi.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/core/__pycache__/wsgi.cpython-311.pyc


--------------------------------------------------------------------------------
/core/asgi.py:
--------------------------------------------------------------------------------
 1 | """
 2 | ASGI config for core project.
 3 | 
 4 | It exposes the ASGI callable as a module-level variable named ``application``.
 5 | 
 6 | For more information on this file, see
 7 | https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
 8 | """
 9 | 
10 | import os
11 | 
12 | from django.core.asgi import get_asgi_application
13 | 
14 | os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
15 | 
16 | application = get_asgi_application()
17 | 


--------------------------------------------------------------------------------
/core/settings.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Django settings for core project.
  3 | 
  4 | Generated by 'django-admin startproject' using Django 5.2.
  5 | 
  6 | For more information on this file, see
  7 | https://docs.djangoproject.com/en/5.2/topics/settings/
  8 | 
  9 | For the full list of settings and their values, see
 10 | https://docs.djangoproject.com/en/5.2/ref/settings/
 11 | """
 12 | 
 13 | from pathlib import Path
 14 | import os
 15 | from dotenv import load_dotenv
 16 | 
 17 | # Build paths inside the project like this: BASE_DIR / 'subdir'.
 18 | BASE_DIR = Path(__file__).resolve().parent.parent
 19 | 
 20 | 
 21 | # Quick-start development settings - unsuitable for production
 22 | # See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
 23 | 
 24 | # SECURITY WARNING: keep the secret key used in production secret!
 25 | SECRET_KEY = 'django-insecure-bn6u0=2@8k_*qyq_(64j^pld*qkd37^ic+v_@%_n5f2*8e!7t_'
 26 | 
 27 | # SECURITY WARNING: don't run with debug turned on in production!
 28 | DEBUG = True
 29 | 
 30 | ALLOWED_HOSTS = []
 31 | 
 32 | 
 33 | # Application definition
 34 | 
 35 | INSTALLED_APPS = [
 36 |     'django.contrib.admin',
 37 |     'django.contrib.auth',
 38 |     'django.contrib.contenttypes',
 39 |     'django.contrib.sessions',
 40 |     'django.contrib.messages',
 41 |     'django.contrib.staticfiles',
 42 |     
 43 |     'fans',
 44 | ]
 45 | 
 46 | MIDDLEWARE = [
 47 |     'django.middleware.security.SecurityMiddleware',
 48 |     'django.contrib.sessions.middleware.SessionMiddleware',
 49 |     'django.middleware.common.CommonMiddleware',
 50 |     'django.middleware.csrf.CsrfViewMiddleware',
 51 |     'django.contrib.auth.middleware.AuthenticationMiddleware',
 52 |     'django.contrib.messages.middleware.MessageMiddleware',
 53 |     'django.middleware.clickjacking.XFrameOptionsMiddleware',
 54 | ]
 55 | 
 56 | ROOT_URLCONF = 'core.urls'
 57 | 
 58 | TEMPLATES = [
 59 |     {
 60 |         'BACKEND': 'django.template.backends.django.DjangoTemplates',
 61 |         'DIRS': [],
 62 |         'APP_DIRS': True,
 63 |         'OPTIONS': {
 64 |             'context_processors': [
 65 |                 'django.template.context_processors.debug',
 66 |                 'django.template.context_processors.request',
 67 |                 'django.contrib.auth.context_processors.auth',
 68 |                 'django.contrib.messages.context_processors.messages',
 69 |             ],
 70 |         },
 71 |     },
 72 | ]
 73 | 
 74 | WSGI_APPLICATION = 'core.wsgi.application'
 75 | 
 76 | 
 77 | # Database
 78 | # https://docs.djangoproject.com/en/5.2/ref/settings/#databases
 79 | 
 80 | DATABASES = {
 81 |     'default': {
 82 |         'ENGINE': 'django.db.backends.sqlite3',
 83 |         'NAME': BASE_DIR / 'db.sqlite3',
 84 |     }
 85 | }
 86 | 
 87 | 
 88 | # Password validation
 89 | # https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
 90 | 
 91 | AUTH_PASSWORD_VALIDATORS = [
 92 |     {
 93 |         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
 94 |     },
 95 |     {
 96 |         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
 97 |     },
 98 |     {
 99 |         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
100 |     },
101 |     {
102 |         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
103 |     },
104 | ]
105 | 
106 | 
107 | # Internationalization
108 | # https://docs.djangoproject.com/en/5.2/topics/i18n/
109 | 
110 | LANGUAGE_CODE = 'en-us'
111 | 
112 | TIME_ZONE = 'UTC'
113 | 
114 | USE_I18N = True
115 | 
116 | USE_TZ = True
117 | 
118 | 
119 | # Static files (CSS, JavaScript, Images)
120 | # https://docs.djangoproject.com/en/5.2/howto/static-files/
121 | 
122 | STATIC_URL = 'static/'
123 | 
124 | # Default primary key field type
125 | # https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
126 | 
127 | DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
128 | 
129 | #minhas cositas
130 | 
131 | # Carrega as variáveis de ambiente do arquivo .env
132 | load_dotenv()
133 | 
134 | TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
135 | TWITTER_API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
136 | TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
137 | TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
138 | 
139 | BASE_DIR = Path(__file__).resolve().parent.parent
140 | 
141 | STATIC_URL = '/static/'
142 | 
143 | STATICFILES_DIRS = [
144 |     os.path.join(BASE_DIR, "static"),
145 | ]


--------------------------------------------------------------------------------
/core/urls.py:
--------------------------------------------------------------------------------
 1 | """
 2 | URL configuration for core project.
 3 | 
 4 | The `urlpatterns` list routes URLs to views. For more information please see:
 5 |     https://docs.djangoproject.com/en/5.2/topics/http/urls/
 6 | Examples:
 7 | Function views
 8 |     1. Add an import:  from my_app import views
 9 |     2. Add a URL to urlpatterns:  path('', views.home, name='home')
10 | Class-based views
11 |     1. Add an import:  from other_app.views import Home
12 |     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
13 | Including another URLconf
14 |     1. Import the include() function: from django.urls import include, path
15 |     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
16 | """
17 | from django.contrib import admin
18 | from django.urls import path, include
19 | 
20 | urlpatterns = [
21 |     path('admin/', admin.site.urls),
22 |     path('', include('fans.urls')),
23 | ]
24 | 


--------------------------------------------------------------------------------
/core/wsgi.py:
--------------------------------------------------------------------------------
 1 | """
 2 | WSGI config for core project.
 3 | 
 4 | It exposes the WSGI callable as a module-level variable named ``application``.
 5 | 
 6 | For more information on this file, see
 7 | https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
 8 | """
 9 | 
10 | import os
11 | 
12 | from django.core.wsgi import get_wsgi_application
13 | 
14 | os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
15 | 
16 | application = get_wsgi_application()
17 | 


--------------------------------------------------------------------------------
/db.sqlite3:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/db.sqlite3


--------------------------------------------------------------------------------
/fans/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/__init__.py


--------------------------------------------------------------------------------
/fans/__pycache__/__init__.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/__pycache__/__init__.cpython-311.pyc


--------------------------------------------------------------------------------
/fans/__pycache__/admin.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/__pycache__/admin.cpython-311.pyc


--------------------------------------------------------------------------------
/fans/__pycache__/apps.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/__pycache__/apps.cpython-311.pyc


--------------------------------------------------------------------------------
/fans/__pycache__/models.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/__pycache__/models.cpython-311.pyc


--------------------------------------------------------------------------------
/fans/admin.py:
--------------------------------------------------------------------------------
1 | from django.contrib import admin
2 | 
3 | # Register your models here.
4 | 


--------------------------------------------------------------------------------
/fans/agendador.py:
--------------------------------------------------------------------------------
 1 | import os
 2 | import django
 3 | import time
 4 | import schedule
 5 | from dotenv import load_dotenv
 6 | 
 7 | # Setup do Django
 8 | os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'know_your_fan.settings')
 9 | django.setup()
10 | 
11 | from .models import Usuario
12 | from .services.notificacao_service import enviar_notificacao
13 | 
14 | load_dotenv()
15 | 
16 | def buscar_informacoes_esports(usuario):
17 |     """Simulação de busca de informações de esports para o usuário."""
18 |     # mensagem de exemplo
19 |     return f"Olá {usuario.nome}, hoje seu time favorito tem jogo! Não perca! 🏆"
20 | 
21 | def enviar_notificacoes():
22 |     """Busca usuários e envia notificações personalizadas."""
23 |     usuarios = Usuario.objects.all()
24 | 
25 |     for usuario in usuarios:
26 |         if usuario.numero_whatsapp:
27 |             mensagem = buscar_informacoes_esports(usuario)
28 |             enviar_notificacao(usuario.numero_whatsapp, mensagem)
29 | 
30 | def iniciar_agendamento():
31 |     """Agendamento periódico para envio de notificações."""
32 |     # Agenda o envio a cada 1 hora
33 |     schedule.every(1).hours.do(enviar_notificacoes)
34 | 
35 |     print("Agendamento iniciado. Aguardando execução das tarefas...")
36 |     while True:
37 |         schedule.run_pending()
38 |         time.sleep(1)
39 | 


--------------------------------------------------------------------------------
/fans/apps.py:
--------------------------------------------------------------------------------
1 | from django.apps import AppConfig
2 | 
3 | 
4 | class FansConfig(AppConfig):
5 |     default_auto_field = 'django.db.models.BigAutoField'
6 |     name = 'fans'
7 | 


--------------------------------------------------------------------------------
/fans/forms.py:
--------------------------------------------------------------------------------
 1 | from django import forms
 2 | from .models import Fan, RedeSocial, PerfilEsports
 3 | 
 4 | class FanForm(forms.ModelForm):
 5 |     class Meta:
 6 |         model = Fan
 7 |         fields = [
 8 |             'nome', 'cpf', 'endereco', 'email', 'numero_whatsapp',
 9 |             'twitter_username', 'twitch_username', 'instagram_username'
10 |         ]
11 | 
12 |     def __init__(self, *args, **kwargs):
13 |         super(FanForm, self).__init__(*args, **kwargs)
14 |         for field_name, field in self.fields.items():
15 |             field.widget.attrs.update({
16 |                 'class': 'w-full px-4 py-2 bg-gray-100 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500'
17 |             })
18 |             if isinstance(field.widget, forms.Textarea):
19 |                 field.widget.attrs.update({'rows': 3})
20 | 
21 | 
22 | class RedeSocialForm(forms.ModelForm):
23 |     class Meta:
24 |         model = RedeSocial
25 |         fields = ['plataforma', 'usuario', 'url']
26 | 
27 | 
28 | class PerfilEsportsForm(forms.ModelForm):
29 |     class Meta:
30 |         model = PerfilEsports
31 |         fields = ['site', 'url']
32 |     
33 | class EsportsProfileForm(forms.Form):
34 |     link_perfil_esports = forms.URLField(label="Link do Perfil de Esports", required=False, max_length=500)
35 |     
36 | class InstagramForm(forms.Form):
37 |     username = forms.CharField(label='Usuário do Instagram', max_length=150)
38 | 
39 | class TwitterForm(forms.Form):
40 |     username = forms.CharField(label='Usuário do Twitter (X)', max_length=150)


--------------------------------------------------------------------------------
/fans/migrations/0001_initial.py:
--------------------------------------------------------------------------------
 1 | # Generated by Django 5.2 on 2025-04-28 23:08
 2 | 
 3 | import django.db.models.deletion
 4 | from django.db import migrations, models
 5 | 
 6 | 
 7 | class Migration(migrations.Migration):
 8 | 
 9 |     initial = True
10 | 
11 |     dependencies = [
12 |     ]
13 | 
14 |     operations = [
15 |         migrations.CreateModel(
16 |             name='Fan',
17 |             fields=[
18 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
19 |                 ('nome', models.CharField(max_length=255)),
20 |                 ('endereco', models.TextField()),
21 |                 ('cpf', models.CharField(max_length=14, unique=True)),
22 |                 ('telefone', models.CharField(max_length=20)),
23 |                 ('jogos_favoritos', models.TextField()),
24 |                 ('streamers_favoritos', models.TextField()),
25 |                 ('criado_em', models.DateTimeField(auto_now_add=True)),
26 |             ],
27 |         ),
28 |         migrations.CreateModel(
29 |             name='DocumentoIdentidade',
30 |             fields=[
31 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
32 |                 ('documento', models.FileField(upload_to='documentos/')),
33 |                 ('dados_extraidos', models.JSONField(blank=True, null=True)),
34 |                 ('validado', models.BooleanField(default=False)),
35 |                 ('fan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fans.fan')),
36 |             ],
37 |         ),
38 |         migrations.CreateModel(
39 |             name='PerfilEsports',
40 |             fields=[
41 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
42 |                 ('site', models.CharField(max_length=100)),
43 |                 ('url', models.URLField()),
44 |                 ('verificado', models.BooleanField(default=False)),
45 |                 ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfis_esports', to='fans.fan')),
46 |             ],
47 |         ),
48 |         migrations.CreateModel(
49 |             name='RedeSocial',
50 |             fields=[
51 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
52 |                 ('plataforma', models.CharField(max_length=50)),
53 |                 ('usuario', models.CharField(max_length=255)),
54 |                 ('url', models.URLField()),
55 |                 ('dados_extraidos', models.JSONField(blank=True, null=True)),
56 |                 ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='redes_sociais', to='fans.fan')),
57 |             ],
58 |         ),
59 |     ]
60 | 


--------------------------------------------------------------------------------
/fans/migrations/0002_rename_telefone_fan_numero_whatsapp_remove_fan_cpf_and_more.py:
--------------------------------------------------------------------------------
 1 | # Generated by Django 5.2 on 2025-04-29 13:19
 2 | 
 3 | from django.db import migrations, models
 4 | 
 5 | 
 6 | class Migration(migrations.Migration):
 7 | 
 8 |     dependencies = [
 9 |         ('fans', '0001_initial'),
10 |     ]
11 | 
12 |     operations = [
13 |         migrations.RenameField(
14 |             model_name='fan',
15 |             old_name='telefone',
16 |             new_name='numero_whatsapp',
17 |         ),
18 |         migrations.RemoveField(
19 |             model_name='fan',
20 |             name='cpf',
21 |         ),
22 |         migrations.RemoveField(
23 |             model_name='fan',
24 |             name='criado_em',
25 |         ),
26 |         migrations.RemoveField(
27 |             model_name='fan',
28 |             name='endereco',
29 |         ),
30 |         migrations.RemoveField(
31 |             model_name='fan',
32 |             name='jogos_favoritos',
33 |         ),
34 |         migrations.RemoveField(
35 |             model_name='fan',
36 |             name='streamers_favoritos',
37 |         ),
38 |         migrations.AddField(
39 |             model_name='fan',
40 |             name='email',
41 |             field=models.EmailField(default=1, max_length=254),
42 |             preserve_default=False,
43 |         ),
44 |         migrations.AddField(
45 |             model_name='fan',
46 |             name='instagram_username',
47 |             field=models.CharField(blank=True, max_length=100, null=True),
48 |         ),
49 |         migrations.AddField(
50 |             model_name='fan',
51 |             name='twitch_username',
52 |             field=models.CharField(blank=True, max_length=100, null=True),
53 |         ),
54 |         migrations.AddField(
55 |             model_name='fan',
56 |             name='twitter_username',
57 |             field=models.CharField(blank=True, max_length=100, null=True),
58 |         ),
59 |         migrations.DeleteModel(
60 |             name='DocumentoIdentidade',
61 |         ),
62 |     ]
63 | 


--------------------------------------------------------------------------------
/fans/migrations/0003_fan_cpf_fan_endereco.py:
--------------------------------------------------------------------------------
 1 | # Generated by Django 5.2 on 2025-04-29 16:14
 2 | 
 3 | from django.db import migrations, models
 4 | 
 5 | 
 6 | class Migration(migrations.Migration):
 7 | 
 8 |     dependencies = [
 9 |         ('fans', '0002_rename_telefone_fan_numero_whatsapp_remove_fan_cpf_and_more'),
10 |     ]
11 | 
12 |     operations = [
13 |         migrations.AddField(
14 |             model_name='fan',
15 |             name='cpf',
16 |             field=models.CharField(default=1, max_length=14),
17 |             preserve_default=False,
18 |         ),
19 |         migrations.AddField(
20 |             model_name='fan',
21 |             name='endereco',
22 |             field=models.TextField(default=1),
23 |             preserve_default=False,
24 |         ),
25 |     ]
26 | 


--------------------------------------------------------------------------------
/fans/migrations/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/migrations/__init__.py


--------------------------------------------------------------------------------
/fans/migrations/__pycache__/0001_initial.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/migrations/__pycache__/0001_initial.cpython-311.pyc


--------------------------------------------------------------------------------
/fans/migrations/__pycache__/__init__.cpython-311.pyc:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/migrations/__pycache__/__init__.cpython-311.pyc


--------------------------------------------------------------------------------
/fans/models.py:
--------------------------------------------------------------------------------
 1 | from django.db import models
 2 | 
 3 | # Create your models here.
 4 | class Fan(models.Model):
 5 |     nome = models.CharField(max_length=255)
 6 |     cpf = models.CharField(max_length=14)
 7 |     endereco = models.TextField()
 8 |     email = models.EmailField()
 9 |     numero_whatsapp = models.CharField(max_length=20)
10 | 
11 |     # campos para redes sociais
12 |     twitter_username = models.CharField(max_length=100, blank=True, null=True)
13 |     twitch_username = models.CharField(max_length=100, blank=True, null=True)
14 |     instagram_username = models.CharField(max_length=100, blank=True, null=True)
15 | 
16 |     def __str__(self):
17 |         return self.nome
18 |     
19 | 
20 | class RedeSocial(models.Model):
21 |     fan = models.ForeignKey(Fan, on_delete=models.CASCADE, related_name='redes_sociais')
22 |     plataforma = models.CharField(max_length=50)  # Ex: Twitter, Instagram, Twitch  YouTube e por ai vai
23 |     usuario = models.CharField(max_length=255)
24 |     url = models.URLField()
25 |     dados_extraidos = models.JSONField(null=True, blank=True)  # Dados públicos coletados
26 | 
27 |     def __str__(self):
28 |         return f"{self.plataforma} - {self.usuario}"
29 | 
30 | 
31 | class PerfilEsports(models.Model):
32 |     fan = models.ForeignKey(Fan, on_delete=models.CASCADE, related_name='perfis_esports')
33 |     site = models.CharField(max_length=100)  # Ex: HLTV, Liquipedia, VLR?
34 |     url = models.URLField()
35 |     verificado = models.BooleanField(default=False)
36 | 
37 |     def __str__(self):
38 |         return f"{self.site} de {self.fan.nome}"
39 | 


--------------------------------------------------------------------------------
/fans/services/esports_service.py:
--------------------------------------------------------------------------------
 1 | import re
 2 | from urllib.parse import urlparse
 3 | 
 4 | def validar_link_esports(link):
 5 |     """Valida se o link pertence a plataformas de esports válidas (HLTV, Liquipedia)."""
 6 |     valid_domains = ['hltv.org', 'liquipedia.net']
 7 |     try:
 8 |         parsed_url = urlparse(link)
 9 |         domain = parsed_url.netloc.lower()
10 | 
11 |         if any(valid_domain in domain for valid_domain in valid_domains):
12 |             return True
13 |         return False
14 |     except Exception as e:
15 |         return False
16 | 


--------------------------------------------------------------------------------
/fans/services/notificacao_service.py:
--------------------------------------------------------------------------------
 1 | import schedule
 2 | import time
 3 | import requests
 4 | from datetime import datetime
 5 | from twilio.rest import Client
 6 | import os
 7 | from dotenv import load_dotenv
 8 | 
 9 | load_dotenv()  # Carrega as variáveis do .env
10 | 
11 | def enviar_notificacao(whatsapp_number, message):
12 |     """Envio de notificação real via Twilio WhatsApp API."""
13 |     account_sid = os.getenv('TWILIO_ACCOUNT_SID')
14 |     auth_token = os.getenv('TWILIO_AUTH_TOKEN')
15 |     twilio_number = os.getenv('TWILIO_PHONE_NUMBER')
16 | 
17 |     client = Client(account_sid, auth_token)
18 | 
19 |     message = client.messages.create(
20 |         body=message,
21 |         from_=twilio_number,
22 |         to=f'whatsapp:{whatsapp_number}'
23 |     )
24 | 
25 |     print(f"Mensagem enviada para {whatsapp_number}: {message.body}")
26 | 
27 | # Função que consulta dados atualizados sobre jogos e envia notificações
28 | def agendar_notificacao():
29 |     """Agendar notificações personalizadas para os usuários com base em suas preferências."""
30 |     # Aqui estamos apenas simulando um cenário de notificação.
31 |     usuarios = [
32 |         {"whatsapp_number": "71996233756", "preferencia": "FURIA vs Team1", "hora": "15:00"},
33 |     ]
34 |     
35 |     for usuario in usuarios:
36 |         message = f"Olá! Não perca o jogo {usuario['preferencia']} às {usuario['hora']}!"
37 |         enviar_notificacao(usuario['whatsapp_number'], message)
38 | 
39 | # Agendando a execução da notificação diariamente às 10:00 (exemplo)
40 | schedule.every().day.at("10:00").do(agendar_notificacao)
41 | 
42 | def rodar_agendamentos():
43 |     """Fica rodando os agendamentos em loop."""
44 |     while True:
45 |         schedule.run_pending()
46 |         time.sleep(60)
47 | 


--------------------------------------------------------------------------------
/fans/services/rede_sociais/instagram_service.py:
--------------------------------------------------------------------------------
 1 | import instaloader
 2 | 
 3 | def buscar_informacoes_instagram(username):
 4 |     loader = instaloader.Instaloader()
 5 | 
 6 |     try:
 7 |         profile = instaloader.Profile.from_username(loader.context, username)
 8 |         dados = {
 9 |             'username': profile.username,
10 |             'seguidores': profile.followers,
11 |             'seguindo': profile.followees,
12 |             'bio': profile.biography,
13 |             'url_perfil': f"https://instagram.com/{profile.username}"
14 |         }
15 |         return dados
16 |     except Exception as e:
17 |         print(f"Erro ao buscar informações do Instagram: {e}")
18 |         return None
19 | 


--------------------------------------------------------------------------------
/fans/services/rede_sociais/twitter_service.py:
--------------------------------------------------------------------------------
 1 | import tweepy
 2 | from django.conf import settings
 3 | 
 4 | # Configuração do Twitter
 5 | auth = tweepy.OAuth1UserHandler(
 6 |     settings.TWITTER_API_KEY,
 7 |     settings.TWITTER_API_SECRET_KEY,
 8 |     settings.TWITTER_ACCESS_TOKEN,
 9 |     settings.TWITTER_ACCESS_TOKEN_SECRET
10 | )
11 | 
12 | api = tweepy.API(auth)
13 | 
14 | def obter_dados_twitter(usuario_handle):
15 |     """Retorna dados básicos do perfil do Twitter."""
16 |     try:
17 |         usuario = api.get_user(screen_name=usuario_handle)
18 |         dados = {
19 |             'nome': usuario.name,
20 |             'descricao': usuario.description,
21 |             'seguindo': usuario.friends_count,
22 |             'seguidores': usuario.followers_count,
23 |             'tweets': usuario.statuses_count
24 |         }
25 |         return dados
26 |     except tweepy.TweepError as e:
27 |         print(f"Erro ao acessar o perfil do Twitter: {e}")
28 |         return None
29 | 


--------------------------------------------------------------------------------
/fans/templates/fans/base.html:
--------------------------------------------------------------------------------
 1 | {% load static %}
 2 | 
 3 | <!DOCTYPE html>
 4 | <html lang="pt-br">
 5 | <head>
 6 |   <meta charset="UTF-8">
 7 |   <meta name="viewport" content="width=device-width, initial-scale=1.0">
 8 |   <title>{% block title %}Know Your Fan{% endblock %}</title>
 9 |   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
10 |   <link rel="icon" href="{% static 'images/favicon.ico' %}" type="image/x-icon">
11 |   {% block head %}{% endblock %}
12 | </head>
13 | <body class="bg-white text-black font-sans">
14 | 
15 |   {% include 'partials/navbar.html' %}
16 | 
17 |   <main class="min-h-screen px-4 py-8">
18 |     {% block content %}{% endblock %}
19 |   </main>
20 | 
21 |   {% include 'partials/footer.html' %}
22 | 
23 |   {% block scripts %}{% endblock %}
24 | </body>
25 | </html>
26 | 


--------------------------------------------------------------------------------
/fans/templates/fans/cadastro_fan.html:
--------------------------------------------------------------------------------
 1 | {% extends 'fans/base.html' %}
 2 | {% load static %}
 3 | 
 4 | {% block title %}Cadastro | Carteirinha Furiosa{% endblock %}
 5 | 
 6 | {% block content %}
 7 | <section class="min-h-screen bg-cover bg-center relative" style="background-image: url('{% static 'images/furia-torcida2.jpg' %}');">
 8 |   <!-- Overlay escuro para contraste -->
 9 |   <div class="absolute inset-0 bg-black bg-opacity-60"></div>
10 | 
11 |   <!-- Conteúdo acima da imagem -->
12 |   <div class="relative z-10 flex flex-col justify-center items-center min-h-screen py-12 px-6">
13 |     <div class="w-full max-w-2xl rounded-xl shadow-lg p-8 bg-white bg-opacity-95 backdrop-blur-md">
14 |       <h2 class="text-3xl font-bold uppercase text-center text-black mb-8">Cadastro do Fã</h2>
15 | 
16 |       <form method="post" class="space-y-6">
17 |         {% csrf_token %}
18 |         {% for field in fan_form %}
19 |           <div>
20 |             <label class="block text-sm font-semibold text-gray-700 mb-1">{{ field.label_tag }}</label>
21 |             {{ field }}
22 |             {% if field.errors %}
23 |               <p class="text-sm text-red-600 mt-1">{{ field.errors }}</p>
24 |             {% endif %}
25 |           </div>
26 |         {% endfor %}
27 |         <div class="text-center">
28 |           <button type="submit" class="bg-yellow-500 hover:bg-yellow-600 text-black font-bold uppercase px-8 py-3 rounded-lg transition">
29 |             Próximo
30 |           </button>
31 |         </div>
32 |       </form>
33 |     </div>
34 |   </div>
35 | </section>
36 | {% endblock %}
37 | 


--------------------------------------------------------------------------------
/fans/templates/fans/cadastro_finalizado.html:
--------------------------------------------------------------------------------
 1 | {% load static %}
 2 | <!DOCTYPE html>
 3 | <html lang="pt-BR">
 4 | <head>
 5 |     <meta charset="UTF-8">
 6 |     <title>Cadastro Finalizado</title>
 7 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
 8 | </head>
 9 | <body class="bg-light">
10 |     <div class="container py-5 text-center">
11 |         <h2 class="mb-4">Cadastro concluído com sucesso!</h2>
12 |         <p class="lead">Obrigado por se cadastrar! Em breve você receberá atualizações personalizadas.</p>
13 |     </div>
14 | </body>
15 | </html>
16 | 


--------------------------------------------------------------------------------
/fans/templates/fans/cadastro_redes_sociais.html:
--------------------------------------------------------------------------------
 1 | {% load static %}
 2 | <!DOCTYPE html>
 3 | <html lang="pt-BR">
 4 | <head>
 5 |     <meta charset="UTF-8">
 6 |     <title>Redes Sociais e Perfis</title>
 7 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
 8 | </head>
 9 | <body class="bg-light">
10 |     <div class="container py-5">
11 |         <h2 class="mb-4">Redes Sociais e Perfis de Esports</h2>
12 |         <form method="post" class="card p-4 shadow-sm">
13 |             {% csrf_token %}
14 |             <h5>Rede Social</h5>
15 |             <div class="mb-3">
16 |                 {{ rede_form.as_p }}
17 |             </div>
18 |             <h5>Perfil de Esports</h5>
19 |             <div class="mb-3">
20 |                 {{ perfil_form.as_p }}
21 |             </div>
22 |             <button type="submit" class="btn btn-success">Finalizar Cadastro</button>
23 |         </form>
24 |     </div>
25 | </body>
26 | </html>
27 | 


--------------------------------------------------------------------------------
/fans/templates/fans/home.html:
--------------------------------------------------------------------------------
 1 | {% extends 'fans/base.html' %}
 2 | {% load static %}
 3 | 
 4 | {% block title %}Home | Carteirinha Furiosa{% endblock %}
 5 | 
 6 | {% block content %}
 7 | <section class="relative">
 8 |   <img src="{% static 'images/banner-furia.jpg' %}" alt="Banner FURIA" class="w-full h-full object-cover">
 9 |   <div class="absolute inset-0 bg-black bg-opacity-60 flex flex-col justify-center items-center text-center text-white px-4">
10 |     <h1 class="text-4xl md:text-5xl font-bold tracking-wide uppercase mb-4">Conheça a Carteirinha Furiosa</h1>
11 |     <p class="text-lg md:text-xl text-gray-300 max-w-2xl">A plataforma oficial da FURIA para entender e se conectar com você, fã de esports.</p>
12 |     <a href="{% url 'cadastro_fan' %}" class="mt-6 inline-block bg-yellow-500 hover:bg-yellow-600 text-black font-bold uppercase px-6 py-3 rounded-lg transition">Começar Agora</a>
13 |   </div>
14 | </section>
15 | 
16 | <section class="bg-white text-black py-16 px-6 md:px-16 text-center">
17 |   <h2 class="text-3xl md:text-4xl font-bold uppercase mb-8">O que é a Carteirinha Furiosa</h2>
18 |   <div class="w-full">
19 |     <div class="p-8 border border-gray-200 rounded-xl shadow hover:shadow-lg transition text-left w-full bg-gray-50 max-w-7xl mx-auto">
20 |       <h3 class="text-2xl font-semibold uppercase mb-4">Crie seu perfil</h3>
21 |       <p class="text-lg leading-relaxed">
22 |         Preencha dados básicos, seus interesses no universo FURIA, e nos diga quem são seus jogadores e streamers favoritos. Com base nos seus gostos, nosso sistema enviará pelo WhatsApp informações para que você viva o universo FURIA de onde estiver, a qualquer hora.
23 |       </p>
24 |     </div>
25 |   </div>
26 | </section>
27 | 
28 | <section class="bg-white text-black py-20 px-6 md:px-16">
29 |   <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center gap-12">
30 |     <!-- Imagem -->
31 |     <div class="w-full md:w-1/2">
32 |       <img src="{% static 'images/furia-torcida.jpg' %}" alt="Carteirinha Furiosa" class="w-full h-auto rounded-xl shadow-lg">
33 |     </div>
34 | 
35 |     <!-- Texto e botão -->
36 |     <div class="w-full md:w-1/2 text-center md:text-left">
37 |       <h2 class="text-3xl md:text-4xl font-bold uppercase mb-4">Faça parte da FURIA</h2>
38 |       <p class="text-lg text-gray-700 mb-6">
39 |         Cadastre-se agora e tenha acesso exclusivo a conteúdos personalizados, novidades do seu time favorito, e benefícios únicos como membro da Carteirinha Furiosa.
40 |       </p>
41 |       <a href="{% url 'cadastro_fan' %}" class="inline-block bg-yellow-500 hover:bg-yellow-600 text-black font-bold uppercase px-8 py-4 rounded-lg transition">
42 |         Inscreva-se Agora
43 |       </a>
44 |     </div>
45 |   </div>
46 | </section>
47 | 
48 | 
49 | 
50 | {% endblock %}
51 | 


--------------------------------------------------------------------------------
/fans/templates/fans/instagram_info.html:
--------------------------------------------------------------------------------
 1 | <!DOCTYPE html>
 2 | <html lang="pt-BR">
 3 | <head>
 4 |     <meta charset="UTF-8">
 5 |     <title>Buscar Instagram</title>
 6 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
 7 | </head>
 8 | <body class="container py-5">
 9 |     <h1 class="mb-4">Buscar Informações do Instagram</h1>
10 | 
11 |     <form method="post" class="mb-4">
12 |         {% csrf_token %}
13 |         {{ form.as_p }}
14 |         <button type="submit" class="btn btn-primary">Buscar</button>
15 |     </form>
16 | 
17 |     {% if dados_instagram %}
18 |         <div class="card">
19 |             <div class="card-body">
20 |                 <h5 class="card-title">@{{ dados_instagram.username }}</h5>
21 |                 <p><strong>Seguidores:</strong> {{ dados_instagram.seguidores }}</p>
22 |                 <p><strong>Seguindo:</strong> {{ dados_instagram.seguindo }}</p>
23 |                 <p><strong>Bio:</strong> {{ dados_instagram.bio }}</p>
24 |                 <a href="{{ dados_instagram.url_perfil }}" class="btn btn-success" target="_blank">Ver Perfil</a>
25 |             </div>
26 |         </div>
27 |     {% endif %}
28 | </body>
29 | </html>
30 | 


--------------------------------------------------------------------------------
/fans/templates/fans/perfil_esports_valido.html:
--------------------------------------------------------------------------------
 1 | {% load static %}
 2 | <!DOCTYPE html>
 3 | <html lang="pt-BR">
 4 | <head>
 5 |     <meta charset="UTF-8">
 6 |     <title>Perfil de Esports Vinculado</title>
 7 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
 8 | </head>
 9 | <body class="bg-light">
10 |     <div class="container py-5">
11 |         <h2 class="mb-4">Perfil de Esports Vinculado com Sucesso</h2>
12 |         <p>O link do seu perfil de esports foi validado e vinculado ao seu cadastro!</p>
13 |         <ul class="list-group">
14 |             <li class="list-group-item"><strong>Link do Perfil:</strong> {{ fan.perfil_esports_link }}</li>
15 |         </ul>
16 |         <a href="{% url 'perfil' fan.id %}" class="btn btn-primary mt-4">Voltar ao Perfil</a>
17 |     </div>
18 | </body>
19 | </html>
20 | 


--------------------------------------------------------------------------------
/fans/templates/fans/twitter_info.html:
--------------------------------------------------------------------------------
 1 | <!DOCTYPE html>
 2 | <html lang="pt-BR">
 3 | <head>
 4 |     <meta charset="UTF-8">
 5 |     <title>Buscar Twitter</title>
 6 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
 7 | </head>
 8 | <body class="container py-5">
 9 |     <h1 class="mb-4">Buscar Informações do Twitter</h1>
10 | 
11 |     <form method="post" class="mb-4">
12 |         {% csrf_token %}
13 |         {{ form.as_p }}
14 |         <button type="submit" class="btn btn-primary">Buscar</button>
15 |     </form>
16 | 
17 |     {% if dados_twitter %}
18 |         <div class="card">
19 |             <div class="card-body">
20 |                 <h5 class="card-title">@{{ dados_twitter.username }}</h5>
21 |                 <p><strong>Nome:</strong> {{ dados_twitter.nome }}</p>
22 |                 <p><strong>Bio:</strong> {{ dados_twitter.bio }}</p>
23 |                 <p><strong>Seguidores:</strong> {{ dados_twitter.seguidores }}</p>
24 |                 <p><strong>Seguindo:</strong> {{ dados_twitter.seguindo }}</p>
25 |                 <a href="{{ dados_twitter.url_perfil }}" class="btn btn-success" target="_blank">Ver Perfil</a>
26 |             </div>
27 |         </div>
28 |     {% endif %}
29 | </body>
30 | </html>
31 | 


--------------------------------------------------------------------------------
/fans/templates/fans/vincular_perfil_esports.html:
--------------------------------------------------------------------------------
 1 | {% load static %}
 2 | <!DOCTYPE html>
 3 | <html lang="pt-BR">
 4 | <head>
 5 |     <meta charset="UTF-8">
 6 |     <title>Vincular Perfil de Esports</title>
 7 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
 8 | </head>
 9 | <body class="bg-light">
10 |     <div class="container py-5">
11 |         <h2 class="mb-4">Vincular Perfil de Esports</h2>
12 |         <form method="post" class="card p-4 shadow-sm">
13 |             {% csrf_token %}
14 |             {{ form.as_p }}
15 |             <button type="submit" class="btn btn-primary">Vincular</button>
16 |         </form>
17 |     </div>
18 | </body>
19 | </html>
20 | 


--------------------------------------------------------------------------------
/fans/templates/fans/vincular_twitter.html:
--------------------------------------------------------------------------------
 1 | {% load static %}
 2 | <!DOCTYPE html>
 3 | <html lang="pt-BR">
 4 | <head>
 5 |     <meta charset="UTF-8">
 6 |     <title>Vincular Twitter</title>
 7 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
 8 | </head>
 9 | <body class="bg-light">
10 |     <div class="container py-5">
11 |         <h2 class="mb-4">Vincular Conta do Twitter</h2>
12 |         <form method="post" class="card p-4 shadow-sm">
13 |             {% csrf_token %}
14 |             {{ form.as_p }}
15 |             <button type="submit" class="btn btn-primary">Vincular</button>
16 |         </form>
17 |     </div>
18 | </body>
19 | </html>
20 | 


--------------------------------------------------------------------------------
/fans/templates/partials/footer.html:
--------------------------------------------------------------------------------
 1 | {% load static %}
 2 | 
 3 | <footer class="w-full bg-white text-dark border-t py-12 px-6 md:px-16">
 4 |   <div class="flex flex-col md:flex-row justify-between gap-12 flex-wrap">
 5 |     
 6 |     <!-- Newsletter -->
 7 |     <div class="md:w-1/4">
 8 |       <h6 class="text-uppercase font-bold mb-4">SEJA O PRIMEIRO A SABER DAS NOSSAS NOVIDADES:</h6>
 9 |       <div class="flex">
10 |         <input type="email" class="border border-dark px-3 py-2 w-full rounded-l" placeholder="Seu e-mail">
11 |         <button class="bg-black text-white px-4 py-2 rounded-r hover:bg-gray-800 transition">
12 |           <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
13 |             <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
14 |           </svg>
15 |         </button>
16 |       </div>
17 |     </div>
18 | 
19 |     <!-- Informações -->
20 |     <div class="md:w-1/4">
21 |       <h6 class="text-uppercase font-bold mb-4">INFORMAÇÕES</h6>
22 |       <ul class="space-y-2">
23 |         <li><a href="https://www.furia.gg/quem-somos" class="text-dark hover:underline">Quem somos</a></li>
24 |       </ul>
25 |     </div>
26 | 
27 |     <!-- Políticas -->
28 |     <div class="md:w-1/4">
29 |       <h6 class="text-uppercase font-bold mb-4">POLÍTICAS</h6>
30 |       <ul class="space-y-2">
31 |         <li><a href="https://www.furia.gg/politica-privacidade" class="text-dark hover:underline">Política de Privacidade</a></li>
32 |         <li><a href="https://www.furia.gg/politica-cookie" class="text-dark hover:underline">Política de Cookie</a></li>
33 |       </ul>
34 |     </div>
35 | 
36 |     <!-- Redes Sociais -->
37 |     <div class="md:w-1/4">
38 |       <h6 class="text-uppercase font-bold mb-4">SIGA FURIA</h6>
39 |       <div class="flex gap-4">
40 |         <a href="https://www.instagram.com/furiagg/" target="_blank">
41 |           <img src="{% static 'images/insta-logo.avif' %}" alt="Instagram" width="24" height="24">
42 |         </a>
43 |       </div>
44 |     </div>
45 |   </div>
46 | 
47 |   <div class="border-t border-gray-300 mt-8 pt-4 text-center text-sm text-gray-500">
48 |     © 2024 Furia. All Rights Reserved.
49 |   </div>
50 | </footer>
51 | 


--------------------------------------------------------------------------------
/fans/templates/partials/navbar.html:
--------------------------------------------------------------------------------
 1 | {% load static %}
 2 | 
 3 | <nav class="fixed top-0 w-full z-50 bg-white text-black px-8 py-4 flex items-center justify-between uppercase tracking-wide relative shadow-md">
 4 | 
 5 |   <ul class="flex gap-8 text-sm items-center absolute left-8">
 6 |     <li><a href="https://www.furia.gg/" class="hover:underline">Loja</a></li>
 7 |     <li><a href="https://www.youtube.com/@FURIAggCS" class="hover:underline">Conteúdo</a></li>
 8 |     <li><a href="https://www.furia.gg/quem-somos" class="hover:underline">Sobre</a></li>
 9 |   </ul>
10 | 
11 |   <a href="/" class="text-2xl font-black mx-auto">
12 |     <img src="{% static 'images/logo-furia.svg' %}" alt="FURIA Logo" class="h-10">
13 |   </a>
14 | 
15 |   <div class="flex gap-6 items-center text-xs absolute right-8">
16 |     <a href="/cadastro" class="bg-black text-white px-4 py-2 rounded hover:bg-gray-800 transition">Entrar</a>
17 |   </div>
18 | </nav>
19 | 


--------------------------------------------------------------------------------
/fans/tests.py:
--------------------------------------------------------------------------------
1 | from django.test import TestCase
2 | 
3 | # Create your tests here.
4 | 


--------------------------------------------------------------------------------
/fans/urls.py:
--------------------------------------------------------------------------------
 1 | from django.urls import path
 2 | from . import views
 3 | 
 4 | urlpatterns = [
 5 |     path('cadastro/', views.cadastro_fan, name='cadastro_fan'),
 6 |     path('cadastro/redes-sociais/<int:fan_id>/', views.cadastro_redes_sociais, name='cadastro_redes_sociais'),
 7 |     path('cadastro/finalizado/', views.cadastro_finalizado, name='cadastro_finalizado'),
 8 |     path('vincular_perfil_esports/<int:fan_id>/', views.vincular_perfil_esports, name='vincular_perfil_esports'),
 9 |     path('instagram/', views.instagram_info_view, name='instagram_info'),
10 |     path('twitter/', views.twitter_info_view, name='twitter_info'),
11 |     path('', views.home, name='home'),
12 | ]
13 | 


--------------------------------------------------------------------------------
/fans/views.py:
--------------------------------------------------------------------------------
 1 | from django.shortcuts import render, redirect
 2 | from django.http import HttpResponse
 3 | from .forms import FanForm, RedeSocialForm, PerfilEsportsForm, TwitterForm, EsportsProfileForm, InstagramForm
 4 | from fans.services.rede_sociais.twitter_service import obter_dados_twitter
 5 | from fans.services.rede_sociais.instagram_service import buscar_informacoes_instagram
 6 | from .models import Fan
 7 | from .services.esports_service import validar_link_esports
 8 | 
 9 | def cadastro_fan(request):
10 |     if request.method == 'POST':
11 |         fan_form = FanForm(request.POST)
12 |         
13 |         if fan_form.is_valid():
14 |             fan = fan_form.save()
15 |             return redirect('cadastro_redes_sociais', fan_id=fan.id)  # Passa o fan_id
16 |     else:
17 |         fan_form = FanForm()
18 | 
19 |     return render(request, 'fans/cadastro_fan.html', {
20 |         'fan_form': fan_form,
21 |     })
22 | 
23 | def cadastro_redes_sociais(request, fan_id):
24 |     if request.method == 'POST':
25 |         rede_form = RedeSocialForm(request.POST)
26 |         perfil_form = PerfilEsportsForm(request.POST)
27 | 
28 |         if rede_form.is_valid() and perfil_form.is_valid():
29 |             rede_social = rede_form.save(commit=False)
30 |             rede_social.fan_id = fan_id
31 |             rede_social.save()
32 | 
33 |             perfil = perfil_form.save(commit=False)
34 |             perfil.fan_id = fan_id
35 |             perfil.save()
36 | 
37 |             return redirect('cadastro_finalizado')
38 | 
39 |     else:
40 |         rede_form = RedeSocialForm()
41 |         perfil_form = PerfilEsportsForm()
42 | 
43 |     return render(request, 'fans/cadastro_redes_sociais.html', {
44 |         'rede_form': rede_form,
45 |         'perfil_form': perfil_form,
46 |     })
47 | 
48 | def cadastro_finalizado(request):
49 |     return render(request, 'fans/cadastro_finalizado.html')
50 | 
51 | def vincular_perfil_esports(request, fan_id):
52 |     fan = Fan.objects.get(id=fan_id)
53 | 
54 |     if request.method == 'POST':
55 |         form = EsportsProfileForm(request.POST)
56 |         if form.is_valid():
57 |             link_perfil = form.cleaned_data['link_perfil_esports']
58 | 
59 |             if link_perfil and validar_link_esports(link_perfil):
60 |                 # Armazenar o link do perfil de esports no banco de dados
61 |                 fan.perfil_esports_link = link_perfil
62 |                 fan.save()
63 | 
64 |                 return render(request, 'fans/perfil_esports_valido.html', {'fan': fan})
65 |             else:
66 |                 return HttpResponse("Link de perfil de esports inválido ou não pertence a plataformas válidas.", status=400)
67 |     else:
68 |         form = EsportsProfileForm()
69 | 
70 |     return render(request, 'fans/vincular_perfil_esports.html', {'form': form, 'fan': fan})
71 | 
72 | def instagram_info_view(request):
73 |     dados_instagram = None
74 | 
75 |     if request.method == 'POST':
76 |         form = InstagramForm(request.POST)
77 |         if form.is_valid():
78 |             username = form.cleaned_data['username']
79 |             dados_instagram = buscar_informacoes_instagram(username)
80 |     else:
81 |         form = InstagramForm()
82 | 
83 |     return render(request, 'fans/instagram_info.html', {'form': form, 'dados_instagram': dados_instagram})
84 | 
85 | def twitter_info_view(request):
86 |     dados_twitter = None
87 | 
88 |     if request.method == 'POST':
89 |         form = TwitterForm(request.POST)
90 |         if form.is_valid():
91 |             username = form.cleaned_data['username']
92 |             dados_twitter = obter_dados_twitter(username)
93 |     else:
94 |         form = TwitterForm()
95 | 
96 |     return render(request, 'fans/twitter_info.html', {'form': form, 'dados_twitter': dados_twitter})
97 | 
98 | def home(request):
99 |     return render(request, 'fans/home.html')


--------------------------------------------------------------------------------
/manage.py:
--------------------------------------------------------------------------------
 1 | #!/usr/bin/env python
 2 | """Django's command-line utility for administrative tasks."""
 3 | import os
 4 | import sys
 5 | 
 6 | 
 7 | def main():
 8 |     """Run administrative tasks."""
 9 |     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
10 |     try:
11 |         from django.core.management import execute_from_command_line
12 |     except ImportError as exc:
13 |         raise ImportError(
14 |             "Couldn't import Django. Are you sure it's installed and "
15 |             "available on your PYTHONPATH environment variable? Did you "
16 |             "forget to activate a virtual environment?"
17 |         ) from exc
18 |     execute_from_command_line(sys.argv)
19 | 
20 | 
21 | if __name__ == '__main__':
22 |     main()
23 | 


--------------------------------------------------------------------------------
/readme.md:
--------------------------------------------------------------------------------
 1 | # Know Your Fan
 2 | 
 3 | Projeto desenvolvido para o teste técnico da FURIA.
 4 | 
 5 | ## Descrição
 6 | 
 7 | O "Know Your Fan" é uma solução web para coleta, validação e análise de dados de fãs de esports.  
 8 | O sistema permite:
 9 | - Cadastro de informações pessoais e preferências.
10 | - Upload de documentos e validação via OCR e OpenCV.
11 | - Vinculação de redes sociais e plataformas de esports.
12 | - Envio de conteúdo personalizado via WhatsApp.
13 | 
14 | ## Tecnologias Utilizadas
15 | 
16 | - **Backend:** Django
17 | - **Frontend:** HTML5, CSS3 (Bootstrap 5), JavaScript (ES6+)
18 | - **Banco de Dados:** SQLite3
19 | - **OCR e Análise de Imagens:** Pytesseract, OpenCV
20 | - **Integrações de APIs:** Twitter, Instagram, Twitch, YouTube
21 | - **Agendamento de Tarefas:** Schedule
22 | - **Envio de Mensagens:** Integração com API do WhatsApp Business (simulada ou real)
23 | 
24 | ## Instalação e Execução
25 | 
26 | 1. Clone o repositório:
27 |     ```bash
28 |     git clone https://github.com/SEU_USUARIO/Know-Your-Fan.git
29 |     cd Know-Your-Fan
30 |     ```
31 | 
32 | 2. Crie e ative o ambiente virtual:
33 |     ```bash
34 |     # Windows
35 |     python -m venv venv
36 |     .\venv\Scripts\activate
37 | 
38 |     # Mac/Linux
39 |     python3 -m venv venv
40 |     source venv/bin/activate
41 |     ```
42 | 
43 | 3. Instale as dependências:
44 |     ```bash
45 |     pip install -r requirements.txt
46 |     ```
47 | 
48 | 4. Execute as migrações do Django (após a criação do projeto Django):
49 |     ```bash
50 |     python manage.py migrate
51 |     ```
52 | 
53 | 5. Inicie o servidor de desenvolvimento:
54 |     ```bash
55 |     python manage.py runserver
56 |     ```
57 | 
58 | ## Autor
59 | 
60 | Desenvolvido por Rafael Mandel.
61 | 


--------------------------------------------------------------------------------
/requirements.txt:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/requirements.txt


--------------------------------------------------------------------------------
/scheduler.py:
--------------------------------------------------------------------------------
1 | import time
2 | from fans.services.notificacao_service import rodar_agendamentos
3 | 
4 | if __name__ == "__main__":
5 |     # Inicia o agendamento em background
6 |     rodar_agendamentos()
7 | 


--------------------------------------------------------------------------------
/static/images/banner-furia.jpg:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/static/images/banner-furia.jpg


--------------------------------------------------------------------------------
/static/images/furia-logo.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/static/images/furia-logo.png


--------------------------------------------------------------------------------
/static/images/furia-torcida.jpg:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/static/images/furia-torcida.jpg


--------------------------------------------------------------------------------
/static/images/furia-torcida2.jpg:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/static/images/furia-torcida2.jpg


--------------------------------------------------------------------------------
/static/images/insta-logo.avif:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/static/images/insta-logo.avif


--------------------------------------------------------------------------------
/static/images/logo-furia.svg:
--------------------------------------------------------------------------------
1 | <svg width="90" height="32" viewBox="0 0 90 32" fill="none" xmlns="http://www.w3.org/2000/svg">
2 | <path fill-rule="evenodd" clip-rule="evenodd" d="M53.8249 6.78989C53.7668 7.50049 53.6459 8.20517 53.5465 8.91208C53.3582 10.2526 53.179 11.5946 52.9702 12.9322C52.8319 13.8189 52.5263 14.0802 51.6546 14.1054C51.0396 14.1224 50.4238 14.1091 49.8084 14.1047C49.7386 14.1039 49.669 14.0713 49.5054 14.0292C49.8178 11.3289 50.2467 8.64338 50.6222 5.85279C51.4768 5.85279 52.2612 5.82317 53.0421 5.86241C53.6386 5.89201 53.8751 6.17626 53.8249 6.78989ZM61.0934 4.03705C60.9707 2.09399 60.1129 1.0155 58.2263 0.484033C57.0311 0.147236 55.8031 0.0569315 54.5689 0.0554511C48.6789 0.0473087 42.789 0.0465707 36.8988 0.0465707C36.7119 0.0465707 36.525 0.0880225 36.3114 0.11319C35.8071 3.52852 34.964 6.8158 33.825 10.0246C32.6803 13.2497 31.301 16.3675 29.5629 19.3165C29.5086 19.3024 29.4543 19.2876 29.4 19.2736C30.2909 12.8885 31.1819 6.50343 32.0785 0.0769165C31.7631 0.0628524 31.5445 0.0443486 31.3257 0.0450888C21.4689 0.0532312 11.612 0.0628532 1.75499 0.0739563C1.73902 0.0739563 1.72024 0.101345 1.70796 0.11911C1.69428 0.139836 1.68652 0.163521 1.66152 0.217557C1.8211 0.385584 1.98638 0.565458 2.15861 0.737927C2.87177 1.45445 3.57451 2.18208 4.30779 2.87788C4.58962 3.14509 4.71126 3.41083 4.61446 3.78834C4.57202 3.9534 4.57919 4.13105 4.55501 4.30204C4.13283 7.27843 3.70548 10.2533 3.28693 13.2305C2.54588 18.5008 1.8089 23.7711 1.07355 29.0421C0.976013 29.7416 0.898737 30.4433 0.806152 31.1917C3.18643 31.1917 5.49098 31.1917 7.87163 31.1917C8.43734 27.1516 8.99957 23.1375 9.57202 19.05C11.8227 19.05 14.0039 19.05 16.2367 19.05C16.5198 17.0078 16.7923 15.0425 17.0792 12.9729C14.8188 12.9729 12.6631 12.9729 10.4184 12.9729C10.7491 10.636 11.0653 8.40281 11.3788 6.18662C12.5042 6.03636 20.0601 6.08743 20.5866 6.24732C20.5717 6.48566 20.5569 6.73067 20.5412 6.97642C20.434 8.64856 20.2892 10.32 20.2268 11.9936C20.0767 16.0285 20.3917 20.0256 21.3233 23.9613C21.9045 26.4166 22.7174 28.7897 23.9922 30.9829C24.187 31.3175 24.4197 31.6306 24.6659 32C25.0127 31.8024 25.314 31.6439 25.6017 31.4648C27.5542 30.2442 29.3326 28.803 30.9697 27.1871C36.9424 21.2936 40.5354 14.1239 42.2861 5.97418C42.5326 4.82685 42.7206 3.66694 42.9443 2.46632C43.5729 2.84901 43.9557 3.27537 43.7448 4.04149C43.6344 4.44268 43.6075 4.86682 43.5495 5.28208C43.1333 8.25847 42.7196 11.2363 42.3033 14.2135C41.9313 16.873 41.5569 19.5326 41.1837 22.1922C40.7762 25.096 40.3681 27.9992 39.9652 30.9037C39.9533 30.9896 39.9964 31.0829 40.0191 31.1998C42.3572 31.1998 44.6658 31.1998 47.0594 31.1998C47.6102 27.3396 48.1583 23.4987 48.7145 19.6007C49.3889 19.6007 50.0006 19.5918 50.612 19.6029C51.3052 19.6163 51.6714 19.9205 51.7553 20.5993C51.8001 20.9627 51.7965 21.3424 51.7475 21.7051C51.4412 23.9761 51.1144 26.2441 50.7974 28.5136C50.6754 29.3863 50.5614 30.2605 50.4366 31.1872C52.8354 31.1872 55.1624 31.1872 57.5361 31.1872C57.5846 30.9193 57.6351 30.6817 57.6696 30.4426C57.9996 28.1501 58.3503 25.8599 58.6454 23.5631C58.8084 22.2943 58.9622 21.0145 58.9667 19.7384C58.9727 18.0233 58.2458 17.1736 56.6076 16.6917C56.4909 16.6569 56.371 16.634 56.2527 16.6058C56.2411 16.5747 56.2296 16.5429 56.2181 16.5118C56.4066 16.463 56.5928 16.4001 56.7842 16.3682C58.3235 16.1121 59.2972 15.2076 59.789 13.7501C59.8836 13.471 59.9946 13.1912 60.0441 12.9026C60.2904 11.471 60.5403 10.0394 60.7466 8.60193C60.964 7.08968 61.1903 5.57595 61.0934 4.03705Z" fill="black"/>
3 | <path fill-rule="evenodd" clip-rule="evenodd" d="M82.518 19.6681C81.3237 19.6681 80.1812 19.6681 78.9544 19.6681C80.1509 15.1698 81.3371 10.7078 82.5232 6.24583C82.5927 6.24805 82.6622 6.24953 82.7317 6.25101C82.6607 10.7056 82.5898 15.1595 82.518 19.6681ZM74.3696 0.196825C75.1009 0.929634 75.7864 1.66836 76.5318 2.3427C76.9755 2.74389 77.0502 3.11326 76.8853 3.68914C74.377 12.4754 71.893 21.2699 69.4053 30.0629C69.307 30.4108 69.2286 30.7653 69.1251 31.1806C71.5173 31.1806 73.8423 31.1806 76.222 31.1806C76.6857 29.4411 77.1471 27.7141 77.6011 26.0109C79.1496 26.0109 80.6175 26.0109 82.1194 26.0109C82.1194 27.7482 82.1194 29.4403 82.1194 31.1821C84.4503 31.1821 86.7553 31.1821 89.1128 31.1821C89.3029 29.367 89.1276 0.683142 88.9302 0.0843114C87.1029 -0.0726133 74.9419 0.00362985 74.3696 0.196825Z" fill="black"/>
4 | <path fill-rule="evenodd" clip-rule="evenodd" d="M60.9396 0.0909788C61.1519 0.330807 61.285 0.495873 61.4336 0.645396C62.145 1.36266 62.8446 2.09399 63.5818 2.78386C63.942 3.1214 64.0529 3.44783 63.9701 3.94748C63.7157 5.47749 63.5249 7.01787 63.3119 8.55455C62.8483 11.8966 62.389 15.2394 61.9217 18.5807C61.4026 22.2877 60.876 25.9939 60.3554 29.7009C60.2874 30.182 60.2386 30.6654 60.1758 31.1931C62.5577 31.1931 64.8634 31.1931 67.2416 31.1931C68.6977 20.7806 70.1419 10.4539 71.5913 0.0909788C68.0084 0.0909788 64.5299 0.0909788 60.9396 0.0909788Z" fill="black"/>
5 | </svg>
6 | 


--------------------------------------------------------------------------------