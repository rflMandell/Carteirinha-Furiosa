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
    │   ├── 0004_jogo_proplayer_streamer_remove_redesocial_fan_and_more.py
    │   ├── 0005_preferencetopic_remove_preferenciasfan_jogos_and_more.py
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
    │   │   ├── home.html
    │   │   ├── instagram_info.html
    │   │   ├── perfil_esports_valido.html
    │   │   ├── preferences.html
    │   │   ├── profile.html
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
├── static
    └── images
    │   ├── banner-furia.jpg
    │   ├── furia-logo.png
    │   ├── furia-torcida.jpg
    │   ├── furia-torcida2.jpg
    │   ├── insta-logo.avif
    │   └── logo-furia.svg
└── teste.md


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
 2 | from .models import *
 3 | # Register your models here.
 4 | 
 5 | @admin.register(PreferenceTopic)
 6 | class PreferenceTopicAdmin(admin.ModelAdmin):
 7 |     list_display = ('name', 'description', 'order')
 8 |     search_fields = ('name',)
 9 |     list_editable = ('order',)
10 | 
11 | @admin.register(PreferenceOption)
12 | class PreferenceOptionAdmin(admin.ModelAdmin):
13 |     list_display = ('name', 'topic', 'order')
14 |     list_filter = ('topic',)
15 |     search_fields = ('name',)
16 |     list_editable = ('order',)
17 | 
18 | @admin.register(UserPreference)
19 | class UserPreferenceAdmin(admin.ModelAdmin):
20 |     list_display = ('user', 'option')
21 |     list_filter = ('user', 'option__topic')


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
 2 | from .models import *
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
21 | class EsportsProfileForm(forms.Form):
22 |     link_perfil_esports = forms.URLField(label="Link do Perfil de Esports", required=False, max_length=500)
23 |     
24 | class InstagramForm(forms.Form):
25 |     username = forms.CharField(label='Usuário do Instagram', max_length=150)
26 | 
27 | class TwitterForm(forms.Form):
28 |     username = forms.CharField(label='Usuário do Twitter (X)', max_length=150)


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
/fans/migrations/0004_jogo_proplayer_streamer_remove_redesocial_fan_and_more.py:
--------------------------------------------------------------------------------
 1 | # Generated by Django 5.2 on 2025-04-29 18:57
 2 | 
 3 | import django.db.models.deletion
 4 | from django.db import migrations, models
 5 | 
 6 | 
 7 | class Migration(migrations.Migration):
 8 | 
 9 |     dependencies = [
10 |         ('fans', '0003_fan_cpf_fan_endereco'),
11 |     ]
12 | 
13 |     operations = [
14 |         migrations.CreateModel(
15 |             name='Jogo',
16 |             fields=[
17 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
18 |                 ('nome', models.CharField(max_length=100)),
19 |                 ('imagem', models.ImageField(upload_to='jogos/')),
20 |             ],
21 |         ),
22 |         migrations.CreateModel(
23 |             name='ProPlayer',
24 |             fields=[
25 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
26 |                 ('nome', models.CharField(max_length=100)),
27 |                 ('imagem', models.ImageField(upload_to='pro_players/')),
28 |             ],
29 |         ),
30 |         migrations.CreateModel(
31 |             name='Streamer',
32 |             fields=[
33 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
34 |                 ('nome', models.CharField(max_length=100)),
35 |                 ('imagem', models.ImageField(upload_to='streamers/')),
36 |             ],
37 |         ),
38 |         migrations.RemoveField(
39 |             model_name='redesocial',
40 |             name='fan',
41 |         ),
42 |         migrations.CreateModel(
43 |             name='PreferenciasFan',
44 |             fields=[
45 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
46 |                 ('fan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fans.fan')),
47 |                 ('jogos', models.ManyToManyField(blank=True, to='fans.jogo')),
48 |                 ('pro_players', models.ManyToManyField(blank=True, to='fans.proplayer')),
49 |                 ('streamers', models.ManyToManyField(blank=True, to='fans.streamer')),
50 |             ],
51 |         ),
52 |         migrations.DeleteModel(
53 |             name='PerfilEsports',
54 |         ),
55 |         migrations.DeleteModel(
56 |             name='RedeSocial',
57 |         ),
58 |     ]
59 | 


--------------------------------------------------------------------------------
/fans/migrations/0005_preferencetopic_remove_preferenciasfan_jogos_and_more.py:
--------------------------------------------------------------------------------
  1 | # Generated by Django 5.2 on 2025-05-02 18:40
  2 | 
  3 | import django.db.models.deletion
  4 | from django.conf import settings
  5 | from django.db import migrations, models
  6 | 
  7 | 
  8 | class Migration(migrations.Migration):
  9 | 
 10 |     dependencies = [
 11 |         ('fans', '0004_jogo_proplayer_streamer_remove_redesocial_fan_and_more'),
 12 |         migrations.swappable_dependency(settings.AUTH_USER_MODEL),
 13 |     ]
 14 | 
 15 |     operations = [
 16 |         migrations.CreateModel(
 17 |             name='PreferenceTopic',
 18 |             fields=[
 19 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
 20 |                 ('name', models.CharField(max_length=100)),
 21 |                 ('description', models.TextField(blank=True, null=True)),
 22 |                 ('order', models.PositiveBigIntegerField(default=0)),
 23 |             ],
 24 |             options={
 25 |                 'ordering': ['order', 'name'],
 26 |             },
 27 |         ),
 28 |         migrations.RemoveField(
 29 |             model_name='preferenciasfan',
 30 |             name='jogos',
 31 |         ),
 32 |         migrations.RemoveField(
 33 |             model_name='preferenciasfan',
 34 |             name='fan',
 35 |         ),
 36 |         migrations.RemoveField(
 37 |             model_name='preferenciasfan',
 38 |             name='pro_players',
 39 |         ),
 40 |         migrations.RemoveField(
 41 |             model_name='preferenciasfan',
 42 |             name='streamers',
 43 |         ),
 44 |         migrations.CreateModel(
 45 |             name='PerfilEsports',
 46 |             fields=[
 47 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
 48 |                 ('site', models.CharField(max_length=100)),
 49 |                 ('url', models.URLField()),
 50 |                 ('verificado', models.BooleanField(default=False)),
 51 |                 ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfis_esports', to='fans.fan')),
 52 |             ],
 53 |         ),
 54 |         migrations.CreateModel(
 55 |             name='PreferenceOption',
 56 |             fields=[
 57 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
 58 |                 ('name', models.CharField(max_length=100)),
 59 |                 ('image', models.ImageField(upload_to='preferences/')),
 60 |                 ('order', models.PositiveIntegerField(default=0)),
 61 |                 ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='fans.preferencetopic')),
 62 |             ],
 63 |             options={
 64 |                 'ordering': ['topic', 'order', 'name'],
 65 |             },
 66 |         ),
 67 |         migrations.CreateModel(
 68 |             name='RedeSocial',
 69 |             fields=[
 70 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
 71 |                 ('plataforma', models.CharField(max_length=50)),
 72 |                 ('usuario', models.CharField(max_length=255)),
 73 |                 ('url', models.URLField()),
 74 |                 ('dados_extraidos', models.JSONField(blank=True, null=True)),
 75 |                 ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='redes_sociais', to='fans.fan')),
 76 |             ],
 77 |         ),
 78 |         migrations.CreateModel(
 79 |             name='UserPreference',
 80 |             fields=[
 81 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
 82 |                 ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fans.preferenceoption')),
 83 |                 ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preferences', to=settings.AUTH_USER_MODEL)),
 84 |             ],
 85 |             options={
 86 |                 'unique_together': {('user', 'option')},
 87 |             },
 88 |         ),
 89 |         migrations.DeleteModel(
 90 |             name='Jogo',
 91 |         ),
 92 |         migrations.DeleteModel(
 93 |             name='ProPlayer',
 94 |         ),
 95 |         migrations.DeleteModel(
 96 |             name='PreferenciasFan',
 97 |         ),
 98 |         migrations.DeleteModel(
 99 |             name='Streamer',
100 |         ),
101 |     ]
102 | 


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
 2 | from django.contrib.auth.models import User
 3 | 
 4 | # Create your models here.
 5 | class Fan(models.Model):
 6 |     nome = models.CharField(max_length=255)
 7 |     cpf = models.CharField(max_length=14)
 8 |     endereco = models.TextField()
 9 |     email = models.EmailField()
10 |     numero_whatsapp = models.CharField(max_length=20)
11 | 
12 |     # campos para redes sociais
13 |     twitter_username = models.CharField(max_length=100, blank=True, null=True)
14 |     twitch_username = models.CharField(max_length=100, blank=True, null=True)
15 |     instagram_username = models.CharField(max_length=100, blank=True, null=True)
16 | 
17 |     def __str__(self):
18 |         return self.nome
19 |     
20 | class PreferenceTopic(models.Model):
21 |     name = models.CharField(max_length=100)
22 |     description = models.TextField(blank=True, null=True)
23 |     order = models.PositiveBigIntegerField(default=0)
24 |     
25 |     def __str__(self):
26 |         return self.name
27 |     
28 |     class Meta:
29 |         ordering = ['order', 'name']
30 | 
31 | class PreferenceOption(models.Model):
32 |     name = models.CharField(max_length=100)
33 |     image = models.ImageField(upload_to='preferences/')
34 |     topic = models.ForeignKey(PreferenceTopic, related_name='options', on_delete=models.CASCADE)
35 |     order = models.PositiveIntegerField(default=0)
36 |     
37 |     def __str__(self):
38 |         return f"{self.topic.name} - {self.name}"
39 |     
40 |     class Meta:
41 |         ordering = ['topic', 'order', 'name']
42 |         
43 | class UserPreference(models.Model):
44 |     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='preferences')
45 |     option = models.ForeignKey(PreferenceOption, on_delete=models.CASCADE)
46 |     
47 |     class Meta:
48 |         unique_together = ('user', 'option')
49 |         
50 |     def __str__(self):
51 |         return f"{self.user.username} - {self.option.name}"
52 |     
53 | class RedeSocial(models.Model):
54 |     fan = models.ForeignKey(Fan, on_delete=models.CASCADE, related_name='redes_sociais')
55 |     plataforma = models.CharField(max_length=50)  # Ex: Twitter, Instagram, Twitch  YouTube e por ai vai
56 |     usuario = models.CharField(max_length=255)
57 |     url = models.URLField()
58 |     dados_extraidos = models.JSONField(null=True, blank=True)  # Dados públicos coletados
59 | 
60 | class PerfilEsports(models.Model):
61 |     fan = models.ForeignKey(Fan, on_delete=models.CASCADE, related_name='perfis_esports')
62 |     site = models.CharField(max_length=100)  # Ex: HLTV, Liquipedia, VLR?
63 |     url = models.URLField()
64 |     verificado = models.BooleanField(default=False)


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
/fans/templates/fans/preferences.html:
--------------------------------------------------------------------------------
  1 | {% extends 'fans/base.html' %}
  2 | {% load static %}
  3 | 
  4 | {% block title %}Preferencias | Carteirinha Furiosa{% endblock %}
  5 | 
  6 | {% block content %}
  7 | <div class="preferences-container">
  8 |     <h1>Selecione seus preferidos para ser os melhores entre os Melhores na sua Carteirinha Furiosa</h1>
  9 |     <p>Clique nas opções que você gosta e então salve suas escolhas.</p>
 10 |     
 11 |     <form method="post" id="preferences-form">
 12 |         {% csrf_token %}
 13 |         
 14 |         {% for topic in topics %}
 15 |             <div class="topic-section">
 16 |                 <h2 class="topic-title">{{ topic.name }}</h2>
 17 |                 {% if topic.description %}
 18 |                     <p class="topic-description">{{ topic.description }}</p>
 19 |                 {% endif %}
 20 |                 
 21 |                 <div class="options-grid">
 22 |                     {% for option in topic.options.all %}
 23 |                         <div class="option-item {% if option.id in current_preferences %}selected{% endif %}" 
 24 |                              data-option-id="{{ option.id }}">
 25 |                             <div class="option-image">
 26 |                                 <img src="{{ option.image.url }}" alt="{{ option.name }}">
 27 |                             </div>
 28 |                             <div class="option-name">{{ option.name }}</div>
 29 |                             <input type="checkbox" name="selected_options" value="{{ option.id }}" 
 30 |                                    {% if option.id in current_preferences %}checked{% endif %} class="hidden-checkbox">
 31 |                         </div>
 32 |                     {% endfor %}
 33 |                 </div>
 34 |             </div>
 35 |         {% endfor %}
 36 |         
 37 |         <div class="actions">
 38 |             <button type="submit" class="save-button">Salvar preferências</button>
 39 |         </div>
 40 |     </form>
 41 | </div>
 42 | 
 43 | <style>
 44 |     .preferences-container {
 45 |         padding: 20px;
 46 |         max-width: 1200px;
 47 |         margin: 0 auto;
 48 |     }
 49 |     
 50 |     .topic-section {
 51 |         margin-bottom: 40px;
 52 |         background-color: #f8f9fa;
 53 |         border-radius: 10px;
 54 |         padding: 20px;
 55 |     }
 56 |     
 57 |     .topic-title {
 58 |         font-size: 24px;
 59 |         margin-bottom: 5px;
 60 |         color: #333;
 61 |         border-bottom: 2px solid #4a90e2;
 62 |         padding-bottom: 10px;
 63 |     }
 64 |     
 65 |     .topic-description {
 66 |         color: #666;
 67 |         margin-bottom: 20px;
 68 |     }
 69 |     
 70 |     .options-grid {
 71 |         display: grid;
 72 |         grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
 73 |         gap: 20px;
 74 |         margin: 20px 0;
 75 |     }
 76 |     
 77 |     .option-item {
 78 |         display: flex;
 79 |         flex-direction: column;
 80 |         align-items: center;
 81 |         cursor: pointer;
 82 |         padding: 15px;
 83 |         border-radius: 10px;
 84 |         transition: all 0.3s ease;
 85 |         border: 2px solid transparent;
 86 |         background-color: white;
 87 |     }
 88 |     
 89 |     .option-item:hover {
 90 |         transform: translateY(-5px);
 91 |         box-shadow: 0 5px 15px rgba(0,0,0,0.1);
 92 |     }
 93 |     
 94 |     .option-item.selected {
 95 |         border-color: #4a90e2;
 96 |         transform: scale(1.05);
 97 |         box-shadow: 0 8px 20px rgba(74,144,226,0.2);
 98 |         background-color: rgba(74,144,226,0.05);
 99 |     }
