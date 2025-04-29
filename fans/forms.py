from django import forms
from .models import Fan, RedeSocial, PerfilEsports

class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = [
            'nome', 'cpf', 'endereco', 'email', 'numero_whatsapp',
            'twitter_username', 'twitch_username', 'instagram_username'
        ]

    def __init__(self, *args, **kwargs):
        super(FanForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 bg-gray-100 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500'
            })
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({'rows': 3})


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