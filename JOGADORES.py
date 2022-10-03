import sqlite3
from time import sleep
from FUNÇOES import check,Senha
from sqlite3 import Error

def Menu ():
    import sqlite3
    from time import sleep
    from sqlite3 import Error
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
                exit()
        else:
            print(' AÇÃO INVÁLIDA ')
            x = str(input(' ------- AÇÃO ------- \n '))
            continue 

def Menu_acesso(email):
    print ('=======================')
    print ('  1- ALTERAR')
    print ('  2- DELETAR')
    print ('  0- SAIR:')
    print ('=======================')
    x = '100'
    x= str(input(' ------- AÇÃO ------- \n '))
    while x!='0':
        if x=='1':
            conta1 = Jogadores()
            conta1.Alterar(email)
        if x=='2':
            conta1 = Jogadores()
            conta1.Deletar(email)
        if x=='0':
            exit()
        else:
            print(' AÇÃO INVÁLIDA ')
            x = str(input(' ------- AÇÃO ------- \n '))
            continue 




class Jogadores:

    def Criar (self,vemail):
        try:
            con = sqlite3.connect ('CASSINO (1).db')
            con.execute('PRAGMA foreign_keys = 1') 
            cursor = con.cursor() 
        except Error as ex:
            print (ex)
        else:
            sleep(1)
            while True:
                vnome = str(input('NOME:')).upper()
                if ((len(vnome)==0) or vnome.isspace()):
                    print ('Opss! Digite seu nome\nCadrastre um nome usando letras, números ou qualquer outra caracter!')
                    continue
                else:
                    sleep(1)
                    print ('Uma senha de 7 digitos será gerada, guarde essa senha para acessar o sistema!')
                    cursor.execute('INSERT INTO JOGADORES (nome,email,senha) VALUES (?,?,?)',(vnome,vemail,Senha()))
                    cursor.execute('INSERT INTO CARTEIRA (DINAR,email) VALUES (?,?)',(0,vemail))
                    con.commit()
                    sleep(1)
                    print ('- CADASTRO FINALIZADO -')
                    print ('------------------- ')
                    cursor.close()
                    con.close()
                    return Menu()
                break 

    def Entrar (self):
        try:
            con = sqlite3.connect ('CASSINO (1).db')
            con.execute('PRAGMA foreign_keys = 1') 
            cursor = con.cursor() 
        except Error as ex:
            print (ex)
        else:
            sleep(1)
            while True :
                vemail = input('DIGITE SEU EMAIL:')
                if ((len(vemail)==0) or vemail.isspace()):
                    print ('Opss! Digite seu email')
                    continue
                else:
                    cursor.execute('SELECT COUNT (email), email FROM JOGADORES WHERE email = ?',(vemail,))
                    for linha in cursor.fetchall():
                        if linha [0] == 0:
                            sleep(1)
                            print ('Email não econtrado!')
                            print ('-------------------- ')
                            continue
                        elif linha [0] == 1:
                            sleep(1)
                            print ('- ENCONTRADO -')
                            print ('------------------- ')
                            sleep(1)
                            senha= str(input('SENHA:'))
                            cursor.execute('SELECT email, senha FROM JOGADORES WHERE email = ?',(vemail,))
                            for linha in cursor.fetchall():
                                if linha [1] == senha:
                                    sleep(1)
                                    print ('- ACESSO PERMITIDO -')
                                    cursor.execute('SELECT nome FROM JOGADORES WHERE email = ?',(vemail,))
                                    for linha in cursor.fetchall():
                                        print (linha[0])
                                        cursor.execute('SELECT DINAR FROM CARTEIRA WHERE email = ?',(vemail,))
                                        for linha in cursor.fetchall():
                                            print (f'Ð: {linha[0]}')
                                            return Menu_acesso(vemail) 
                                else:
                                    sleep(1)
                                    print ('- ACESSO NEGADO -')
                                    return Menu()
    
    def Alterar(self,email):
        try:
            con = sqlite3.connect ('CASSINO (1).db')
            con.execute('PRAGMA foreign_keys = 1') 
            cursor = con.cursor() 
        except Error as ex:
            print (ex)
        else:
            cursor.execute('SELECT * FROM JOGADORES')
            while True:
                print(email)
                sleep(1)
                senha= str(input('SENHA:'))
                if ((len(senha)==0) or senha.isspace()):
                    print ('Opss! Digite sua senha!')
                else:
                    cursor.execute('SELECT email, senha FROM JOGADORES WHERE email=?',(email,))
                    for linha in cursor.fetchall():
                                if linha [1] == senha:
                                    print ('- ACESSO PERMITIDO -')
                                    while True:
                                        n = input('1 - Alterar senha \n2 - Alterar nome \n3 - SAIR \n...')
                                        if n == '1': 
                                            sleep(1)
                                            print ('- ALTERANDO SENHA -')
                                            while True: 
                                                nova_s= str(input('NOVA SENHA:'))
                                                if ((len(nova_s)==0) or nova_s.isspace()):
                                                    print ('Opss! Digite seu nome!')
                                                    continue
                                                else:
                                                    cursor.execute('UPDATE JOGADORES SET senha=? WHERE email=?',(nova_s,email))
                                                    con.commit()
                                                    print ('- SENHA ALTERADA -')
                                                    cursor.close()
                                                    con.close()
                                                    return Menu_acesso(email)
                                        if n == '2':
                                            sleep(1)
                                            print ('- ALTERANDO NOME -')
                                            while True:
                                                nova_n= str(input('NOVO NOME:'))
                                                if ((len(nova_n)==0) or nova_n.isspace()):
                                                    print ('Opss! Digite seu nome!')
                                                    continue
                                                else:
                                                    cursor.execute('UPDATE JOGADORES SET nome=? WHERE email=?',(nova_n,email))
                                                    con.commit
                                                    cursor.close()
                                                    con.close()
                                                    return Menu_acesso(email)
                                        if n == '3':
                                            return Menu_acesso(email)
                                            exit() 
                                        else:
                                            print ('AÇÃO INVÁLIDA ')
                                            print ('-------------------')
                                            continue
                                else:
                                    print ('- ACESSO NEGADO -')
                                    print ('------------------- ')
                                    return Menu_acesso(email)
    
    def Deletar(self,email):
        try:
            con = sqlite3.connect ('CASSINO (1).db')
            con.execute('PRAGMA foreign_keys = 1') 
            cursor = con.cursor() 
        except Error as ex:
            print (ex)
        else:
            cursor.execute('SELECT * FROM JOGADORES')
            senha= str(input('SENHA:'))
            cursor.execute('SELECT email, senha FROM JOGADORES WHERE email=?',(email,))
            for linha in cursor.fetchall():
                if linha [1] == senha:
                            print ('ACESSO PERMITIDO')
                            cursor.execute('DELETE FROM JOGADORES WHERE email=?',(email,))  
                            con.commit()
                            print ('- CONTA DELETADA -')
                            exit()
                else:
                    print ('ACESSO NEGADO')
                    print ('------------------- ')
                    return Menu_acesso(email)

Menu()