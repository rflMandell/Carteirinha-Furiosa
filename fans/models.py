from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fan(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    endereco = models.TextField()
    email = models.EmailField()
    numero_whatsapp = models.CharField(max_length=20)

    # campos para redes sociais
    twitter_username = models.CharField(max_length=100, blank=True, null=True)
    twitch_username = models.CharField(max_length=100, blank=True, null=True)
    instagram_username = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome
    
class PreferenceTopic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveBigIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order', 'name']

class PreferenceOption(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='preferences/')
    topic = models.ForeignKey(PreferenceTopic, related_name='options', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.topic.name} - {self.name}"
    
    class Meta:
        ordering = ['topic', 'order', 'name']
        
class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='preferences')
    option = models.ForeignKey(PreferenceOption, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'option')
        
    def __str__(self):
        return f"{self.user.username} - {self.option.name}"
    
class RedeSocial(models.Model):
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE, related_name='redes_sociais')
    plataforma = models.CharField(max_length=50)  # Ex: Twitter, Instagram, Twitch  YouTube e por ai vai
    usuario = models.CharField(max_length=255)
    url = models.URLField()
    dados_extraidos = models.JSONField(null=True, blank=True)  # Dados públicos coletados

class PerfilEsports(models.Model):
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE, related_name='perfis_esports')
    site = models.CharField(max_length=100)  # Ex: HLTV, Liquipedia, VLR?
    url = models.URLField()
    verificado = models.BooleanField(default=False)