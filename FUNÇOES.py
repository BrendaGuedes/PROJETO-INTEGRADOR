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

def Carteira():
    print ('=======================')
    print ('  1- SACAR  ')
    print ('  2- DEPOSITAR')
    print ('=======================')
    c = '100'
    c= str(input(' ------- AÇÃO ------- \n '))
    while c!='0':
        if c=='1':
            return '1'
        if c=='2':
            return '2'
        else: 
            print(' AÇÃO INVÁLIDA ')
            c = str(input(' ------- AÇÃO ------- \n '))
            continue 

def Jogos():
    print ('=======================')
    print ('  1- DADOS')
    print ('  2- BANCA')
    print ('  3- ROLETA')
    print ('=======================')
    j= '100'
    j= str(input(' ------- AÇÃO ------- \n '))
    while j!='0':
        if j=='1':
            return '1'
        if j=='2':
            return '2'
        if j=='3':
            return '3'
        else: 
            print(' AÇÃO INVÁLIDA ')
            j = str(input(' ------- AÇÃO ------- \n '))
            continue 

def Açoes():
    print ('=======================')
    print ('  1- ALTERAR')
    print ('  2- DELETAR')
    print ('=======================')
    a = '100'
    a= str(input(' ------- AÇÃO ------- \n '))
    while a!='0':
        if a=='1':
            return '1'
        if a=='2':
            return '2'
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

def Msg():
    print ('=======================')
    print ('   THE VEGAS\033[0;31m')
    print ('=======================')
    pass 