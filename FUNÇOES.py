def check(email):
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        print("Email válido")
        return True
    else:
        print("Email inválido")
        return False 

def Senha():
    import string
    from random import choice
    caracters = string.ascii_letters + string.digits 
    senhasegura = ''
    tamanho_da_senha = 7
    for i in range(tamanho_da_senha):
        senhasegura += choice(caracters)
    print(f' SENHA GERADA: {senhasegura} ') 
    return senhasegura 

