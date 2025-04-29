import tweepy
from django.conf import settings

# Configuração do Twitter
auth = tweepy.OAuth1UserHandler(
    settings.TWITTER_API_KEY,
    settings.TWITTER_API_SECRET_KEY,
    settings.TWITTER_ACCESS_TOKEN,
    settings.TWITTER_ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)

def obter_dados_twitter(usuario_handle):
    """Retorna dados básicos do perfil do Twitter."""
    try:
        usuario = api.get_user(screen_name=usuario_handle)
        dados = {
            'nome': usuario.name,
            'descricao': usuario.description,
            'seguindo': usuario.friends_count,
            'seguidores': usuario.followers_count,
            'tweets': usuario.statuses_count
        }
        return dados
    except tweepy.TweepError as e:
        print(f"Erro ao acessar o perfil do Twitter: {e}")
        return None
