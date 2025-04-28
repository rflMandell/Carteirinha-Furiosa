from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FanForm, DocumentoIdentidadeForm, RedeSocialForm, PerfilEsportsForm, TwitterForm, EsportsProfileForm
from fans.services.ocr_service import extrair_texto_documento
from fans.services.twitter_service import obter_dados_twitter
from .models import Fan
from .services.esports_service import validar_link_esports

def cadastro_fan(request):
    if request.method == 'POST':
        fan_form = FanForm(request.POST)
        documento_form = DocumentoIdentidadeForm(request.POST, request.FILES)
        
        if fan_form.is_valid() and documento_form.is_valid():
            fan = fan_form.save()

            documento = documento_form.save(commit=False)
            documento.fan = fan
            documento.save()

            # Validação OCR
            texto_extraido = extrair_texto_documento(documento.documento.path)

            # Aqui podemos fazer verificações básicas:
            nome = fan.nome.lower()
            cpf = fan.cpf.replace(".", "").replace("-", "")

            if nome not in texto_extraido.lower() or cpf not in texto_extraido:
                fan.delete()  # Deleta cadastro inválido
                documento.delete()
                return HttpResponse("Falha na validação do documento. Por favor, envie um documento legível.", status=400)

            return redirect('cadastro_redes_sociais')
    else:
        fan_form = FanForm()
        documento_form = DocumentoIdentidadeForm()

    return render(request, 'fans/cadastro_fan.html', {
        'fan_form': fan_form,
        'documento_form': documento_form,
    })


def cadastro_redes_sociais(request, fan_id):
    if request.method == 'POST':
        rede_form = RedeSocialForm(request.POST)
        perfil_form = PerfilEsportsForm(request.POST)

        if rede_form.is_valid() and perfil_form.is_valid():
            rede_social = rede_form.save(commit=False)
            rede_social.fan_id = fan_id
            rede_social.save()

            perfil = perfil_form.save(commit=False)
            perfil.fan_id = fan_id
            perfil.save()

            return redirect('cadastro_finalizado')

    else:
        rede_form = RedeSocialForm()
        perfil_form = PerfilEsportsForm()

    return render(request, 'fans/cadastro_redes_sociais.html', {
        'rede_form': rede_form,
        'perfil_form': perfil_form,
    })


def cadastro_finalizado(request):
    return render(request, 'fans/cadastro_finalizado.html')

def vincular_twitter(request, fan_id):
    fan = Fan.objects.get(id=fan_id)

    if request.method == 'POST':
        form = TwitterForm(request.POST)
        if form.is_valid():
            twitter_handle = form.cleaned_data['twitter_handle']
            dados_twitter = obter_dados_twitter(twitter_handle)

            if dados_twitter:
                # Armazenar dados do Twitter no banco de dados (se necessário)
                fan.twitter_handle = twitter_handle
                fan.save()

                # Exibir dados do Twitter para o usuário
                return render(request, 'fans/dados_twitter.html', {'dados_twitter': dados_twitter, 'fan': fan})
            else:
                return HttpResponse("Falha ao acessar o perfil do Twitter. Tente novamente.", status=400)
    else:
        form = TwitterForm()

    return render(request, 'fans/vincular_twitter.html', {'form': form, 'fan': fan})

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