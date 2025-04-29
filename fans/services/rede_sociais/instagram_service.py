import instaloader

def buscar_informacoes_instagram(username):
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        dados = {
            'username': profile.username,
            'seguidores': profile.followers,
            'seguindo': profile.followees,
            'bio': profile.biography,
            'url_perfil': f"https://instagram.com/{profile.username}"
        }
        return dados
    except Exception as e:
        print(f"Erro ao buscar informações do Instagram: {e}")
        return None