100 |     
101 |     .option-image {
102 |         width: 100px;
103 |         height: 100px;
104 |         overflow: hidden;
105 |         border-radius: 50%;
106 |         margin-bottom: 10px;
107 |     }
108 |     
109 |     .option-image img {
110 |         width: 100%;
111 |         height: 100%;
112 |         object-fit: cover;
113 |     }
114 |     
115 |     .option-name {
116 |         font-weight: 600;
117 |         text-align: center;
118 |         margin-top: 5px;
119 |     }
120 |     
121 |     .hidden-checkbox {
122 |         display: none;
123 |     }
124 |     
125 |     .save-button {
126 |         background-color: #4a90e2;
127 |         color: white;
128 |         border: none;
129 |         padding: 12px 24px;
130 |         font-size: 16px;
131 |         border-radius: 5px;
132 |         cursor: pointer;
133 |         transition: background-color 0.3s;
134 |     }
135 |     
136 |     .save-button:hover {
137 |         background-color: #3a80d2;
138 |     }
139 | 
140 |     .actions {
141 |         display: flex;
142 |         justify-content: center;
143 |         margin-top: 30px;
144 |     }
145 | </style>
146 | 
147 | <script>
148 |     document.addEventListener('DOMContentLoaded', function() {
149 |         const optionItems = document.querySelectorAll('.option-item');
150 |         
151 |         optionItems.forEach(item => {
152 |             item.addEventListener('click', function() {
153 |                 // Toggle selected class
154 |                 this.classList.toggle('selected');
155 |                 
156 |                 // Toggle checkbox
157 |                 const checkbox = this.querySelector('input[type="checkbox"]');
158 |                 checkbox.checked = !checkbox.checked;
159 |                 
160 |                 // Add animation effect
161 |                 this.animate([
162 |                     { transform: 'scale(1)' },
163 |                     { transform: 'scale(1.1)' },
164 |                     { transform: 'scale(1.05)' }
165 |                 ], {
166 |                     duration: 300,
167 |                     easing: 'ease-out'
168 |                 });
169 |             });
170 |         });
171 |     });
172 | </script>
173 | {% endblock %}


--------------------------------------------------------------------------------
/fans/templates/fans/profile.html:
--------------------------------------------------------------------------------
  1 | {% extends 'fans/base.html' %}
  2 | {% load static %}
  3 | 
  4 | {% block title %}Profile | Carteirinha Furiosa{% endblock %}
  5 | 
  6 | {% block content %}
  7 | <div class="profile-container">
  8 |     <div class="profile-header">
  9 |         <h1>{{ user.username }}</h1>
 10 |         <!-- Outras informações do perfil -->
 11 |     </div>
 12 |     
 13 |     <div class="profile-section">
 14 |         <h2>Suas preferências</h2>
 15 |         
 16 |         {% if user.preferences.exists %}
 17 |             {% regroup user.preferences.all|dictsort:"option.topic.name" by option.topic as topic_list %}
 18 |             
 19 |             {% for topic in topic_list %}
 20 |                 <div class="preference-topic">
 21 |                     <h3>{{ topic.grouper }}</h3>
 22 |                     <div class="preferences-list">
 23 |                         {% for preference in topic.list %}
 24 |                             <div class="preference-item">
 25 |                                 <div class="preference-image">
 26 |                                     <img src="{{ preference.option.image.url }}" alt="{{ preference.option.name }}">
 27 |                                 </div>
 28 |                                 <div class="preference-name">{{ preference.option.name }}</div>
 29 |                             </div>
 30 |                         {% endfor %}
 31 |                     </div>
 32 |                 </div>
 33 |             {% endfor %}
 34 |             
 35 |             <a href="{% url 'select_preferences' %}" class="btn">Editar preferências</a>
 36 |         {% else %}
 37 |             <p>Você ainda não selecionou suas preferências.</p>
 38 |             <a href="{% url 'select_preferences' %}" class="btn">Adicionar preferências</a>
 39 |         {% endif %}
 40 |     </div>
 41 | </div>
 42 | 
 43 | <style>
 44 |     .profile-container {
 45 |         max-width: 1000px;
 46 |         margin: 0 auto;
 47 |         padding: 20px;
 48 |     }
 49 |     
 50 |     .profile-section {
 51 |         margin: 30px 0;
 52 |         padding: 20px;
 53 |         background-color: #f8f9fa;
 54 |         border-radius: 8px;
 55 |     }
 56 |     
 57 |     .preference-topic {
 58 |         margin: 25px 0;
 59 |     }
 60 |     
 61 |     .preference-topic h3 {
 62 |         font-size: 18px;
 63 |         color: #333;
 64 |         margin-bottom: 15px;
 65 |         padding-bottom: 8px;
 66 |         border-bottom: 1px solid #ddd;
 67 |     }
 68 |     
 69 |     .preferences-list {
 70 |         display: flex;
 71 |         flex-wrap: wrap;
 72 |         gap: 15px;
 73 |         margin-top: 15px;
 74 |     }
 75 |     
 76 |     .preference-item {
 77 |         display: flex;
 78 |         flex-direction: column;
 79 |         align-items: center;
 80 |         width: 100px;
 81 |         transition: transform 0.2s;
 82 |     }
 83 |     
 84 |     .preference-item:hover {
 85 |         transform: scale(1.05);
 86 |     }
 87 |     
 88 |     .preference-image {
 89 |         width: 70px;
 90 |         height: 70px;
 91 |         border-radius: 50%;
 92 |         overflow: hidden;
 93 |         box-shadow: 0 3px 10px rgba(0,0,0,0.1);
 94 |     }
 95 |     
 96 |     .preference-image img {
 97 |         width: 100%;
 98 |         height: 100%;
 99 |         object-fit: cover;
100 |     }
101 |     
102 |     .preference-name {
103 |         margin-top: 8px;
104 |         text-align: center;
105 |         font-size: 14px;
106 |         font-weight: 500;
107 |     }
108 |     
109 |     .btn {
110 |         display: inline-block;
111 |         padding: 8px 16px;
112 |         background-color: #4a90e2;
113 |         color: white;
114 |         text-decoration: none;
115 |         border-radius: 4px;
116 |         margin-top: 20px;
117 |         transition: background-color 0.3s;
118 |     }
119 |     
120 |     .btn:hover {
121 |         background-color: #3a80d2;
122 |     }
123 | </style>
124 | {% endblock %}


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
 6 |     path('cadastro/preferences/', views.select_preferences, name='preferences'),
 7 |     path('cadastro/finalizado/', views.cadastro_finalizado, name='cadastro_finalizado'),
 8 |     path('vincular_perfil_esports/<int:fan_id>/', views.vincular_perfil_esports, name='vincular_perfil_esports'),
 9 |     path('instagram/', views.instagram_info_view, name='instagram_info'),
10 |     path('twitter/', views.twitter_info_view, name='twitter_info'),
11 |     path('', views.home, name='home'),
12 |     path('profile/', views.profile_view, name='profile'),
13 | ]
14 | 


--------------------------------------------------------------------------------
/fans/views.py:
--------------------------------------------------------------------------------
  1 | from django.shortcuts import render, redirect
  2 | from django.http import HttpResponse
  3 | from .forms import *
  4 | from .models import *
  5 | from fans.services.rede_sociais.twitter_service import obter_dados_twitter
  6 | from fans.services.rede_sociais.instagram_service import buscar_informacoes_instagram
  7 | from .services.esports_service import validar_link_esports
  8 | 
  9 | def cadastro_fan(request):
 10 |     if request.method == 'POST':
 11 |         fan_form = FanForm(request.POST)
 12 |         
 13 |         if fan_form.is_valid():
 14 |             fan = fan_form.save()
 15 |             return redirect('preferences', fan_id=fan.id)
 16 |     else:
 17 |         fan_form = FanForm()
 18 | 
 19 |     return render(request, 'fans/cadastro_fan.html', {
 20 |         'fan_form': fan_form,
 21 |     })
 22 | 
 23 | def select_preferences(request):
 24 |     topics = PreferenceTopic.objects.prefetch_related('options').all()
 25 |     
 26 |     if request.method == 'POST':
 27 |         #vai limpar as preferencias anteriores
 28 |         UserPreference.objects.filter(user=request.user).delete()
 29 |         
 30 |         #vai add novas preferencias
 31 |         selected_ids = request.POST.getlist('selected_options')
 32 |         for option_id in selected_ids:
 33 |             UserPreference.objects.create(
 34 |                 user=request.user,
 35 |                 option_id=option_id
 36 |             )
 37 |         return redirect('profile')
 38 | 
 39 |     #obtem as preferencias atuais do user (se ja existirem)
 40 |     current_preferences = UserPreference.objects.filter(
 41 |         user=request.user
 42 |     ).values_list('option_id', flat=True)
 43 |     
 44 |     context = {
 45 |         'topics': topics,
 46 |         'current_preferences': list(current_preferences)
 47 |     }
 48 |     return render(request, 'preferences.html', context)
 49 | 
 50 | def cadastro_finalizado(request):
 51 |     return render(request, 'fans/cadastro_finalizado.html')
 52 | 
 53 | #em breve vai de delete no betinha
 54 | def vincular_perfil_esports(request, fan_id):
 55 |     fan = Fan.objects.get(id=fan_id)
 56 | 
 57 |     if request.method == 'POST':
 58 |         form = EsportsProfileForm(request.POST)
 59 |         if form.is_valid():
 60 |             link_perfil = form.cleaned_data['link_perfil_esports']
 61 | 
 62 |             if link_perfil and validar_link_esports(link_perfil):
 63 |                 # Armazenar o link do perfil de esports no banco de dados
 64 |                 fan.perfil_esports_link = link_perfil
 65 |                 fan.save()
 66 | 
 67 |                 return render(request, 'fans/perfil_esports_valido.html', {'fan': fan})
 68 |             else:
 69 |                 return HttpResponse("Link de perfil de esports inválido ou não pertence a plataformas válidas.", status=400)
 70 |     else:
 71 |         form = EsportsProfileForm()
 72 | 
 73 |     return render(request, 'fans/vincular_perfil_esports.html', {'form': form, 'fan': fan})
 74 | 
 75 | def instagram_info_view(request):
 76 |     dados_instagram = None
 77 | 
 78 |     if request.method == 'POST':
 79 |         form = InstagramForm(request.POST)
 80 |         if form.is_valid():
 81 |             username = form.cleaned_data['username']
 82 |             dados_instagram = buscar_informacoes_instagram(username)
 83 |     else:
 84 |         form = InstagramForm()
 85 | 
 86 |     return render(request, 'fans/instagram_info.html', {'form': form, 'dados_instagram': dados_instagram})
 87 | 
 88 | def twitter_info_view(request):
 89 |     dados_twitter = None
 90 | 
 91 |     if request.method == 'POST':
 92 |         form = TwitterForm(request.POST)
 93 |         if form.is_valid():
 94 |             username = form.cleaned_data['username']
 95 |             dados_twitter = obter_dados_twitter(username)
 96 |     else:
 97 |         form = TwitterForm()
 98 | 
 99 |     return render(request, 'fans/twitter_info.html', {'form': form, 'dados_twitter': dados_twitter})
