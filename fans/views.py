from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from fans.services.rede_sociais.twitter_service import obter_dados_twitter
from fans.services.rede_sociais.instagram_service import buscar_informacoes_instagram
from .services.esports_service import validar_link_esports

def cadastro_fan(request):
    if request.method == 'POST':
        fan_form = FanForm(request.POST)
        
        if fan_form.is_valid():
            fan = fan_form.save()
            return redirect('preferences', fan_id=fan.id)
    else:
        fan_form = FanForm()

    return render(request, 'fans/cadastro_fan.html', {
        'fan_form': fan_form,
    })

def select_preferences(request):
    topics = PreferenceTopic.objects.prefetch_related('options').all()
    
    if request.method == 'POST':
        #vai limpar as preferencias anteriores
        UserPreference.objects.filter(user=request.user).delete()
        
        #vai add novas preferencias
        selected_ids = request.POST.getlist('selected_options')
        for option_id in selected_ids:
            UserPreference.objects.create(
                user=request.user,
                option_id=option_id
            )
        return redirect('profile')

    #obtem as preferencias atuais do user (se ja existirem)
    current_preferences = UserPreference.objects.filter(
        user=request.user
    ).values_list('option_id', flat=True)
    
    context = {
        'topics': topics,
        'current_preferences': list(current_preferences)
    }
    return render(request, 'preferences.html', context)

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

def instagram_info_view(request):
    dados_instagram = None

    if request.method == 'POST':
        form = InstagramForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            dados_instagram = buscar_informacoes_instagram(username)
    else:
        form = InstagramForm()

    return render(request, 'fans/instagram_info.html', {'form': form, 'dados_instagram': dados_instagram})

def twitter_info_view(request):
    dados_twitter = None

    if request.method == 'POST':
        form = TwitterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            dados_twitter = obter_dados_twitter(username)
    else:
        form = TwitterForm()

    return render(request, 'fans/twitter_info.html', {'form': form, 'dados_twitter': dados_twitter})

def home(request):
    return render(request, 'fans/home.html')

def profile_view(request):
    user = request.user
    #preferencias ordenada por topico
    preferences = UserPreference.objects.filter(user=user).select_related(
        'option', 'option__topic'
    ).order_by('option__topic__order', 'option__order')
    
    return render(request, 'profile.html', {
        'user': user,
        'preferences': preferences
    })