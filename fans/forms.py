from django import forms
from .models import Fan, DocumentoIdentidade, RedeSocial, PerfilEsports

class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = [
            'nome', 'cpf', 'endereco', 'email', 'numero_whatsapp',
            'twitter_username', 'twitch_username', 'instagram_username', 'youtube_channel_id'
        ]


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
    
class EsportsProfileForm(forms.Form):
    link_perfil_esports = forms.URLField(label="Link do Perfil de Esports", required=False, max_length=500)
    
class InstagramForm(forms.Form):
    username = forms.CharField(label='Usuário do Instagram', max_length=150)

class TwitterForm(forms.Form):
    username = forms.CharField(label='Usuário do Twitter (X)', max_length=150)