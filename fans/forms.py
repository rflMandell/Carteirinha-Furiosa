from django import forms
from .models import *

class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = [
            'profile_picture', 'nome_completo', 'cpf', 'endereco', 'email', 'numero_whatsapp',
        ]

    def __init__(self, *args, **kwargs):
        super(FanForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 bg-gray-100 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-500'
            })
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({'rows': 3})
    
class EsportsProfileForm(forms.Form):
    link_perfil_esports = forms.URLField(label="Link do Perfil de Esports", required=False, max_length=500)
    
class InstagramForm(forms.Form):
    instagram_username = forms.CharField(label='Seu @ do Instagram', max_length=100)

class TwitterForm(forms.Form):
    twitter_username = forms.CharField(label='Seu @ do Twitter', max_length=100)
    
class DocumentoValidacaoForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = ['documento_validacao']