100 | 
101 | def home(request):
102 |     return render(request, 'fans/home.html')
103 | 
104 | def profile_view(request):
105 |     user = request.user
106 |     #preferencias ordenada por topico
107 |     preferences = UserPreference.objects.filter(user=user).select_related(
108 |         'option', 'option__topic'
109 |     ).order_by('option__topic__order', 'option__order')
110 |     
111 |     return render(request, 'profile.html', {
112 |         'user': user,
113 |         'preferences': preferences
114 |     })


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
/teste.md:
--------------------------------------------------------------------------------
   1 | ├── .gitignore
   2 | ├── core
   3 |     ├── __init__.py
   4 |     ├── __pycache__
   5 |     │   ├── __init__.cpython-311.pyc
   6 |     │   ├── settings.cpython-311.pyc
   7 |     │   ├── urls.cpython-311.pyc
   8 |     │   └── wsgi.cpython-311.pyc
   9 |     ├── asgi.py
  10 |     ├── settings.py
  11 |     ├── urls.py
  12 |     └── wsgi.py
  13 | ├── db.sqlite3
  14 | ├── fans
  15 |     ├── __init__.py
  16 |     ├── __pycache__
  17 |     │   ├── __init__.cpython-311.pyc
  18 |     │   ├── admin.cpython-311.pyc
  19 |     │   ├── apps.cpython-311.pyc
  20 |     │   └── models.cpython-311.pyc
  21 |     ├── admin.py
  22 |     ├── agendador.py
  23 |     ├── apps.py
  24 |     ├── forms.py
  25 |     ├── migrations
  26 |     │   ├── 0001_initial.py
  27 |     │   ├── 0002_rename_telefone_fan_numero_whatsapp_remove_fan_cpf_and_more.py
  28 |     │   ├── 0003_fan_cpf_fan_endereco.py
  29 |     │   ├── __init__.py
  30 |     │   └── __pycache__
  31 |     │   │   ├── 0001_initial.cpython-311.pyc
  32 |     │   │   └── __init__.cpython-311.pyc
  33 |     ├── models.py
  34 |     ├── services
  35 |     │   ├── esports_service.py
  36 |     │   ├── notificacao_service.py
  37 |     │   └── rede_sociais
  38 |     │   │   ├── instagram_service.py
  39 |     │   │   └── twitter_service.py
  40 |     ├── templates
  41 |     │   ├── fans
  42 |     │   │   ├── base.html
  43 |     │   │   ├── cadastro_fan.html
  44 |     │   │   ├── cadastro_finalizado.html
  45 |     │   │   ├── cadastro_redes_sociais.html
  46 |     │   │   ├── home.html
  47 |     │   │   ├── instagram_info.html
  48 |     │   │   ├── perfil_esports_valido.html
  49 |     │   │   ├── twitter_info.html
  50 |     │   │   ├── vincular_perfil_esports.html
  51 |     │   │   └── vincular_twitter.html
  52 |     │   └── partials
  53 |     │   │   ├── footer.html
  54 |     │   │   └── navbar.html
  55 |     ├── tests.py
  56 |     ├── urls.py
  57 |     └── views.py
  58 | ├── manage.py
  59 | ├── readme.md
  60 | ├── requirements.txt
  61 | ├── scheduler.py
  62 | └── static
  63 |     └── images
  64 |         ├── banner-furia.jpg
  65 |         ├── furia-logo.png
  66 |         ├── furia-torcida.jpg
  67 |         ├── furia-torcida2.jpg
  68 |         ├── insta-logo.avif
  69 |         └── logo-furia.svg
  70 | 
  71 | 
  72 | /.gitignore:
  73 | --------------------------------------------------------------------------------
  74 |  1 | # Ignorar o arquivo .env (credenciais e tokens)
  75 |  2 | .env
  76 |  3 | 
  77 |  4 | # Ignorar arquivos de banco de dados SQLite
  78 |  5 | .sqlite3
  79 |  6 | 
  80 |  7 | # Ignorar diretórios de cache
  81 |  8 | __pycache__/
  82 |  9 | .pyc
  83 | 10 | 
  84 | 11 | # Ignorar ambientes virtuais
  85 | 12 | venv/
  86 | 
  87 | 
  88 | --------------------------------------------------------------------------------
  89 | /core/__init__.py:
  90 | --------------------------------------------------------------------------------
  91 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/core/__init__.py
  92 | 
  93 | 
  94 | --------------------------------------------------------------------------------
  95 | /core/__pycache__/__init__.cpython-311.pyc:
  96 | --------------------------------------------------------------------------------
  97 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/core/__pycache__/__init__.cpython-311.pyc
  98 | 
  99 | 
 100 | --------------------------------------------------------------------------------
 101 | /core/__pycache__/settings.cpython-311.pyc:
 102 | --------------------------------------------------------------------------------
 103 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/core/__pycache__/settings.cpython-311.pyc
 104 | 
 105 | 
 106 | --------------------------------------------------------------------------------
 107 | /core/__pycache__/urls.cpython-311.pyc:
 108 | --------------------------------------------------------------------------------
 109 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/core/__pycache__/urls.cpython-311.pyc
 110 | 
 111 | 
 112 | --------------------------------------------------------------------------------
 113 | /core/__pycache__/wsgi.cpython-311.pyc:
 114 | --------------------------------------------------------------------------------
 115 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/core/__pycache__/wsgi.cpython-311.pyc
 116 | 
 117 | 
 118 | --------------------------------------------------------------------------------
 119 | /core/asgi.py:
 120 | --------------------------------------------------------------------------------
 121 |  1 | """
 122 |  2 | ASGI config for core project.
 123 |  3 | 
 124 |  4 | It exposes the ASGI callable as a module-level variable named ``application``.
 125 |  5 | 
 126 |  6 | For more information on this file, see
 127 |  7 | https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
 128 |  8 | """
 129 |  9 | 
 130 | 10 | import os
 131 | 11 | 
 132 | 12 | from django.core.asgi import get_asgi_application
 133 | 13 | 
 134 | 14 | os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
 135 | 15 | 
 136 | 16 | application = get_asgi_application()
 137 | 17 | 
 138 | 
 139 | 
 140 | --------------------------------------------------------------------------------
 141 | /core/settings.py:
 142 | --------------------------------------------------------------------------------
 143 |   1 | """
 144 |   2 | Django settings for core project.
 145 |   3 | 
 146 |   4 | Generated by 'django-admin startproject' using Django 5.2.
 147 |   5 | 
 148 |   6 | For more information on this file, see
 149 |   7 | https://docs.djangoproject.com/en/5.2/topics/settings/
 150 |   8 | 
 151 |   9 | For the full list of settings and their values, see
 152 |  10 | https://docs.djangoproject.com/en/5.2/ref/settings/
 153 |  11 | """
 154 |  12 | 
 155 |  13 | from pathlib import Path
 156 |  14 | import os
 157 |  15 | from dotenv import load_dotenv
 158 |  16 | 
 159 |  17 | # Build paths inside the project like this: BASE_DIR / 'subdir'.
 160 |  18 | BASE_DIR = Path(__file__).resolve().parent.parent
 161 |  19 | 
 162 |  20 | 
 163 |  21 | # Quick-start development settings - unsuitable for production
 164 |  22 | # See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
 165 |  23 | 
 166 |  24 | # SECURITY WARNING: keep the secret key used in production secret!
 167 |  25 | SECRET_KEY = 'django-insecure-bn6u0=2@8k_*qyq_(64j^pld*qkd37^ic+v_@%_n5f2*8e!7t_'
 168 |  26 | 
 169 |  27 | # SECURITY WARNING: don't run with debug turned on in production!
 170 |  28 | DEBUG = True
 171 |  29 | 
 172 |  30 | ALLOWED_HOSTS = []
 173 |  31 | 
 174 |  32 | 
 175 |  33 | # Application definition
 176 |  34 | 
 177 |  35 | INSTALLED_APPS = [
 178 |  36 |     'django.contrib.admin',
 179 |  37 |     'django.contrib.auth',
 180 |  38 |     'django.contrib.contenttypes',
 181 |  39 |     'django.contrib.sessions',
 182 |  40 |     'django.contrib.messages',
 183 |  41 |     'django.contrib.staticfiles',
 184 |  42 |     
 185 |  43 |     'fans',
 186 |  44 | ]
 187 |  45 | 
 188 |  46 | MIDDLEWARE = [
 189 |  47 |     'django.middleware.security.SecurityMiddleware',
 190 |  48 |     'django.contrib.sessions.middleware.SessionMiddleware',
 191 |  49 |     'django.middleware.common.CommonMiddleware',
 192 |  50 |     'django.middleware.csrf.CsrfViewMiddleware',
 193 |  51 |     'django.contrib.auth.middleware.AuthenticationMiddleware',
 194 |  52 |     'django.contrib.messages.middleware.MessageMiddleware',
 195 |  53 |     'django.middleware.clickjacking.XFrameOptionsMiddleware',
 196 |  54 | ]
 197 |  55 | 
 198 |  56 | ROOT_URLCONF = 'core.urls'
 199 |  57 | 
 200 |  58 | TEMPLATES = [
 201 |  59 |     {
 202 |  60 |         'BACKEND': 'django.template.backends.django.DjangoTemplates',
 203 |  61 |         'DIRS': [],
 204 |  62 |         'APP_DIRS': True,
 205 |  63 |         'OPTIONS': {
 206 |  64 |             'context_processors': [
 207 |  65 |                 'django.template.context_processors.debug',
 208 |  66 |                 'django.template.context_processors.request',
 209 |  67 |                 'django.contrib.auth.context_processors.auth',
 210 |  68 |                 'django.contrib.messages.context_processors.messages',
 211 |  69 |             ],
 212 |  70 |         },
 213 |  71 |     },
 214 |  72 | ]
 215 |  73 | 
 216 |  74 | WSGI_APPLICATION = 'core.wsgi.application'
 217 |  75 | 
 218 |  76 | 
 219 |  77 | # Database
 220 |  78 | # https://docs.djangoproject.com/en/5.2/ref/settings/#databases
 221 |  79 | 
 222 |  80 | DATABASES = {
 223 |  81 |     'default': {
 224 |  82 |         'ENGINE': 'django.db.backends.sqlite3',
 225 |  83 |         'NAME': BASE_DIR / 'db.sqlite3',
 226 |  84 |     }
 227 |  85 | }
 228 |  86 | 
 229 |  87 | 
 230 |  88 | # Password validation
 231 |  89 | # https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
 232 |  90 | 
 233 |  91 | AUTH_PASSWORD_VALIDATORS = [
 234 |  92 |     {
 235 |  93 |         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
 236 |  94 |     },
 237 |  95 |     {
 238 |  96 |         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
 239 |  97 |     },
 240 |  98 |     {
 241 |  99 |         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
 242 | 100 |     },
 243 | 101 |     {
 244 | 102 |         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
 245 | 103 |     },
 246 | 104 | ]
 247 | 105 | 
 248 | 106 | 
 249 | 107 | # Internationalization
 250 | 108 | # https://docs.djangoproject.com/en/5.2/topics/i18n/
 251 | 109 | 
 252 | 110 | LANGUAGE_CODE = 'en-us'
 253 | 111 | 
 254 | 112 | TIME_ZONE = 'UTC'
 255 | 113 | 
 256 | 114 | USE_I18N = True
 257 | 115 | 
 258 | 116 | USE_TZ = True
 259 | 117 | 
 260 | 118 | 
 261 | 119 | # Static files (CSS, JavaScript, Images)
 262 | 120 | # https://docs.djangoproject.com/en/5.2/howto/static-files/
 263 | 121 | 
 264 | 122 | STATIC_URL = 'static/'
 265 | 123 | 
 266 | 124 | # Default primary key field type
 267 | 125 | # https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
 268 | 126 | 
 269 | 127 | DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 270 | 128 | 
 271 | 129 | #minhas cositas
 272 | 130 | 
 273 | 131 | # Carrega as variáveis de ambiente do arquivo .env
 274 | 132 | load_dotenv()
 275 | 133 | 
 276 | 134 | TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
 277 | 135 | TWITTER_API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
 278 | 136 | TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
 279 | 137 | TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
 280 | 138 | 
 281 | 139 | BASE_DIR = Path(__file__).resolve().parent.parent
 282 | 140 | 
 283 | 141 | STATIC_URL = '/static/'
 284 | 142 | 
 285 | 143 | STATICFILES_DIRS = [
 286 | 144 |     os.path.join(BASE_DIR, "static"),
 287 | 145 | ]
 288 | 
 289 | 
 290 | --------------------------------------------------------------------------------
 291 | /core/urls.py:
 292 | --------------------------------------------------------------------------------
 293 |  1 | """
 294 |  2 | URL configuration for core project.
 295 |  3 | 
 296 |  4 | The `urlpatterns` list routes URLs to views. For more information please see:
 297 |  5 |     https://docs.djangoproject.com/en/5.2/topics/http/urls/
 298 |  6 | Examples:
 299 |  7 | Function views
 300 |  8 |     1. Add an import:  from my_app import views
 301 |  9 |     2. Add a URL to urlpatterns:  path('', views.home, name='home')
 302 | 10 | Class-based views
 303 | 11 |     1. Add an import:  from other_app.views import Home
 304 | 12 |     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
 305 | 13 | Including another URLconf
 306 | 14 |     1. Import the include() function: from django.urls import include, path
 307 | 15 |     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
 308 | 16 | """
 309 | 17 | from django.contrib import admin
 310 | 18 | from django.urls import path, include
 311 | 19 | 
 312 | 20 | urlpatterns = [
 313 | 21 |     path('admin/', admin.site.urls),
 314 | 22 |     path('', include('fans.urls')),
 315 | 23 | ]
 316 | 24 | 
 317 | 
 318 | 
 319 | --------------------------------------------------------------------------------
 320 | /core/wsgi.py:
 321 | --------------------------------------------------------------------------------
 322 |  1 | """
 323 |  2 | WSGI config for core project.
 324 |  3 | 
 325 |  4 | It exposes the WSGI callable as a module-level variable named ``application``.
 326 |  5 | 
 327 |  6 | For more information on this file, see
 328 |  7 | https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
 329 |  8 | """
 330 |  9 | 
 331 | 10 | import os
 332 | 11 | 
 333 | 12 | from django.core.wsgi import get_wsgi_application
 334 | 13 | 
 335 | 14 | os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
 336 | 15 | 
 337 | 16 | application = get_wsgi_application()
 338 | 17 | 
 339 | 
 340 | 
 341 | --------------------------------------------------------------------------------
 342 | /db.sqlite3:
 343 | --------------------------------------------------------------------------------
 344 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/db.sqlite3
 345 | 
 346 | 
 347 | --------------------------------------------------------------------------------
 348 | /fans/__init__.py:
 349 | --------------------------------------------------------------------------------
 350 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/__init__.py
 351 | 
 352 | 
 353 | --------------------------------------------------------------------------------
 354 | /fans/__pycache__/__init__.cpython-311.pyc:
 355 | --------------------------------------------------------------------------------
 356 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/__pycache__/__init__.cpython-311.pyc
 357 | 
 358 | 
 359 | --------------------------------------------------------------------------------
 360 | /fans/__pycache__/admin.cpython-311.pyc:
 361 | --------------------------------------------------------------------------------
 362 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/__pycache__/admin.cpython-311.pyc
 363 | 
 364 | 
 365 | --------------------------------------------------------------------------------
 366 | /fans/__pycache__/apps.cpython-311.pyc:
 367 | --------------------------------------------------------------------------------
 368 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/__pycache__/apps.cpython-311.pyc
 369 | 
 370 | 
 371 | --------------------------------------------------------------------------------
 372 | /fans/__pycache__/models.cpython-311.pyc:
 373 | --------------------------------------------------------------------------------
 374 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/__pycache__/models.cpython-311.pyc
 375 | 
 376 | 
 377 | --------------------------------------------------------------------------------
 378 | /fans/admin.py:
 379 | --------------------------------------------------------------------------------
 380 | 1 | from django.contrib import admin
 381 | 2 | 
 382 | 3 | # Register your models here.
 383 | 4 | 
 384 | 
 385 | 
 386 | --------------------------------------------------------------------------------
 387 | /fans/agendador.py:
 388 | --------------------------------------------------------------------------------
 389 |  1 | import os
 390 |  2 | import django
 391 |  3 | import time
 392 |  4 | import schedule
 393 |  5 | from dotenv import load_dotenv
 394 |  6 | 
 395 |  7 | # Setup do Django
 396 |  8 | os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'know_your_fan.settings')
 397 |  9 | django.setup()
 398 | 10 | 
 399 | 11 | from .models import Usuario
 400 | 12 | from .services.notificacao_service import enviar_notificacao
 401 | 13 | 
 402 | 14 | load_dotenv()
 403 | 15 | 
 404 | 16 | def buscar_informacoes_esports(usuario):
 405 | 17 |     """Simulação de busca de informações de esports para o usuário."""
 406 | 18 |     # mensagem de exemplo
 407 | 19 |     return f"Olá {usuario.nome}, hoje seu time favorito tem jogo! Não perca! 🏆"
 408 | 20 | 
 409 | 21 | def enviar_notificacoes():
 410 | 22 |     """Busca usuários e envia notificações personalizadas."""
 411 | 23 |     usuarios = Usuario.objects.all()
 412 | 24 | 
 413 | 25 |     for usuario in usuarios:
 414 | 26 |         if usuario.numero_whatsapp:
 415 | 27 |             mensagem = buscar_informacoes_esports(usuario)
 416 | 28 |             enviar_notificacao(usuario.numero_whatsapp, mensagem)
 417 | 29 | 
 418 | 30 | def iniciar_agendamento():
 419 | 31 |     """Agendamento periódico para envio de notificações."""
 420 | 32 |     # Agenda o envio a cada 1 hora
 421 | 33 |     schedule.every(1).hours.do(enviar_notificacoes)
 422 | 34 | 
 423 | 35 |     print("Agendamento iniciado. Aguardando execução das tarefas...")
 424 | 36 |     while True:
 425 | 37 |         schedule.run_pending()
 426 | 38 |         time.sleep(1)
 427 | 39 | 
 428 | 
 429 | 
 430 | --------------------------------------------------------------------------------
 431 | /fans/apps.py:
 432 | --------------------------------------------------------------------------------
 433 | 1 | from django.apps import AppConfig
 434 | 2 | 
 435 | 3 | 
 436 | 4 | class FansConfig(AppConfig):
 437 | 5 |     default_auto_field = 'django.db.models.BigAutoField'
 438 | 6 |     name = 'fans'
 439 | 7 | 
 440 | 
 441 | 
 442 | --------------------------------------------------------------------------------
 443 | /fans/forms.py:
 444 | --------------------------------------------------------------------------------
 445 |  1 | from django import forms
 446 |  2 | from .models import Fan, RedeSocial, PerfilEsports
 447 |  3 | 
 448 |  4 | class FanForm(forms.ModelForm):
 449 |  5 |     class Meta:
 450 |  6 |         model = Fan
 451 |  7 |         fields = [
 452 |  8 |             'nome', 'cpf', 'endereco', 'email', 'numero_whatsapp',
 453 |  9 |             'twitter_username', 'twitch_username', 'instagram_username'
 454 | 10 |         ]
 455 | 11 | 
 456 | 12 |     def __init__(self, *args, **kwargs):
 457 | 13 |         super(FanForm, self).__init__(*args, **kwargs)
 458 | 14 |         for field_name, field in self.fields.items():
 459 | 15 |             field.widget.attrs.update({
 460 | 16 |                 'class': 'w-full px-4 py-2 bg-gray-100 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500'
 461 | 17 |             })
 462 | 18 |             if isinstance(field.widget, forms.Textarea):
 463 | 19 |                 field.widget.attrs.update({'rows': 3})
 464 | 20 | 
 465 | 21 | 
 466 | 22 | class RedeSocialForm(forms.ModelForm):
 467 | 23 |     class Meta:
 468 | 24 |         model = RedeSocial
 469 | 25 |         fields = ['plataforma', 'usuario', 'url']
 470 | 26 | 
 471 | 27 | 
 472 | 28 | class PerfilEsportsForm(forms.ModelForm):
 473 | 29 |     class Meta:
 474 | 30 |         model = PerfilEsports
 475 | 31 |         fields = ['site', 'url']
 476 | 32 |     
 477 | 33 | class EsportsProfileForm(forms.Form):
 478 | 34 |     link_perfil_esports = forms.URLField(label="Link do Perfil de Esports", required=False, max_length=500)
 479 | 35 |     
 480 | 36 | class InstagramForm(forms.Form):
 481 | 37 |     username = forms.CharField(label='Usuário do Instagram', max_length=150)
 482 | 38 | 
 483 | 39 | class TwitterForm(forms.Form):
 484 | 40 |     username = forms.CharField(label='Usuário do Twitter (X)', max_length=150)
 485 | 
 486 | 
 487 | --------------------------------------------------------------------------------
 488 | /fans/migrations/0001_initial.py:
 489 | --------------------------------------------------------------------------------
 490 |  1 | # Generated by Django 5.2 on 2025-04-28 23:08
 491 |  2 | 
 492 |  3 | import django.db.models.deletion
 493 |  4 | from django.db import migrations, models
 494 |  5 | 
 495 |  6 | 
 496 |  7 | class Migration(migrations.Migration):
 497 |  8 | 
 498 |  9 |     initial = True
 499 | 10 | 
 500 | 11 |     dependencies = [
 501 | 12 |     ]
 502 | 13 | 
 503 | 14 |     operations = [
 504 | 15 |         migrations.CreateModel(
 505 | 16 |             name='Fan',
 506 | 17 |             fields=[
 507 | 18 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
 508 | 19 |                 ('nome', models.CharField(max_length=255)),
 509 | 20 |                 ('endereco', models.TextField()),
 510 | 21 |                 ('cpf', models.CharField(max_length=14, unique=True)),
 511 | 22 |                 ('telefone', models.CharField(max_length=20)),
 512 | 23 |                 ('jogos_favoritos', models.TextField()),
 513 | 24 |                 ('streamers_favoritos', models.TextField()),
 514 | 25 |                 ('criado_em', models.DateTimeField(auto_now_add=True)),
 515 | 26 |             ],
 516 | 27 |         ),
 517 | 28 |         migrations.CreateModel(
 518 | 29 |             name='DocumentoIdentidade',
 519 | 30 |             fields=[
 520 | 31 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
 521 | 32 |                 ('documento', models.FileField(upload_to='documentos/')),
 522 | 33 |                 ('dados_extraidos', models.JSONField(blank=True, null=True)),
 523 | 34 |                 ('validado', models.BooleanField(default=False)),
 524 | 35 |                 ('fan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fans.fan')),
 525 | 36 |             ],
 526 | 37 |         ),
 527 | 38 |         migrations.CreateModel(
 528 | 39 |             name='PerfilEsports',
 529 | 40 |             fields=[
 530 | 41 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
 531 | 42 |                 ('site', models.CharField(max_length=100)),
 532 | 43 |                 ('url', models.URLField()),
 533 | 44 |                 ('verificado', models.BooleanField(default=False)),
 534 | 45 |                 ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfis_esports', to='fans.fan')),
 535 | 46 |             ],
 536 | 47 |         ),
 537 | 48 |         migrations.CreateModel(
 538 | 49 |             name='RedeSocial',
 539 | 50 |             fields=[
 540 | 51 |                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
 541 | 52 |                 ('plataforma', models.CharField(max_length=50)),
 542 | 53 |                 ('usuario', models.CharField(max_length=255)),
 543 | 54 |                 ('url', models.URLField()),
 544 | 55 |                 ('dados_extraidos', models.JSONField(blank=True, null=True)),
 545 | 56 |                 ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='redes_sociais', to='fans.fan')),
 546 | 57 |             ],
 547 | 58 |         ),
 548 | 59 |     ]
 549 | 60 | 
 550 | 
 551 | 
 552 | --------------------------------------------------------------------------------
 553 | /fans/migrations/0002_rename_telefone_fan_numero_whatsapp_remove_fan_cpf_and_more.py:
 554 | --------------------------------------------------------------------------------
 555 |  1 | # Generated by Django 5.2 on 2025-04-29 13:19
 556 |  2 | 
 557 |  3 | from django.db import migrations, models
 558 |  4 | 
 559 |  5 | 
 560 |  6 | class Migration(migrations.Migration):
 561 |  7 | 
 562 |  8 |     dependencies = [
 563 |  9 |         ('fans', '0001_initial'),
 564 | 10 |     ]
 565 | 11 | 
 566 | 12 |     operations = [
 567 | 13 |         migrations.RenameField(
 568 | 14 |             model_name='fan',
 569 | 15 |             old_name='telefone',
 570 | 16 |             new_name='numero_whatsapp',
 571 | 17 |         ),
 572 | 18 |         migrations.RemoveField(
 573 | 19 |             model_name='fan',
 574 | 20 |             name='cpf',
 575 | 21 |         ),
 576 | 22 |         migrations.RemoveField(
 577 | 23 |             model_name='fan',
 578 | 24 |             name='criado_em',
 579 | 25 |         ),
 580 | 26 |         migrations.RemoveField(
 581 | 27 |             model_name='fan',
 582 | 28 |             name='endereco',
 583 | 29 |         ),
 584 | 30 |         migrations.RemoveField(
 585 | 31 |             model_name='fan',
 586 | 32 |             name='jogos_favoritos',
 587 | 33 |         ),
 588 | 34 |         migrations.RemoveField(
 589 | 35 |             model_name='fan',
 590 | 36 |             name='streamers_favoritos',
 591 | 37 |         ),
 592 | 38 |         migrations.AddField(
 593 | 39 |             model_name='fan',
 594 | 40 |             name='email',
 595 | 41 |             field=models.EmailField(default=1, max_length=254),
 596 | 42 |             preserve_default=False,
 597 | 43 |         ),
 598 | 44 |         migrations.AddField(
 599 | 45 |             model_name='fan',
 600 | 46 |             name='instagram_username',
 601 | 47 |             field=models.CharField(blank=True, max_length=100, null=True),
 602 | 48 |         ),
 603 | 49 |         migrations.AddField(
 604 | 50 |             model_name='fan',
 605 | 51 |             name='twitch_username',
 606 | 52 |             field=models.CharField(blank=True, max_length=100, null=True),
 607 | 53 |         ),
 608 | 54 |         migrations.AddField(
 609 | 55 |             model_name='fan',
 610 | 56 |             name='twitter_username',
 611 | 57 |             field=models.CharField(blank=True, max_length=100, null=True),
 612 | 58 |         ),
 613 | 59 |         migrations.DeleteModel(
 614 | 60 |             name='DocumentoIdentidade',
 615 | 61 |         ),
 616 | 62 |     ]
 617 | 63 | 
 618 | 
 619 | 
 620 | --------------------------------------------------------------------------------
 621 | /fans/migrations/0003_fan_cpf_fan_endereco.py:
 622 | --------------------------------------------------------------------------------
 623 |  1 | # Generated by Django 5.2 on 2025-04-29 16:14
 624 |  2 | 
 625 |  3 | from django.db import migrations, models
 626 |  4 | 
 627 |  5 | 
 628 |  6 | class Migration(migrations.Migration):
 629 |  7 | 
 630 |  8 |     dependencies = [
 631 |  9 |         ('fans', '0002_rename_telefone_fan_numero_whatsapp_remove_fan_cpf_and_more'),
 632 | 10 |     ]
 633 | 11 | 
 634 | 12 |     operations = [
 635 | 13 |         migrations.AddField(
 636 | 14 |             model_name='fan',
 637 | 15 |             name='cpf',
 638 | 16 |             field=models.CharField(default=1, max_length=14),
 639 | 17 |             preserve_default=False,
 640 | 18 |         ),
 641 | 19 |         migrations.AddField(
 642 | 20 |             model_name='fan',
 643 | 21 |             name='endereco',
 644 | 22 |             field=models.TextField(default=1),
 645 | 23 |             preserve_default=False,
 646 | 24 |         ),
 647 | 25 |     ]
 648 | 26 | 
 649 | 
 650 | 
 651 | --------------------------------------------------------------------------------
 652 | /fans/migrations/__init__.py:
 653 | --------------------------------------------------------------------------------
 654 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/migrations/__init__.py
 655 | 
 656 | 
 657 | --------------------------------------------------------------------------------
 658 | /fans/migrations/__pycache__/0001_initial.cpython-311.pyc:
 659 | --------------------------------------------------------------------------------
 660 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/migrations/__pycache__/0001_initial.cpython-311.pyc
 661 | 
 662 | 
 663 | --------------------------------------------------------------------------------
 664 | /fans/migrations/__pycache__/__init__.cpython-311.pyc:
 665 | --------------------------------------------------------------------------------
 666 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/fans/migrations/__pycache__/__init__.cpython-311.pyc
 667 | 
 668 | 
 669 | --------------------------------------------------------------------------------
 670 | /fans/models.py:
 671 | --------------------------------------------------------------------------------
 672 |  1 | from django.db import models
 673 |  2 | 
 674 |  3 | # Create your models here.
 675 |  4 | class Fan(models.Model):
 676 |  5 |     nome = models.CharField(max_length=255)
 677 |  6 |     cpf = models.CharField(max_length=14)
 678 |  7 |     endereco = models.TextField()
 679 |  8 |     email = models.EmailField()
 680 |  9 |     numero_whatsapp = models.CharField(max_length=20)
 681 | 10 | 
 682 | 11 |     # campos para redes sociais
 683 | 12 |     twitter_username = models.CharField(max_length=100, blank=True, null=True)
 684 | 13 |     twitch_username = models.CharField(max_length=100, blank=True, null=True)
 685 | 14 |     instagram_username = models.CharField(max_length=100, blank=True, null=True)
 686 | 15 | 
 687 | 16 |     def __str__(self):
 688 | 17 |         return self.nome
 689 | 18 |     
 690 | 19 | 
 691 | 20 | class RedeSocial(models.Model):
 692 | 21 |     fan = models.ForeignKey(Fan, on_delete=models.CASCADE, related_name='redes_sociais')
 693 | 22 |     plataforma = models.CharField(max_length=50)  # Ex: Twitter, Instagram, Twitch  YouTube e por ai vai
 694 | 23 |     usuario = models.CharField(max_length=255)
 695 | 24 |     url = models.URLField()
 696 | 25 |     dados_extraidos = models.JSONField(null=True, blank=True)  # Dados públicos coletados
 697 | 26 | 
 698 | 27 |     def __str__(self):
 699 | 28 |         return f"{self.plataforma} - {self.usuario}"
 700 | 29 | 
 701 | 30 | 
 702 | 31 | class PerfilEsports(models.Model):
 703 | 32 |     fan = models.ForeignKey(Fan, on_delete=models.CASCADE, related_name='perfis_esports')
 704 | 33 |     site = models.CharField(max_length=100)  # Ex: HLTV, Liquipedia, VLR?
 705 | 34 |     url = models.URLField()
 706 | 35 |     verificado = models.BooleanField(default=False)
 707 | 36 | 
 708 | 37 |     def __str__(self):
 709 | 38 |         return f"{self.site} de {self.fan.nome}"
 710 | 39 | 
 711 | 
 712 | 
 713 | --------------------------------------------------------------------------------
 714 | /fans/services/esports_service.py:
 715 | --------------------------------------------------------------------------------
 716 |  1 | import re
 717 |  2 | from urllib.parse import urlparse
 718 |  3 | 
 719 |  4 | def validar_link_esports(link):
 720 |  5 |     """Valida se o link pertence a plataformas de esports válidas (HLTV, Liquipedia)."""
 721 |  6 |     valid_domains = ['hltv.org', 'liquipedia.net']
 722 |  7 |     try:
 723 |  8 |         parsed_url = urlparse(link)
 724 |  9 |         domain = parsed_url.netloc.lower()
 725 | 10 | 
 726 | 11 |         if any(valid_domain in domain for valid_domain in valid_domains):
 727 | 12 |             return True
 728 | 13 |         return False
 729 | 14 |     except Exception as e:
 730 | 15 |         return False
 731 | 16 | 
 732 | 
 733 | 
 734 | --------------------------------------------------------------------------------
 735 | /fans/services/notificacao_service.py:
 736 | --------------------------------------------------------------------------------
 737 |  1 | import schedule
 738 |  2 | import time
 739 |  3 | import requests
 740 |  4 | from datetime import datetime
 741 |  5 | from twilio.rest import Client
 742 |  6 | import os
 743 |  7 | from dotenv import load_dotenv
 744 |  8 | 
 745 |  9 | load_dotenv()  # Carrega as variáveis do .env
 746 | 10 | 
 747 | 11 | def enviar_notificacao(whatsapp_number, message):
 748 | 12 |     """Envio de notificação real via Twilio WhatsApp API."""
 749 | 13 |     account_sid = os.getenv('TWILIO_ACCOUNT_SID')
 750 | 14 |     auth_token = os.getenv('TWILIO_AUTH_TOKEN')
 751 | 15 |     twilio_number = os.getenv('TWILIO_PHONE_NUMBER')
 752 | 16 | 
 753 | 17 |     client = Client(account_sid, auth_token)
 754 | 18 | 
 755 | 19 |     message = client.messages.create(
 756 | 20 |         body=message,
 757 | 21 |         from_=twilio_number,
 758 | 22 |         to=f'whatsapp:{whatsapp_number}'
 759 | 23 |     )
 760 | 24 | 
 761 | 25 |     print(f"Mensagem enviada para {whatsapp_number}: {message.body}")
 762 | 26 | 
 763 | 27 | # Função que consulta dados atualizados sobre jogos e envia notificações
 764 | 28 | def agendar_notificacao():
 765 | 29 |     """Agendar notificações personalizadas para os usuários com base em suas preferências."""
 766 | 30 |     # Aqui estamos apenas simulando um cenário de notificação.
 767 | 31 |     usuarios = [
 768 | 32 |         {"whatsapp_number": "71996233756", "preferencia": "FURIA vs Team1", "hora": "15:00"},
 769 | 33 |     ]
 770 | 34 |     
 771 | 35 |     for usuario in usuarios:
 772 | 36 |         message = f"Olá! Não perca o jogo {usuario['preferencia']} às {usuario['hora']}!"
 773 | 37 |         enviar_notificacao(usuario['whatsapp_number'], message)
 774 | 38 | 
 775 | 39 | # Agendando a execução da notificação diariamente às 10:00 (exemplo)
 776 | 40 | schedule.every().day.at("10:00").do(agendar_notificacao)
 777 | 41 | 
 778 | 42 | def rodar_agendamentos():
 779 | 43 |     """Fica rodando os agendamentos em loop."""
 780 | 44 |     while True:
 781 | 45 |         schedule.run_pending()
 782 | 46 |         time.sleep(60)
 783 | 47 | 
 784 | 
 785 | 
 786 | --------------------------------------------------------------------------------
 787 | /fans/services/rede_sociais/instagram_service.py:
 788 | --------------------------------------------------------------------------------
 789 |  1 | import instaloader
 790 |  2 | 
 791 |  3 | def buscar_informacoes_instagram(username):
 792 |  4 |     loader = instaloader.Instaloader()
 793 |  5 | 
 794 |  6 |     try:
 795 |  7 |         profile = instaloader.Profile.from_username(loader.context, username)
 796 |  8 |         dados = {
 797 |  9 |             'username': profile.username,
 798 | 10 |             'seguidores': profile.followers,
 799 | 11 |             'seguindo': profile.followees,
 800 | 12 |             'bio': profile.biography,
 801 | 13 |             'url_perfil': f"https://instagram.com/{profile.username}"
 802 | 14 |         }
 803 | 15 |         return dados
 804 | 16 |     except Exception as e:
 805 | 17 |         print(f"Erro ao buscar informações do Instagram: {e}")
 806 | 18 |         return None
 807 | 19 | 
 808 | 
 809 | 
 810 | --------------------------------------------------------------------------------
 811 | /fans/services/rede_sociais/twitter_service.py:
 812 | --------------------------------------------------------------------------------
 813 |  1 | import tweepy
 814 |  2 | from django.conf import settings
 815 |  3 | 
 816 |  4 | # Configuração do Twitter
 817 |  5 | auth = tweepy.OAuth1UserHandler(
 818 |  6 |     settings.TWITTER_API_KEY,
 819 |  7 |     settings.TWITTER_API_SECRET_KEY,
 820 |  8 |     settings.TWITTER_ACCESS_TOKEN,
 821 |  9 |     settings.TWITTER_ACCESS_TOKEN_SECRET
 822 | 10 | )
 823 | 11 | 
 824 | 12 | api = tweepy.API(auth)
 825 | 13 | 
 826 | 14 | def obter_dados_twitter(usuario_handle):
 827 | 15 |     """Retorna dados básicos do perfil do Twitter."""
 828 | 16 |     try:
 829 | 17 |         usuario = api.get_user(screen_name=usuario_handle)
 830 | 18 |         dados = {
 831 | 19 |             'nome': usuario.name,
 832 | 20 |             'descricao': usuario.description,
 833 | 21 |             'seguindo': usuario.friends_count,
 834 | 22 |             'seguidores': usuario.followers_count,
 835 | 23 |             'tweets': usuario.statuses_count
 836 | 24 |         }
 837 | 25 |         return dados
 838 | 26 |     except tweepy.TweepError as e:
 839 | 27 |         print(f"Erro ao acessar o perfil do Twitter: {e}")
 840 | 28 |         return None
 841 | 29 | 
 842 | 
 843 | 
 844 | --------------------------------------------------------------------------------
 845 | /fans/templates/fans/base.html:
 846 | --------------------------------------------------------------------------------
 847 |  1 | {% load static %}
 848 |  2 | 
 849 |  3 | <!DOCTYPE html>
 850 |  4 | <html lang="pt-br">
 851 |  5 | <head>
 852 |  6 |   <meta charset="UTF-8">
 853 |  7 |   <meta name="viewport" content="width=device-width, initial-scale=1.0">
 854 |  8 |   <title>{% block title %}Know Your Fan{% endblock %}</title>
 855 |  9 |   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
 856 | 10 |   <link rel="icon" href="{% static 'images/favicon.ico' %}" type="image/x-icon">
 857 | 11 |   {% block head %}{% endblock %}
 858 | 12 | </head>
 859 | 13 | <body class="bg-white text-black font-sans">
 860 | 14 | 
 861 | 15 |   {% include 'partials/navbar.html' %}
 862 | 16 | 
 863 | 17 |   <main class="min-h-screen px-4 py-8">
 864 | 18 |     {% block content %}{% endblock %}
 865 | 19 |   </main>
 866 | 20 | 
 867 | 21 |   {% include 'partials/footer.html' %}
 868 | 22 | 
 869 | 23 |   {% block scripts %}{% endblock %}
 870 | 24 | </body>
 871 | 25 | </html>
 872 | 26 | 
 873 | 
 874 | 
 875 | --------------------------------------------------------------------------------
 876 | /fans/templates/fans/cadastro_fan.html:
 877 | --------------------------------------------------------------------------------
 878 |  1 | {% extends 'fans/base.html' %}
 879 |  2 | {% load static %}
 880 |  3 | 
 881 |  4 | {% block title %}Cadastro | Carteirinha Furiosa{% endblock %}
 882 |  5 | 
 883 |  6 | {% block content %}
 884 |  7 | <section class="min-h-screen bg-cover bg-center relative" style="background-image: url('{% static 'images/furia-torcida2.jpg' %}');">
 885 |  8 |   <!-- Overlay escuro para contraste -->
 886 |  9 |   <div class="absolute inset-0 bg-black bg-opacity-60"></div>
 887 | 10 | 
 888 | 11 |   <!-- Conteúdo acima da imagem -->
 889 | 12 |   <div class="relative z-10 flex flex-col justify-center items-center min-h-screen py-12 px-6">
 890 | 13 |     <div class="w-full max-w-2xl rounded-xl shadow-lg p-8 bg-white bg-opacity-95 backdrop-blur-md">
 891 | 14 |       <h2 class="text-3xl font-bold uppercase text-center text-black mb-8">Cadastro do Fã</h2>
 892 | 15 | 
 893 | 16 |       <form method="post" class="space-y-6">
 894 | 17 |         {% csrf_token %}
 895 | 18 |         {% for field in fan_form %}
 896 | 19 |           <div>
 897 | 20 |             <label class="block text-sm font-semibold text-gray-700 mb-1">{{ field.label_tag }}</label>
 898 | 21 |             {{ field }}
 899 | 22 |             {% if field.errors %}
 900 | 23 |               <p class="text-sm text-red-600 mt-1">{{ field.errors }}</p>
 901 | 24 |             {% endif %}
 902 | 25 |           </div>
 903 | 26 |         {% endfor %}
 904 | 27 |         <div class="text-center">
 905 | 28 |           <button type="submit" class="bg-yellow-500 hover:bg-yellow-600 text-black font-bold uppercase px-8 py-3 rounded-lg transition">
 906 | 29 |             Próximo
 907 | 30 |           </button>
 908 | 31 |         </div>
 909 | 32 |       </form>
 910 | 33 |     </div>
 911 | 34 |   </div>
 912 | 35 | </section>
 913 | 36 | {% endblock %}
 914 | 37 | 
 915 | 
 916 | 
 917 | --------------------------------------------------------------------------------
 918 | /fans/templates/fans/cadastro_finalizado.html:
 919 | --------------------------------------------------------------------------------
 920 |  1 | {% load static %}
 921 |  2 | <!DOCTYPE html>
 922 |  3 | <html lang="pt-BR">
 923 |  4 | <head>
 924 |  5 |     <meta charset="UTF-8">
 925 |  6 |     <title>Cadastro Finalizado</title>
 926 |  7 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
 927 |  8 | </head>
 928 |  9 | <body class="bg-light">
 929 | 10 |     <div class="container py-5 text-center">
 930 | 11 |         <h2 class="mb-4">Cadastro concluído com sucesso!</h2>
 931 | 12 |         <p class="lead">Obrigado por se cadastrar! Em breve você receberá atualizações personalizadas.</p>
 932 | 13 |     </div>
 933 | 14 | </body>
 934 | 15 | </html>
 935 | 16 | 
 936 | 
 937 | 
 938 | --------------------------------------------------------------------------------
 939 | /fans/templates/fans/cadastro_redes_sociais.html:
 940 | --------------------------------------------------------------------------------
 941 |  1 | {% load static %}
 942 |  2 | <!DOCTYPE html>
 943 |  3 | <html lang="pt-BR">
 944 |  4 | <head>
 945 |  5 |     <meta charset="UTF-8">
 946 |  6 |     <title>Redes Sociais e Perfis</title>
 947 |  7 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
 948 |  8 | </head>
 949 |  9 | <body class="bg-light">
 950 | 10 |     <div class="container py-5">
 951 | 11 |         <h2 class="mb-4">Redes Sociais e Perfis de Esports</h2>
 952 | 12 |         <form method="post" class="card p-4 shadow-sm">
 953 | 13 |             {% csrf_token %}
 954 | 14 |             <h5>Rede Social</h5>
 955 | 15 |             <div class="mb-3">
 956 | 16 |                 {{ rede_form.as_p }}
 957 | 17 |             </div>
 958 | 18 |             <h5>Perfil de Esports</h5>
 959 | 19 |             <div class="mb-3">
 960 | 20 |                 {{ perfil_form.as_p }}
 961 | 21 |             </div>
 962 | 22 |             <button type="submit" class="btn btn-success">Finalizar Cadastro</button>
 963 | 23 |         </form>
 964 | 24 |     </div>
 965 | 25 | </body>
 966 | 26 | </html>
 967 | 27 | 
 968 | 
 969 | 
 970 | --------------------------------------------------------------------------------
 971 | /fans/templates/fans/home.html:
 972 | --------------------------------------------------------------------------------
 973 |  1 | {% extends 'fans/base.html' %}
 974 |  2 | {% load static %}
 975 |  3 | 
 976 |  4 | {% block title %}Home | Carteirinha Furiosa{% endblock %}
 977 |  5 | 
 978 |  6 | {% block content %}
 979 |  7 | <section class="relative">
 980 |  8 |   <img src="{% static 'images/banner-furia.jpg' %}" alt="Banner FURIA" class="w-full h-full object-cover">
 981 |  9 |   <div class="absolute inset-0 bg-black bg-opacity-60 flex flex-col justify-center items-center text-center text-white px-4">
 982 | 10 |     <h1 class="text-4xl md:text-5xl font-bold tracking-wide uppercase mb-4">Conheça a Carteirinha Furiosa</h1>
 983 | 11 |     <p class="text-lg md:text-xl text-gray-300 max-w-2xl">A plataforma oficial da FURIA para entender e se conectar com você, fã de esports.</p>
 984 | 12 |     <a href="{% url 'cadastro_fan' %}" class="mt-6 inline-block bg-yellow-500 hover:bg-yellow-600 text-black font-bold uppercase px-6 py-3 rounded-lg transition">Começar Agora</a>
 985 | 13 |   </div>
 986 | 14 | </section>
 987 | 15 | 
 988 | 16 | <section class="bg-white text-black py-16 px-6 md:px-16 text-center">
 989 | 17 |   <h2 class="text-3xl md:text-4xl font-bold uppercase mb-8">O que é a Carteirinha Furiosa</h2>
 990 | 18 |   <div class="w-full">
 991 | 19 |     <div class="p-8 border border-gray-200 rounded-xl shadow hover:shadow-lg transition text-left w-full bg-gray-50 max-w-7xl mx-auto">
 992 | 20 |       <h3 class="text-2xl font-semibold uppercase mb-4">Crie seu perfil</h3>
 993 | 21 |       <p class="text-lg leading-relaxed">
 994 | 22 |         Preencha dados básicos, seus interesses no universo FURIA, e nos diga quem são seus jogadores e streamers favoritos. Com base nos seus gostos, nosso sistema enviará pelo WhatsApp informações para que você viva o universo FURIA de onde estiver, a qualquer hora.
 995 | 23 |       </p>
 996 | 24 |     </div>
 997 | 25 |   </div>
 998 | 26 | </section>
 999 | 27 | 
