from FUNÇOES import check,Senha
from JOGADORES import Jogadores

def Menu ():
    import sqlite3
    from time import sleep
    from sqlite3 import Error
    print ('======================')
    print ('  1- CRIAR ')
    print ('  2- ACESSAR')
    print ('  0- SAIR:')
    print ('======================')
    x = '100'
    while x!='0':
        x= str(input(' ------- AÇÃO ------- \n '))
        if x=='1':
            try:
                con = sqlite3.connect ('CASSINO (1).db')
                con.execute('PRAGMA foreign_keys = 1') 
                cursor = con.cursor() 
            except Error as ex:
                print (ex)
            else:
                print ('- CADASTRANDO -')
                sleep(1)
            while True:
                    vemail = str(input('CADASTRE SEU EMAIL:'))
                    if ((len(vemail)==0) or vemail.isspace()):
                        print ('Opss! Digite seu email')
                        continue
                    elif check(vemail) == False:
                        continue
                    else:
                        sleep(1)
                        cursor.execute('SELECT COUNT (*) FROM JOGADORES WHERE email=?',(vemail,))
                        for linha in cursor.fetchall():
                            if linha[0]==1:
                                a = input(('Email já cadastrado, retorne ao (1) Menu  ou (2) Cadastre um Email novo! \n '))
                                if a =='1':
                                    return Menu()
                                    exit()
                                if a =='2':                  
                                    continue
                                else:
                                    print(' AÇÃO INVÁLIDA ')
                                    return Menu()
                            else: 
                                conta = Jogadores()
                                conta.Criar(vemail)
                                exit()
        if x=='2':
            conta1 = Jogadores()
            conta1.Entrar()
            exit()
            pass 
        if x=='0':
                exit()
        else:
            print(' AÇÃO INVÁLIDA ')
            x = str(input(' ------- AÇÃO ------- \n '))
            continue 

def Menu_acesso():
    print(EMAIL1)
    print ('======================')
    print ('  1- ALTERAR')
    print ('  2- DELETAR')
    print ('  0- SAIR:')
    print ('======================')
    x = '100'
    while x!='0':
        x= str(input(' ------- AÇÃO ------- \n '))
        if x=='1':
            conta1 = Jogadores()
            conta1.Alterar()
        if x=='2':
            conta1 = Jogadores()
            conta1.Deletar()
        if x=='0':
            exit()
        else:
            print(' AÇÃO INVÁLIDA ')
            x = str(input(' ------- AÇÃO ------- \n '))
            continue 