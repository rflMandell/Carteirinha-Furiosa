from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.conf import settings
from .forms import *
from .models import *
from fans.services.rede_sociais.twitter_service import obter_dados_twitter
from fans.services.rede_sociais.instagram_service import buscar_informacoes_instagram
from .services.esports_service import validar_link_esports
import openai
import re


def cadastro_fan(request):
    if request.method == 'POST':
        fan_form = FanForm(request.POST, request.FILES)
        password = request.POST.get('password')
        email = fan_form.data.get('email')  # ou fan_form.cleaned_data['email'] após is_valid()

        if fan_form.is_valid() and password and email:
            # Cria o User com username=email
            user = User.objects.create_user(username=email, email=email, password=password)
            # Cria o Fan associado ao User
            fan = fan_form.save(commit=False)
            fan.user = user
            fan.save()
            # Faz login automático
            login(request, user)
            return redirect('preferences', fan_id=fan.id)
    else:
        fan_form = FanForm()

    return render(request, 'fans/cadastro_fan.html', {
        'fan_form': fan_form,
    })
    
def login_email(request):
    # Se já está logado, redireciona para o perfil do fã
    if request.user.is_authenticated:
        try:
            fan = Fan.objects.get(user=request.user)
            return redirect('profile', fan_id=fan.id)
        except Fan.DoesNotExist:
            return redirect('home')

    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                fan = Fan.objects.get(user=user)
                return redirect('profile', fan_id=fan.id)
            except Fan.DoesNotExist:
                return redirect('home')
        else:
            error = 'E-mail ou senha inválidos.'
    return render(request, 'fans/login.html', {'error': error})

@login_required
def select_preferences(request, fan_id):
    topics = PreferenceTopic.objects.prefetch_related('options').all()
    if request.method == 'POST':
        UserPreference.objects.filter(user=request.user).delete()
        selected_ids = request.POST.getlist('selected_options')
        for option_id in selected_ids:
            UserPreference.objects.create(
                user=request.user,
                option_id=option_id
            )
        return redirect('profile', fan_id=fan_id)  # Redireciona para o perfil correto
    current_preferences = UserPreference.objects.filter(
        user=request.user
    ).values_list('option_id', flat=True)
    context = {
        'topics': topics,
        'current_preferences': list(current_preferences),
        'fan_id': fan_id,
    }
    return render(request, 'fans/preferences.html', context)

def cadastro_finalizado(request):
    return render(request, 'fans/cadastro_finalizado.html')

#em breve vai de delete no betinha
def vincular_perfil_esports(request, fan_id):
    fan = Fan.objects.get(id=fan_id)

    if request.method == 'POST':
        form = EsportsProfileForm(request.POST)
        if form.is_valid():
            link_perfil = form.cleaned_data['link_perfil_esports']

            if link_perfil and validar_link_esports(link_perfil):
                # Armazenar o link do perfil de esports no banco de dados
                fan.perfil_esports_link = link_perfil
                fan.save()

                return render(request, 'fans/perfil_esports_valido.html', {'fan': fan})
            else:
                return HttpResponse("Link de perfil de esports inválido ou não pertence a plataformas válidas.", status=400)
    else:
        form = EsportsProfileForm()

    return render(request, 'fans/vincular_perfil_esports.html', {'form': form, 'fan': fan})

@login_required
def instagram_info_view(request):
    dados_instagram = None
    fan = Fan.objects.get(user=request.user)

    if request.method == 'POST':
        form = InstagramForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['instagram_username']
            dados_instagram = buscar_informacoes_instagram(username)
            fan.instagram_username = username
            fan.save()
            return redirect('profile', fan_id=fan.id)
    else:
        form = InstagramForm(initial={'instagram_username': fan.instagram_username})

    return render(request, 'fans/instagram_info.html', {
        'form': form,
        'dados_instagram': dados_instagram,
        'fan': fan
    })

