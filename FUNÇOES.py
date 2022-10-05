from platform import java_ver
import sqlite3
from sqlite3 import Error

def Msg():
    print ('=======================')
    print ('\033[0;33m       GOLDEN   \033[0;m           ')
    print ('=======================')
    print ('')

def check(email):
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
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
    print(f'SENHA GERADA:\n  {senhasegura} ') 
    
    return senhasegura 

def Dados(email):
    try:
        con = sqlite3.connect ('CASSINO (1).db')
        con.execute('PRAGMA foreign_keys = 1') 
        cursor = con.cursor() 
    except Error as ex:
         print (ex)
    else: 
        cursor.execute('SELECT nome,id FROM JOGADORES WHERE email = ?',(email,))
        for linha in cursor.fetchall():
            print (linha[0])
            print (f'ID:{linha[1]}')
        cursor.execute('SELECT DINAR FROM CARTEIRA WHERE email = ?',(email,))
        for linha in cursor.fetchall():
            print (f'Ð:{linha[0]}')

def Msg_delete():
    print ('- CONTA DELETADA -\nEsperamos que sua experiência tenha sido boa!\nConfirmamos que sua conta foi deletada do sistema, os dados referentes ao seu email foram todos apagados. ')