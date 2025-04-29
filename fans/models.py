from django.db import models

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
    

class RedeSocial(models.Model):
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE, related_name='redes_sociais')
    plataforma = models.CharField(max_length=50)  # Ex: Twitter, Instagram, Twitch  YouTube e por ai vai
    usuario = models.CharField(max_length=255)
    url = models.URLField()
    dados_extraidos = models.JSONField(null=True, blank=True)  # Dados públicos coletados

    def __str__(self):
        return f"{self.plataforma} - {self.usuario}"


class PerfilEsports(models.Model):
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE, related_name='perfis_esports')
    site = models.CharField(max_length=100)  # Ex: HLTV, Liquipedia, VLR?
    url = models.URLField()
    verificado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.site} de {self.fan.nome}"