@login_required
def twitter_info_view(request):
    fan = Fan.objects.get(user=request.user)
    dados_twitter = None

    if request.method == 'POST':
        form = TwitterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['twitter_username']
        # dados_twitter = buscar_informacoes_twitter(username)
            fan.twitter_username = username
            fan.save()
            return redirect('profile', fan_id=fan.id)
    else:
        form = TwitterForm(initial={'twitter_username': fan.twitter_username})

    return render(request, 'fans/twitter_info.html', {
    'form': form,
    'dados_twitter': dados_twitter,
    'fan': fan
})

def home(request):
    return render(request, 'fans/home.html')

@login_required
def profile_view(request, fan_id):
    fan = Fan.objects.get(id=fan_id)
    if fan.user != request.user:
        return HttpResponseForbidden("Você não pode acessar o perfil de outro usuário.")

    if request.method == 'POST':
        form = FanForm(request.POST, request.FILES, instance=fan)
        if form.is_valid():
            form.save()
            return redirect('profile', fan_id=fan_id)
    else:
        form = FanForm(instance=fan)

    preferences = UserPreference.objects.filter(user=fan.user).select_related(
        'option', 'option__topic'
    ).order_by('option__topic__order', 'option__order')

    return render(request, 'fans/profile.html', {
        'preferences': preferences,
        'fan': fan,
        'form': form,
    })
    
@login_required
def validar_perfil(request):
    fan = Fan.objects.get(user=request.user)
    resultado = None

    if request.method == 'POST':
        form = DocumentoValidacaoForm(request.POST, request.FILES, instance=fan)
        if form.is_valid():
            form.save()
            # Leitura do documento (PDF ou TXT)
            doc_file = fan.documento_validacao
            doc_text = ""
            if doc_file.name.endswith('.pdf'):
                import PyPDF2
                reader = PyPDF2.PdfReader(doc_file)
                doc_text = ""
                for i, page in enumerate(reader.pages):
                    if i >= 5:  # lê até 5 páginas, ajuste se quiser
                        break
                    doc_text += page.extract_text() or ""
            else:
                doc_text = doc_file.read().decode('utf-8', errors='ignore')

            # Filtra só as linhas importantes (nome ou CPF)
            linhas = doc_text.splitlines()
            linhas_importantes = []
            regex_cpf = re.compile(r'\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b')
            for linha in linhas:
                linha_lower = linha.lower()
                if fan.nome_completo.lower() in linha_lower or regex_cpf.search(linha):
                    linhas_importantes.append(linha.strip())
            # Se não encontrar nada, envia as 10 primeiras linhas como fallback
            if not linhas_importantes:
                linhas_importantes = linhas[:10]
            doc_text_filtrado = "\n".join(linhas_importantes)
            # Limita o texto para garantir que não exceda o limite de tokens
            doc_text_filtrado = doc_text_filtrado[:8000]

            # Chamada à OpenAI (GPT-4o)
            prompt = (
                f"Analise as linhas abaixo e diga se o nome '{fan.nome_completo}' e o CPF '{fan.cpf}' "
                "estão presentes e corretos. Responda apenas 'VALIDADO' se sim, ou 'NÃO VALIDADO' se não, "
                "e explique o motivo se não for validado.\n\n"
                f"Linhas extraídas do documento:\n{doc_text_filtrado}"
            )
            client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100
            )
            resultado = response.choices[0].message.content.strip()
            if resultado.startswith("VALIDADO"):
                fan.validado = True
                fan.motivo_validacao = ""
                fan.save()
                messages.success(request, "Perfil validado com sucesso!")
            else:
                fan.validado = False
                fan.motivo_validacao = resultado
                fan.save()
                messages.error(request, f"Validação falhou: {resultado}")
            return redirect('profile', fan_id=fan.id)
    else:
        form = DocumentoValidacaoForm(instance=fan)

    return render(request, 'fans/validar_perfil.html', {
        'form': form,
        'fan': fan,
        'resultado': resultado,
    })