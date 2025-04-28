from django.shortcuts import render, redirect
from .forms import FanForm, DocumentoIdentidadeForm, RedeSocialForm, PerfilEsportsForm
from fans.services.ocr_service import extrair_texto_documento

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