1000 | 28 | <section class="bg-white text-black py-20 px-6 md:px-16">
1001 | 29 |   <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center gap-12">
1002 | 30 |     <!-- Imagem -->
1003 | 31 |     <div class="w-full md:w-1/2">
1004 | 32 |       <img src="{% static 'images/furia-torcida.jpg' %}" alt="Carteirinha Furiosa" class="w-full h-auto rounded-xl shadow-lg">
1005 | 33 |     </div>
1006 | 34 | 
1007 | 35 |     <!-- Texto e botão -->
1008 | 36 |     <div class="w-full md:w-1/2 text-center md:text-left">
1009 | 37 |       <h2 class="text-3xl md:text-4xl font-bold uppercase mb-4">Faça parte da FURIA</h2>
1010 | 38 |       <p class="text-lg text-gray-700 mb-6">
1011 | 39 |         Cadastre-se agora e tenha acesso exclusivo a conteúdos personalizados, novidades do seu time favorito, e benefícios únicos como membro da Carteirinha Furiosa.
1012 | 40 |       </p>
1013 | 41 |       <a href="{% url 'cadastro_fan' %}" class="inline-block bg-yellow-500 hover:bg-yellow-600 text-black font-bold uppercase px-8 py-4 rounded-lg transition">
1014 | 42 |         Inscreva-se Agora
1015 | 43 |       </a>
1016 | 44 |     </div>
1017 | 45 |   </div>
1018 | 46 | </section>
1019 | 47 | 
1020 | 48 | 
1021 | 49 | 
1022 | 50 | {% endblock %}
1023 | 51 | 
1024 | 
1025 | 
1026 | --------------------------------------------------------------------------------
1027 | /fans/templates/fans/instagram_info.html:
1028 | --------------------------------------------------------------------------------
1029 |  1 | <!DOCTYPE html>
1030 |  2 | <html lang="pt-BR">
1031 |  3 | <head>
1032 |  4 |     <meta charset="UTF-8">
1033 |  5 |     <title>Buscar Instagram</title>
1034 |  6 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
1035 |  7 | </head>
1036 |  8 | <body class="container py-5">
1037 |  9 |     <h1 class="mb-4">Buscar Informações do Instagram</h1>
1038 | 10 | 
1039 | 11 |     <form method="post" class="mb-4">
1040 | 12 |         {% csrf_token %}
1041 | 13 |         {{ form.as_p }}
1042 | 14 |         <button type="submit" class="btn btn-primary">Buscar</button>
1043 | 15 |     </form>
1044 | 16 | 
1045 | 17 |     {% if dados_instagram %}
1046 | 18 |         <div class="card">
1047 | 19 |             <div class="card-body">
1048 | 20 |                 <h5 class="card-title">@{{ dados_instagram.username }}</h5>
1049 | 21 |                 <p><strong>Seguidores:</strong> {{ dados_instagram.seguidores }}</p>
1050 | 22 |                 <p><strong>Seguindo:</strong> {{ dados_instagram.seguindo }}</p>
1051 | 23 |                 <p><strong>Bio:</strong> {{ dados_instagram.bio }}</p>
1052 | 24 |                 <a href="{{ dados_instagram.url_perfil }}" class="btn btn-success" target="_blank">Ver Perfil</a>
1053 | 25 |             </div>
1054 | 26 |         </div>
1055 | 27 |     {% endif %}
1056 | 28 | </body>
1057 | 29 | </html>
1058 | 30 | 
1059 | 
1060 | 
1061 | --------------------------------------------------------------------------------
1062 | /fans/templates/fans/perfil_esports_valido.html:
1063 | --------------------------------------------------------------------------------
1064 |  1 | {% load static %}
1065 |  2 | <!DOCTYPE html>
1066 |  3 | <html lang="pt-BR">
1067 |  4 | <head>
1068 |  5 |     <meta charset="UTF-8">
1069 |  6 |     <title>Perfil de Esports Vinculado</title>
1070 |  7 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
1071 |  8 | </head>
1072 |  9 | <body class="bg-light">
1073 | 10 |     <div class="container py-5">
1074 | 11 |         <h2 class="mb-4">Perfil de Esports Vinculado com Sucesso</h2>
1075 | 12 |         <p>O link do seu perfil de esports foi validado e vinculado ao seu cadastro!</p>
1076 | 13 |         <ul class="list-group">
1077 | 14 |             <li class="list-group-item"><strong>Link do Perfil:</strong> {{ fan.perfil_esports_link }}</li>
1078 | 15 |         </ul>
1079 | 16 |         <a href="{% url 'perfil' fan.id %}" class="btn btn-primary mt-4">Voltar ao Perfil</a>
1080 | 17 |     </div>
1081 | 18 | </body>
1082 | 19 | </html>
1083 | 20 | 
1084 | 
1085 | 
1086 | --------------------------------------------------------------------------------
1087 | /fans/templates/fans/twitter_info.html:
1088 | --------------------------------------------------------------------------------
1089 |  1 | <!DOCTYPE html>
1090 |  2 | <html lang="pt-BR">
1091 |  3 | <head>
1092 |  4 |     <meta charset="UTF-8">
1093 |  5 |     <title>Buscar Twitter</title>
1094 |  6 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
1095 |  7 | </head>
1096 |  8 | <body class="container py-5">
1097 |  9 |     <h1 class="mb-4">Buscar Informações do Twitter</h1>
1098 | 10 | 
1099 | 11 |     <form method="post" class="mb-4">
1100 | 12 |         {% csrf_token %}
1101 | 13 |         {{ form.as_p }}
1102 | 14 |         <button type="submit" class="btn btn-primary">Buscar</button>
1103 | 15 |     </form>
1104 | 16 | 
1105 | 17 |     {% if dados_twitter %}
1106 | 18 |         <div class="card">
1107 | 19 |             <div class="card-body">
1108 | 20 |                 <h5 class="card-title">@{{ dados_twitter.username }}</h5>
1109 | 21 |                 <p><strong>Nome:</strong> {{ dados_twitter.nome }}</p>
1110 | 22 |                 <p><strong>Bio:</strong> {{ dados_twitter.bio }}</p>
1111 | 23 |                 <p><strong>Seguidores:</strong> {{ dados_twitter.seguidores }}</p>
1112 | 24 |                 <p><strong>Seguindo:</strong> {{ dados_twitter.seguindo }}</p>
1113 | 25 |                 <a href="{{ dados_twitter.url_perfil }}" class="btn btn-success" target="_blank">Ver Perfil</a>
1114 | 26 |             </div>
1115 | 27 |         </div>
1116 | 28 |     {% endif %}
1117 | 29 | </body>
1118 | 30 | </html>
1119 | 31 | 
1120 | 
1121 | 
1122 | --------------------------------------------------------------------------------
1123 | /fans/templates/fans/vincular_perfil_esports.html:
1124 | --------------------------------------------------------------------------------
1125 |  1 | {% load static %}
1126 |  2 | <!DOCTYPE html>
1127 |  3 | <html lang="pt-BR">
1128 |  4 | <head>
1129 |  5 |     <meta charset="UTF-8">
1130 |  6 |     <title>Vincular Perfil de Esports</title>
1131 |  7 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
1132 |  8 | </head>
1133 |  9 | <body class="bg-light">
1134 | 10 |     <div class="container py-5">
1135 | 11 |         <h2 class="mb-4">Vincular Perfil de Esports</h2>
1136 | 12 |         <form method="post" class="card p-4 shadow-sm">
1137 | 13 |             {% csrf_token %}
1138 | 14 |             {{ form.as_p }}
1139 | 15 |             <button type="submit" class="btn btn-primary">Vincular</button>
1140 | 16 |         </form>
1141 | 17 |     </div>
1142 | 18 | </body>
1143 | 19 | </html>
1144 | 20 | 
1145 | 
1146 | 
1147 | --------------------------------------------------------------------------------
1148 | /fans/templates/fans/vincular_twitter.html:
1149 | --------------------------------------------------------------------------------
1150 |  1 | {% load static %}
1151 |  2 | <!DOCTYPE html>
1152 |  3 | <html lang="pt-BR">
1153 |  4 | <head>
1154 |  5 |     <meta charset="UTF-8">
1155 |  6 |     <title>Vincular Twitter</title>
1156 |  7 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
1157 |  8 | </head>
1158 |  9 | <body class="bg-light">
1159 | 10 |     <div class="container py-5">
1160 | 11 |         <h2 class="mb-4">Vincular Conta do Twitter</h2>
1161 | 12 |         <form method="post" class="card p-4 shadow-sm">
1162 | 13 |             {% csrf_token %}
1163 | 14 |             {{ form.as_p }}
1164 | 15 |             <button type="submit" class="btn btn-primary">Vincular</button>
1165 | 16 |         </form>
1166 | 17 |     </div>
1167 | 18 | </body>
1168 | 19 | </html>
1169 | 20 | 
1170 | 
1171 | 
1172 | --------------------------------------------------------------------------------
1173 | /fans/templates/partials/footer.html:
1174 | --------------------------------------------------------------------------------
1175 |  1 | {% load static %}
1176 |  2 | 
1177 |  3 | <footer class="w-full bg-white text-dark border-t py-12 px-6 md:px-16">
1178 |  4 |   <div class="flex flex-col md:flex-row justify-between gap-12 flex-wrap">
1179 |  5 |     
1180 |  6 |     <!-- Newsletter -->
1181 |  7 |     <div class="md:w-1/4">
1182 |  8 |       <h6 class="text-uppercase font-bold mb-4">SEJA O PRIMEIRO A SABER DAS NOSSAS NOVIDADES:</h6>
1183 |  9 |       <div class="flex">
1184 | 10 |         <input type="email" class="border border-dark px-3 py-2 w-full rounded-l" placeholder="Seu e-mail">
1185 | 11 |         <button class="bg-black text-white px-4 py-2 rounded-r hover:bg-gray-800 transition">
1186 | 12 |           <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
1187 | 13 |             <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
1188 | 14 |           </svg>
1189 | 15 |         </button>
1190 | 16 |       </div>
1191 | 17 |     </div>
1192 | 18 | 
1193 | 19 |     <!-- Informações -->
1194 | 20 |     <div class="md:w-1/4">
1195 | 21 |       <h6 class="text-uppercase font-bold mb-4">INFORMAÇÕES</h6>
1196 | 22 |       <ul class="space-y-2">
1197 | 23 |         <li><a href="https://www.furia.gg/quem-somos" class="text-dark hover:underline">Quem somos</a></li>
1198 | 24 |       </ul>
1199 | 25 |     </div>
1200 | 26 | 
1201 | 27 |     <!-- Políticas -->
1202 | 28 |     <div class="md:w-1/4">
1203 | 29 |       <h6 class="text-uppercase font-bold mb-4">POLÍTICAS</h6>
1204 | 30 |       <ul class="space-y-2">
1205 | 31 |         <li><a href="https://www.furia.gg/politica-privacidade" class="text-dark hover:underline">Política de Privacidade</a></li>
1206 | 32 |         <li><a href="https://www.furia.gg/politica-cookie" class="text-dark hover:underline">Política de Cookie</a></li>
1207 | 33 |       </ul>
1208 | 34 |     </div>
1209 | 35 | 
1210 | 36 |     <!-- Redes Sociais -->
1211 | 37 |     <div class="md:w-1/4">
1212 | 38 |       <h6 class="text-uppercase font-bold mb-4">SIGA FURIA</h6>
1213 | 39 |       <div class="flex gap-4">
1214 | 40 |         <a href="https://www.instagram.com/furiagg/" target="_blank">
1215 | 41 |           <img src="{% static 'images/insta-logo.avif' %}" alt="Instagram" width="24" height="24">
1216 | 42 |         </a>
1217 | 43 |       </div>
1218 | 44 |     </div>
1219 | 45 |   </div>
1220 | 46 | 
1221 | 47 |   <div class="border-t border-gray-300 mt-8 pt-4 text-center text-sm text-gray-500">
1222 | 48 |     © 2024 Furia. All Rights Reserved.
1223 | 49 |   </div>
1224 | 50 | </footer>
1225 | 51 | 
1226 | 
1227 | 
1228 | --------------------------------------------------------------------------------
1229 | /fans/templates/partials/navbar.html:
1230 | --------------------------------------------------------------------------------
1231 |  1 | {% load static %}
1232 |  2 | 
1233 |  3 | <nav class="fixed top-0 w-full z-50 bg-white text-black px-8 py-4 flex items-center justify-between uppercase tracking-wide relative shadow-md">
1234 |  4 | 
1235 |  5 |   <ul class="flex gap-8 text-sm items-center absolute left-8">
1236 |  6 |     <li><a href="https://www.furia.gg/" class="hover:underline">Loja</a></li>
1237 |  7 |     <li><a href="https://www.youtube.com/@FURIAggCS" class="hover:underline">Conteúdo</a></li>
1238 |  8 |     <li><a href="https://www.furia.gg/quem-somos" class="hover:underline">Sobre</a></li>
1239 |  9 |   </ul>
1240 | 10 | 
1241 | 11 |   <a href="/" class="text-2xl font-black mx-auto">
1242 | 12 |     <img src="{% static 'images/logo-furia.svg' %}" alt="FURIA Logo" class="h-10">
1243 | 13 |   </a>
1244 | 14 | 
1245 | 15 |   <div class="flex gap-6 items-center text-xs absolute right-8">
1246 | 16 |     <a href="/cadastro" class="bg-black text-white px-4 py-2 rounded hover:bg-gray-800 transition">Entrar</a>
1247 | 17 |   </div>
1248 | 18 | </nav>
1249 | 19 | 
1250 | 
1251 | 
1252 | --------------------------------------------------------------------------------
1253 | /fans/tests.py:
1254 | --------------------------------------------------------------------------------
1255 | 1 | from django.test import TestCase
1256 | 2 | 
1257 | 3 | # Create your tests here.
1258 | 4 | 
1259 | 
1260 | 
1261 | --------------------------------------------------------------------------------
1262 | /fans/urls.py:
1263 | --------------------------------------------------------------------------------
1264 |  1 | from django.urls import path
1265 |  2 | from . import views
1266 |  3 | 
1267 |  4 | urlpatterns = [
1268 |  5 |     path('cadastro/', views.cadastro_fan, name='cadastro_fan'),
1269 |  6 |     path('cadastro/redes-sociais/<int:fan_id>/', views.cadastro_redes_sociais, name='cadastro_redes_sociais'),
1270 |  7 |     path('cadastro/finalizado/', views.cadastro_finalizado, name='cadastro_finalizado'),
1271 |  8 |     path('vincular_perfil_esports/<int:fan_id>/', views.vincular_perfil_esports, name='vincular_perfil_esports'),
1272 |  9 |     path('instagram/', views.instagram_info_view, name='instagram_info'),
1273 | 10 |     path('twitter/', views.twitter_info_view, name='twitter_info'),
1274 | 11 |     path('', views.home, name='home'),
1275 | 12 | ]
1276 | 13 | 
1277 | 
1278 | 
1279 | --------------------------------------------------------------------------------
1280 | /fans/views.py:
1281 | --------------------------------------------------------------------------------
1282 |  1 | from django.shortcuts import render, redirect
1283 |  2 | from django.http import HttpResponse
1284 |  3 | from .forms import FanForm, RedeSocialForm, PerfilEsportsForm, TwitterForm, EsportsProfileForm, InstagramForm
1285 |  4 | from fans.services.rede_sociais.twitter_service import obter_dados_twitter
1286 |  5 | from fans.services.rede_sociais.instagram_service import buscar_informacoes_instagram
1287 |  6 | from .models import Fan
1288 |  7 | from .services.esports_service import validar_link_esports
1289 |  8 | 
1290 |  9 | def cadastro_fan(request):
1291 | 10 |     if request.method == 'POST':
1292 | 11 |         fan_form = FanForm(request.POST)
1293 | 12 |         
1294 | 13 |         if fan_form.is_valid():
1295 | 14 |             fan = fan_form.save()
1296 | 15 |             return redirect('cadastro_redes_sociais', fan_id=fan.id)  # Passa o fan_id
1297 | 16 |     else:
1298 | 17 |         fan_form = FanForm()
1299 | 18 | 
1300 | 19 |     return render(request, 'fans/cadastro_fan.html', {
1301 | 20 |         'fan_form': fan_form,
1302 | 21 |     })
1303 | 22 | 
1304 | 23 | def cadastro_redes_sociais(request, fan_id):
1305 | 24 |     if request.method == 'POST':
1306 | 25 |         rede_form = RedeSocialForm(request.POST)
1307 | 26 |         perfil_form = PerfilEsportsForm(request.POST)
1308 | 27 | 
1309 | 28 |         if rede_form.is_valid() and perfil_form.is_valid():
1310 | 29 |             rede_social = rede_form.save(commit=False)
1311 | 30 |             rede_social.fan_id = fan_id
1312 | 31 |             rede_social.save()
1313 | 32 | 
1314 | 33 |             perfil = perfil_form.save(commit=False)
1315 | 34 |             perfil.fan_id = fan_id
1316 | 35 |             perfil.save()
1317 | 36 | 
1318 | 37 |             return redirect('cadastro_finalizado')
1319 | 38 | 
1320 | 39 |     else:
1321 | 40 |         rede_form = RedeSocialForm()
1322 | 41 |         perfil_form = PerfilEsportsForm()
1323 | 42 | 
1324 | 43 |     return render(request, 'fans/cadastro_redes_sociais.html', {
1325 | 44 |         'rede_form': rede_form,
1326 | 45 |         'perfil_form': perfil_form,
1327 | 46 |     })
1328 | 47 | 
1329 | 48 | def cadastro_finalizado(request):
1330 | 49 |     return render(request, 'fans/cadastro_finalizado.html')
1331 | 50 | 
1332 | 51 | def vincular_perfil_esports(request, fan_id):
1333 | 52 |     fan = Fan.objects.get(id=fan_id)
1334 | 53 | 
1335 | 54 |     if request.method == 'POST':
1336 | 55 |         form = EsportsProfileForm(request.POST)
1337 | 56 |         if form.is_valid():
1338 | 57 |             link_perfil = form.cleaned_data['link_perfil_esports']
1339 | 58 | 
1340 | 59 |             if link_perfil and validar_link_esports(link_perfil):
1341 | 60 |                 # Armazenar o link do perfil de esports no banco de dados
1342 | 61 |                 fan.perfil_esports_link = link_perfil
1343 | 62 |                 fan.save()
1344 | 63 | 
1345 | 64 |                 return render(request, 'fans/perfil_esports_valido.html', {'fan': fan})
1346 | 65 |             else:
1347 | 66 |                 return HttpResponse("Link de perfil de esports inválido ou não pertence a plataformas válidas.", status=400)
1348 | 67 |     else:
1349 | 68 |         form = EsportsProfileForm()
1350 | 69 | 
1351 | 70 |     return render(request, 'fans/vincular_perfil_esports.html', {'form': form, 'fan': fan})
1352 | 71 | 
1353 | 72 | def instagram_info_view(request):
1354 | 73 |     dados_instagram = None
1355 | 74 | 
1356 | 75 |     if request.method == 'POST':
1357 | 76 |         form = InstagramForm(request.POST)
1358 | 77 |         if form.is_valid():
1359 | 78 |             username = form.cleaned_data['username']
1360 | 79 |             dados_instagram = buscar_informacoes_instagram(username)
1361 | 80 |     else:
1362 | 81 |         form = InstagramForm()
1363 | 82 | 
1364 | 83 |     return render(request, 'fans/instagram_info.html', {'form': form, 'dados_instagram': dados_instagram})
1365 | 84 | 
1366 | 85 | def twitter_info_view(request):
1367 | 86 |     dados_twitter = None
1368 | 87 | 
1369 | 88 |     if request.method == 'POST':
1370 | 89 |         form = TwitterForm(request.POST)
1371 | 90 |         if form.is_valid():
1372 | 91 |             username = form.cleaned_data['username']
1373 | 92 |             dados_twitter = obter_dados_twitter(username)
1374 | 93 |     else:
1375 | 94 |         form = TwitterForm()
1376 | 95 | 
1377 | 96 |     return render(request, 'fans/twitter_info.html', {'form': form, 'dados_twitter': dados_twitter})
1378 | 97 | 
1379 | 98 | def home(request):
1380 | 99 |     return render(request, 'fans/home.html')
1381 | 
1382 | 
1383 | --------------------------------------------------------------------------------
1384 | /manage.py:
1385 | --------------------------------------------------------------------------------
1386 |  1 | #!/usr/bin/env python
1387 |  2 | """Django's command-line utility for administrative tasks."""
1388 |  3 | import os
1389 |  4 | import sys
1390 |  5 | 
1391 |  6 | 
1392 |  7 | def main():
1393 |  8 |     """Run administrative tasks."""
1394 |  9 |     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
1395 | 10 |     try:
1396 | 11 |         from django.core.management import execute_from_command_line
1397 | 12 |     except ImportError as exc:
1398 | 13 |         raise ImportError(
1399 | 14 |             "Couldn't import Django. Are you sure it's installed and "
1400 | 15 |             "available on your PYTHONPATH environment variable? Did you "
1401 | 16 |             "forget to activate a virtual environment?"
1402 | 17 |         ) from exc
1403 | 18 |     execute_from_command_line(sys.argv)
1404 | 19 | 
1405 | 20 | 
1406 | 21 | if __name__ == '__main__':
1407 | 22 |     main()
1408 | 23 | 
1409 | 
1410 | 
1411 | --------------------------------------------------------------------------------
1412 | /readme.md:
1413 | --------------------------------------------------------------------------------
1414 |  1 | # Know Your Fan
1415 |  2 | 
1416 |  3 | Projeto desenvolvido para o teste técnico da FURIA.
1417 |  4 | 
1418 |  5 | ## Descrição
1419 |  6 | 
1420 |  7 | O "Know Your Fan" é uma solução web para coleta, validação e análise de dados de fãs de esports.  
1421 |  8 | O sistema permite:
1422 |  9 | - Cadastro de informações pessoais e preferências.
1423 | 10 | - Upload de documentos e validação via OCR e OpenCV.
1424 | 11 | - Vinculação de redes sociais e plataformas de esports.
1425 | 12 | - Envio de conteúdo personalizado via WhatsApp.
1426 | 13 | 
1427 | 14 | ## Tecnologias Utilizadas
1428 | 15 | 
1429 | 16 | - **Backend:** Django
1430 | 17 | - **Frontend:** HTML5, CSS3 (Bootstrap 5), JavaScript (ES6+)
1431 | 18 | - **Banco de Dados:** SQLite3
1432 | 19 | - **OCR e Análise de Imagens:** Pytesseract, OpenCV
1433 | 20 | - **Integrações de APIs:** Twitter, Instagram, Twitch, YouTube
1434 | 21 | - **Agendamento de Tarefas:** Schedule
1435 | 22 | - **Envio de Mensagens:** Integração com API do WhatsApp Business (simulada ou real)
1436 | 23 | 
1437 | 24 | ## Instalação e Execução
1438 | 25 | 
1439 | 26 | 1. Clone o repositório:
1440 | 27 |     ```bash
1441 | 28 |     git clone https://github.com/SEU_USUARIO/Know-Your-Fan.git
1442 | 29 |     cd Know-Your-Fan
1443 | 30 |     ```
1444 | 31 | 
1445 | 32 | 2. Crie e ative o ambiente virtual:
1446 | 33 |     ```bash
1447 | 34 |     # Windows
1448 | 35 |     python -m venv venv
1449 | 36 |     .\venv\Scripts\activate
1450 | 37 | 
1451 | 38 |     # Mac/Linux
1452 | 39 |     python3 -m venv venv
1453 | 40 |     source venv/bin/activate
1454 | 41 |     ```
1455 | 42 | 
1456 | 43 | 3. Instale as dependências:
1457 | 44 |     ```bash
1458 | 45 |     pip install -r requirements.txt
1459 | 46 |     ```
1460 | 47 | 
1461 | 48 | 4. Execute as migrações do Django (após a criação do projeto Django):
1462 | 49 |     ```bash
1463 | 50 |     python manage.py migrate
1464 | 51 |     ```
1465 | 52 | 
1466 | 53 | 5. Inicie o servidor de desenvolvimento:
1467 | 54 |     ```bash
1468 | 55 |     python manage.py runserver
1469 | 56 |     ```
1470 | 57 | 
1471 | 58 | ## Autor
1472 | 59 | 
1473 | 60 | Desenvolvido por Rafael Mandel.
1474 | 61 | 
1475 | 
1476 | 
1477 | --------------------------------------------------------------------------------
1478 | /requirements.txt:
1479 | --------------------------------------------------------------------------------
1480 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/requirements.txt
1481 | 
1482 | 
1483 | --------------------------------------------------------------------------------
1484 | /scheduler.py:
1485 | --------------------------------------------------------------------------------
1486 | 1 | import time
1487 | 2 | from fans.services.notificacao_service import rodar_agendamentos
1488 | 3 | 
1489 | 4 | if __name__ == "__main__":
1490 | 5 |     # Inicia o agendamento em background
1491 | 6 |     rodar_agendamentos()
1492 | 7 | 
1493 | 
1494 | 
1495 | --------------------------------------------------------------------------------
1496 | /static/images/banner-furia.jpg:
1497 | --------------------------------------------------------------------------------
1498 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/static/images/banner-furia.jpg
1499 | 
1500 | 
1501 | --------------------------------------------------------------------------------
1502 | /static/images/furia-logo.png:
1503 | --------------------------------------------------------------------------------
1504 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/static/images/furia-logo.png
1505 | 
1506 | 
1507 | --------------------------------------------------------------------------------
1508 | /static/images/furia-torcida.jpg:
1509 | --------------------------------------------------------------------------------
1510 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/static/images/furia-torcida.jpg
1511 | 
1512 | 
1513 | --------------------------------------------------------------------------------
1514 | /static/images/furia-torcida2.jpg:
1515 | --------------------------------------------------------------------------------
1516 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/static/images/furia-torcida2.jpg
1517 | 
1518 | 
1519 | --------------------------------------------------------------------------------
1520 | /static/images/insta-logo.avif:
1521 | --------------------------------------------------------------------------------
1522 | https://raw.githubusercontent.com/rflMandell/Know-Your-Fan/codding/static/images/insta-logo.avif
1523 | 
1524 | 
1525 | --------------------------------------------------------------------------------
1526 | /static/images/logo-furia.svg:
1527 | --------------------------------------------------------------------------------
1528 | 1 | <svg width="90" height="32" viewBox="0 0 90 32" fill="none" xmlns="http://www.w3.org/2000/svg">
1529 | 2 | <path fill-rule="evenodd" clip-rule="evenodd" d="M53.8249 6.78989C53.7668 7.50049 53.6459 8.20517 53.5465 8.91208C53.3582 10.2526 53.179 11.5946 52.9702 12.9322C52.8319 13.8189 52.5263 14.0802 51.6546 14.1054C51.0396 14.1224 50.4238 14.1091 49.8084 14.1047C49.7386 14.1039 49.669 14.0713 49.5054 14.0292C49.8178 11.3289 50.2467 8.64338 50.6222 5.85279C51.4768 5.85279 52.2612 5.82317 53.0421 5.86241C53.6386 5.89201 53.8751 6.17626 53.8249 6.78989ZM61.0934 4.03705C60.9707 2.09399 60.1129 1.0155 58.2263 0.484033C57.0311 0.147236 55.8031 0.0569315 54.5689 0.0554511C48.6789 0.0473087 42.789 0.0465707 36.8988 0.0465707C36.7119 0.0465707 36.525 0.0880225 36.3114 0.11319C35.8071 3.52852 34.964 6.8158 33.825 10.0246C32.6803 13.2497 31.301 16.3675 29.5629 19.3165C29.5086 19.3024 29.4543 19.2876 29.4 19.2736C30.2909 12.8885 31.1819 6.50343 32.0785 0.0769165C31.7631 0.0628524 31.5445 0.0443486 31.3257 0.0450888C21.4689 0.0532312 11.612 0.0628532 1.75499 0.0739563C1.73902 0.0739563 1.72024 0.101345 1.70796 0.11911C1.69428 0.139836 1.68652 0.163521 1.66152 0.217557C1.8211 0.385584 1.98638 0.565458 2.15861 0.737927C2.87177 1.45445 3.57451 2.18208 4.30779 2.87788C4.58962 3.14509 4.71126 3.41083 4.61446 3.78834C4.57202 3.9534 4.57919 4.13105 4.55501 4.30204C4.13283 7.27843 3.70548 10.2533 3.28693 13.2305C2.54588 18.5008 1.8089 23.7711 1.07355 29.0421C0.976013 29.7416 0.898737 30.4433 0.806152 31.1917C3.18643 31.1917 5.49098 31.1917 7.87163 31.1917C8.43734 27.1516 8.99957 23.1375 9.57202 19.05C11.8227 19.05 14.0039 19.05 16.2367 19.05C16.5198 17.0078 16.7923 15.0425 17.0792 12.9729C14.8188 12.9729 12.6631 12.9729 10.4184 12.9729C10.7491 10.636 11.0653 8.40281 11.3788 6.18662C12.5042 6.03636 20.0601 6.08743 20.5866 6.24732C20.5717 6.48566 20.5569 6.73067 20.5412 6.97642C20.434 8.64856 20.2892 10.32 20.2268 11.9936C20.0767 16.0285 20.3917 20.0256 21.3233 23.9613C21.9045 26.4166 22.7174 28.7897 23.9922 30.9829C24.187 31.3175 24.4197 31.6306 24.6659 32C25.0127 31.8024 25.314 31.6439 25.6017 31.4648C27.5542 30.2442 29.3326 28.803 30.9697 27.1871C36.9424 21.2936 40.5354 14.1239 42.2861 5.97418C42.5326 4.82685 42.7206 3.66694 42.9443 2.46632C43.5729 2.84901 43.9557 3.27537 43.7448 4.04149C43.6344 4.44268 43.6075 4.86682 43.5495 5.28208C43.1333 8.25847 42.7196 11.2363 42.3033 14.2135C41.9313 16.873 41.5569 19.5326 41.1837 22.1922C40.7762 25.096 40.3681 27.9992 39.9652 30.9037C39.9533 30.9896 39.9964 31.0829 40.0191 31.1998C42.3572 31.1998 44.6658 31.1998 47.0594 31.1998C47.6102 27.3396 48.1583 23.4987 48.7145 19.6007C49.3889 19.6007 50.0006 19.5918 50.612 19.6029C51.3052 19.6163 51.6714 19.9205 51.7553 20.5993C51.8001 20.9627 51.7965 21.3424 51.7475 21.7051C51.4412 23.9761 51.1144 26.2441 50.7974 28.5136C50.6754 29.3863 50.5614 30.2605 50.4366 31.1872C52.8354 31.1872 55.1624 31.1872 57.5361 31.1872C57.5846 30.9193 57.6351 30.6817 57.6696 30.4426C57.9996 28.1501 58.3503 25.8599 58.6454 23.5631C58.8084 22.2943 58.9622 21.0145 58.9667 19.7384C58.9727 18.0233 58.2458 17.1736 56.6076 16.6917C56.4909 16.6569 56.371 16.634 56.2527 16.6058C56.2411 16.5747 56.2296 16.5429 56.2181 16.5118C56.4066 16.463 56.5928 16.4001 56.7842 16.3682C58.3235 16.1121 59.2972 15.2076 59.789 13.7501C59.8836 13.471 59.9946 13.1912 60.0441 12.9026C60.2904 11.471 60.5403 10.0394 60.7466 8.60193C60.964 7.08968 61.1903 5.57595 61.0934 4.03705Z" fill="black"/>
1530 | 3 | <path fill-rule="evenodd" clip-rule="evenodd" d="M82.518 19.6681C81.3237 19.6681 80.1812 19.6681 78.9544 19.6681C80.1509 15.1698 81.3371 10.7078 82.5232 6.24583C82.5927 6.24805 82.6622 6.24953 82.7317 6.25101C82.6607 10.7056 82.5898 15.1595 82.518 19.6681ZM74.3696 0.196825C75.1009 0.929634 75.7864 1.66836 76.5318 2.3427C76.9755 2.74389 77.0502 3.11326 76.8853 3.68914C74.377 12.4754 71.893 21.2699 69.4053 30.0629C69.307 30.4108 69.2286 30.7653 69.1251 31.1806C71.5173 31.1806 73.8423 31.1806 76.222 31.1806C76.6857 29.4411 77.1471 27.7141 77.6011 26.0109C79.1496 26.0109 80.6175 26.0109 82.1194 26.0109C82.1194 27.7482 82.1194 29.4403 82.1194 31.1821C84.4503 31.1821 86.7553 31.1821 89.1128 31.1821C89.3029 29.367 89.1276 0.683142 88.9302 0.0843114C87.1029 -0.0726133 74.9419 0.00362985 74.3696 0.196825Z" fill="black"/>
1531 | 4 | <path fill-rule="evenodd" clip-rule="evenodd" d="M60.9396 0.0909788C61.1519 0.330807 61.285 0.495873 61.4336 0.645396C62.145 1.36266 62.8446 2.09399 63.5818 2.78386C63.942 3.1214 64.0529 3.44783 63.9701 3.94748C63.7157 5.47749 63.5249 7.01787 63.3119 8.55455C62.8483 11.8966 62.389 15.2394 61.9217 18.5807C61.4026 22.2877 60.876 25.9939 60.3554 29.7009C60.2874 30.182 60.2386 30.6654 60.1758 31.1931C62.5577 31.1931 64.8634 31.1931 67.2416 31.1931C68.6977 20.7806 70.1419 10.4539 71.5913 0.0909788C68.0084 0.0909788 64.5299 0.0909788 60.9396 0.0909788Z" fill="black"/>
1532 | 5 | </svg>
1533 | 6 | 
1534 | 
1535 | 
1536 | --------------------------------------------------------------------------------


--------------------------------------------------------------------------------