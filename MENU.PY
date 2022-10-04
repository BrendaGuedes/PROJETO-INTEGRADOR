from JOGADORES import Jogadores
from FUNÇOES import check,Senha,Carteira,Dados,Jogos,Açoes

def Menu ():
    import sqlite3
    from time import sleep
    from sqlite3 import Error
    print ('=======================')
    print ('   THE VEGAS\033[0;31m')
    print ('=======================')
    print ('  1- CRIAR ')
    print ('  2- ACESSAR')
    print ('  0- SAIR:')
    print ('=======================')
    x = '100'
    x= str(input(' ------- AÇÃO ------- \n '))
    while x!='0':
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
            print ('ENCERRADA AS APOSTAS!')
            exit()
        else:
            print(' AÇÃO INVÁLIDA ')
            x = str(input(' ------- AÇÃO ------- \n '))
            continue 

def Menu_acesso(email):
    Dados ( email )
    print ('=======================')
    print ('  0- SAIR:')
    print ('  1- CARTEIRA')
    print ('  2- JOGOS')
    print ('  3- CONFIGURAÇÕES')
    print ('=======================')
    x = '100'
    x= str(input(' ------- AÇÃO ------- \n '))
    while x!='0':
        if x=='1':
            Carteira()
            if Carteira=='1':
                pass 
            if Carteira=='2':
                pass  
        if x=='2':
            Jogos()
            if Jogos=='1':
                pass 
            if Jogos=='2':
                pass 
            if Jogos=='3':
                pass 
        if x=='3':
            Açoes()
            if Açoes =='1':
                conta1 = Jogadores()
                conta1.Alterar(email)
            if Açoes =='2':
                conta1 = Jogadores()
                conta1.Deletar(email)
        if x=='0':
            print ('ENCERRADA AS APOSTAS!')
            exit()
        else:
            print(' AÇÃO INVÁLIDA ')
            x = str(input(' ------- AÇÃO ------- \n '))
            continue 

Menu()
Menu_acesso('teteu@gmail.com')