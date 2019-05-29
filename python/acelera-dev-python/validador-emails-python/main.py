import re
def valid_email(email):
    
    """
     Padrão de e-mail: 
        username@websitename.extension
     DETALHAMENTO DA RE 
        ^[a-zA-Z0-9_.-]+           usuário só pode conter letras, dígitos e os caracteres -, . e _ 
        @[a-zA-Z0-9-]+             site só pode ter letras e dígitos
        (\.[a-zA-Z0-9-.]{1,3})+$   comprimento máximo da extensão é 1, 2, 3 caracteres
    """
    pattern = re.compile(r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-.]{1,3})+$")
    # Se der match, retorno True
    return bool((re.fullmatch(pattern, email)))


def filter_email(emails):
    rv = list(filter(valid_email, emails))
    return rv



