def Msg():
    print ('=======================')
    print ('\033[0;33m      THE KING  \033[0;m           ')
    print ('=======================')

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
    tamanho_da_senha = 10
    for i in range(tamanho_da_senha):
        senhasegura += choice(caracters)
    print(f' SENHA GERADA: {senhasegura} ') 
    return senhasegura 

def Carteira(email):
    import sqlite3
    from sqlite3 import Error
    from CARTEIRA import Carteira
    from JOGADORES import Menu_acesso
    print ('\033[0;33m=======================')
    print ('  1- SACAR  ')
    print ('  2- DEPOSITAR')
    print ('  3- MENU   ')
    print ('=======================\033[0;m')
    c = '100'
    c= str(input(' ------- AÇÃO ------- \n '))
    while c!='0':
        if c=='1':
            conta1 = Carteira(email)
            conta1.Sacar()
        if c=='2':
            conta1 = Carteira(email)
            conta1.Depositar()
        if c=='3':
            return Menu_acesso
        else: 
            print(' AÇÃO INVÁLIDA ')
            c = str(input(' ------- AÇÃO ------- \n '))
            continue 
Carteira('teteu@gmail.com')

def Jogos(email):
    from JOGADORES import Menu_acesso, Jogadores
    print ('\033[0;33m=======================')
    print ('  1- DADOS')
    print ('  2- BLACK JACK')
    print ('  3- ROLETA')
    print ('  4- MENU ')
    print ('=======================\033[0;m')
    j= '100'
    j= str(input(' ------- AÇÃO ------- \n '))
    while j!='0':
        if j=='1':
            pass 
        if j=='2':
            pass 
        if j=='3':
            pass 
        if j=='4':
            return Menu_acesso 
        else: 
            print(' AÇÃO INVÁLIDA ')
            j = str(input(' ------- AÇÃO ------- \n '))
            continue 

def Açoes(email):
    from JOGADORES import Menu_acesso, Jogadores
    print ('\033[0;33m=======================')
    print ('  1- ALTERAR')
    print ('  2- DELETAR')
    print ('  3- MENU   ')
    print ('=======================\033[0;m')
    a = '100'
    a= str(input(' ------- AÇÃO ------- \n '))
    while a!='0':
        if  a =='1':
            conta1 = Jogadores()
            conta1.Alterar(email)
        if a =='2':
            conta1 = Jogadores()
            conta1.Deletar(email)
        if a =='3':
            return Menu_acesso
        else: 
            print(' AÇÃO INVÁLIDA ')
            a = str(input(' ------- AÇÃO ------- \n '))
            continue 

def Dados(email):
    import sqlite3
    from sqlite3 import Error
    try:
        con = sqlite3.connect ('CASSINO (1).db')
        con.execute('PRAGMA foreign_keys = 1') 
        cursor = con.cursor() 
    except Error as ex:
         print (ex)
    else: 
        cursor.execute('SELECT nome FROM JOGADORES WHERE email = ?',(email,))
        for linha in cursor.fetchall():
            print (linha[0])
        cursor.execute('SELECT DINAR FROM CARTEIRA WHERE email = ?',(email,))
        for linha in cursor.fetchall():
            print (f'Ð: {linha[0]}')
