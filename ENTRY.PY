import sqlite3
from time import sleep
from sqlite3 import Error
from CLASS import Jogadores
from FUNÇOES import Msg,check,Msg 

def Menu_principal():
    Msg()
    print ('\033[0;33m  1- CRIAR ')
    print ('  2- ACESSAR')
    print ('  0- SAIR:\033[0;m')
    print ('=======================')
    x = '100'
    x= str(input(' ------- AÇÃO ------- \n'))
    while x!='eeeeee1000':
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
                                a = input(('Email já cadastrado, retorne ao (1) Menu  ou (2) Cadastre um Email novo! \n'))
                                if a =='1':
                                    return Menu_principal()
                                    exit()
                                if a =='2':                  
                                    continue
                                else:
                                    print(' AÇÃO INVÁLIDA ')
                                    return Menu_principal()
                            else: 
                                conta1 = Jogadores()
                                conta1.Criar(vemail)
                                exit()
        if x=='2':
            conta1 = Jogadores()
            conta1.Entrar()
            exit()
        if x=='0':
            sleep(1)
            print ('GOLDEN ENCERRADO!')
            exit()
        else:
            print(' AÇÃO INVÁLIDA ')
            x = str(input(' ------- AÇÃO ------- \n'))
            continue 

Menu_principal()   