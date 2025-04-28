import re
from urllib.parse import urlparse

def validar_link_esports(link):
    """Valida se o link pertence a plataformas de esports válidas (HLTV, Liquipedia)."""
    valid_domains = ['hltv.org', 'liquipedia.net']
    try:
        parsed_url = urlparse(link)
        domain = parsed_url.netloc.lower()

        if any(valid_domain in domain for valid_domain in valid_domains):
            return True
        return False
    except Exception as e:
        return False
