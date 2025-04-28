from django import forms
from .models import Fan, DocumentoIdentidade, RedeSocial, PerfilEsports

class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = ['nome', 'endereco', 'cpf', 'telefone', 'jogos_favoritos', 'streamers_favoritos']


class DocumentoIdentidadeForm(forms.ModelForm):
    class Meta:
        model = DocumentoIdentidade
        fields = ['documento']


class RedeSocialForm(forms.ModelForm):
    class Meta:
        model = RedeSocial
        fields = ['plataforma', 'usuario', 'url']


class PerfilEsportsForm(forms.ModelForm):
    class Meta:
        model = PerfilEsports
        fields = ['site', 'url']
