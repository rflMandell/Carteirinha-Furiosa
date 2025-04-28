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

class TwitterForm(forms.Form):
    twitter_handle = forms.CharField(max_length=255, label="Handle do Twitter", required=True)
    
class EsportsProfileForm(forms.Form):
    link_perfil_esports = forms.URLField(label="Link do Perfil de Esports", required=False, max_length=500)