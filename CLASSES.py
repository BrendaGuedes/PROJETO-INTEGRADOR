import sqlite3
from time import sleep
from sqlite3 import Error
from FUNÇOES import check,Senha,Dados,Msg_delete

def Menu ():
    print ('\033[0;33m=======================')
    print ('  1- CRIAR ')
    print ('  2- ACESSAR')
    print ('  0- SAIR:')
    print ('=======================\033[0;m')
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
                        print ('Opss! Digite seu email.')
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
                                    return Menu()
                                if a =='2':                  
                                    continue
                                else:
                                    print(' AÇÃO INVÁLIDA ')
                                    return Menu()
                            else: 
                                conta1 = Jogadores()
                                conta1.Criar(vemail)
                                exit()
        if x=='2':
            conta1 = Jogadores()
            conta1.Entrar()
            exit()
            pass 
        if x=='0':
                print ('GOLDEN ENCERRADO!')
                exit()
        else:
            print(' AÇÃO INVÁLIDA ')
            x = str(input(' ------- AÇÃO ------- \n'))
            continue 

def Menu_acesso(email):
    print ('=======================\033[0;m')
    Dados ( email )
    print ('\033[0;33m=======================')
    print ('  0- SAIR:')
    print ('  1- CARTEIRA')
    print ('  2- JOGOS')
    print ('  3- CONFIGURAÇÕES')
    print ('=======================\033[0;m')
    x = '100'
    x= str(input(' ------- AÇÃO ------- \n'))
    while x!='eeeee1000':
        if x=='1':
            print ('\033[0;33m=======================')
            print ('  1- SACAR  ')
            print ('  2- DEPOSITAR')
            print ('  3- MENU   ')
            print ('=======================\033[0;m')
            c = '100'
            c= str(input(' ------- AÇÃO ------- \n'))
            while c!='eeeee1000':
                if c=='1':
                    conta1 = Carteira(email)
                    conta1.Sacar()
                if c=='2':
                    conta1 = Carteira(email)
                    conta1.Depositar()
                if c=='3':
                    return Menu_acesso(email)
                else: 
                    print(' AÇÃO INVÁLIDA ')
                    c = str(input(' ------- AÇÃO ------- \n'))
                    continue 
        if x=='2':
            print ('\033[0;33m=======================')
            print ('  1- DADOS')
            print ('  2- BLACK JACK')
            print ('  3- ROLETA')
            print ('  4- MENU ')
            print ('=======================\033[0;m')
            j= '100'
            j= str(input(' ------- AÇÃO ------- \n'))
            while j!='eeeee1000':
                if j=='1':
                    pass  
                if j=='2':
                    pass 
                if j=='3':
                    pass 
                if j=='4':
                    return Menu_acesso(email)
                else: 
                    print(' AÇÃO INVÁLIDA ')
                    j = str(input(' ------- AÇÃO ------- \n'))
                    continue 
        if x=='3':
            print ('\033[0;33m=======================')
            print ('  1- ALTERAR')
            print ('  2- DELETAR')
            print ('  3- MENU   ')
            print ('=======================\033[0;m')
            a = '100'
            a= str(input(' ------- AÇÃO ------- \n'))
            while a!='eeeee1000':
                if  a =='1':
                    conta1 = Jogadores()
                    conta1.Alterar(email)
                if a =='2':
                    conta1 = Jogadores()
                    conta1.Deletar(email)
                if a =='3':
                    return Menu_acesso(email)
                else: 
                    print(' AÇÃO INVÁLIDA ')
                    a = str(input(' ------- AÇÃO ------- \n'))
                    continue 
        if x=='0':
            print ('ENCERRADA AS APOSTAS!')
            exit()
        else:
            print(' AÇÃO INVÁLIDA ')
            x = str(input(' ------- AÇÃO ------- \n'))
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
                    print ('Opss! Digite seu nome\nCadrastre um nome usando letras, números ou qualquer outra caracter.')
                    continue
                if (len(vnome)<6):
                    print ('Opss! Número insuficiente de caracter,requerimos pelo menos 6.')
                    continue
                if (len(vnome)>=10):
                    print('Opss! Número de caracter ultrapassado,requerimos pelo menos 10. ')
                    continue
                else:
                    sleep(1)
                    print ('Uma senha de 10 digitos será gerada, guarde essa senha para acessar o sistema!\nDepois que o sistema for acessado você poderá alterar ou manter essa senha.')
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
                elif check(vemail) == False:
                    continue
                else:
                    cursor.execute('SELECT COUNT (email), email FROM JOGADORES WHERE email = ?',(vemail,))
                    for linha in cursor.fetchall():
                        if linha [0] == 0:
                            sleep(1)
                            print ('Email não econtrado!')
                            print ('-------------------- ')
                            return Menu()
                        elif linha [0] == 1:
                            sleep(1)
                            print ('- ENCONTRADO -')
                            print ('------------------- ')
                            sleep(1)
                            while True: 
                                senha= str(input('SENHA:'))
                                if ((len(senha)==0) or senha.isspace()):
                                    print ('Opss! digite sua senha.')
                                    continue
                                else:
                                    cursor.execute('SELECT email, senha FROM JOGADORES WHERE email = ?',(vemail,))
                                    for linha in cursor.fetchall():
                                        if linha [1] == senha:
                                            sleep(1)
                                            print ('- ACESSO PERMITIDO -')
                                            return Menu_acesso(vemail) 
                                        else:
                                            sleep(1)
                                            print('- ACESSO NEGADO -')
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
            sleep(1)
            while True:
                vmail = str(input('CONFIRME SEU EMAIL:'))
                if ((len(vmail)==0) or vmail.isspace()):
                    print ('Opss! Digite sua email.')
                    continue
                elif vmail!= email:
                    print ('Opss! Email incorreto, tente novmente.')
                    continue
                else:
                    while True:
                        senha= str(input('SENHA:'))
                        if ((len(senha)==0) or senha.isspace()):
                            print ('Opss! Digite sua senha.')
                            continue 
                        else:
                            cursor.execute('SELECT email, senha FROM JOGADORES WHERE email=?',(email,))
                            for linha in cursor.fetchall():
                                if linha [1] == senha:
                                    print ('- ACESSO PERMITIDO -')
                                    print ('---------------------')
                                    while True:
                                        n = input('1 - Alterar senha \n2 - Alterar nome \n3 - SAIR \n')
                                        if n == '1': 
                                            sleep(1)
                                            print ('- ALTERANDO SENHA -')
                                            while True: 
                                                nova_s= str(input('NOVA SENHA:'))
                                                if ((len(nova_s)==0) or nova_s.isspace()):
                                                    print ('Opss! Digite sua nova senha')
                                                    continue
                                                elif (len(nova_s)<6): 
                                                    print ('Opss! Número insuficiente de caracter,requerimos pelo menos 6.')
                                                    continue
                                                elif len(nova_s)>11:
                                                    print ('Opss! Número de caracter ultrapassado, requerimos pelo menos 11.')
                                                else:
                                                    if not any(x.isupper() for x in nova_s):
                                                        print('Opss! Requerimos pelo menos uma letra maiúscula.')
                                                        continue 
                                                    elif not any(x.islower() for x in nova_s):
                                                        print('Opss! Requirimos pelo menos uma letra minúscula.')
                                                        continue 
                                                    elif not any(x.isdigit() for x in nova_s):
                                                        print('Opss! Requirimos pelo menos um número.')
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
                                                nova_n= str(input('NOVO NOME:')).upper()
                                                if ((len(nova_n)==0) or nova_n.isspace()):
                                                    print ('Opss! Digite seu nome!')
                                                    continue
                                                if (len(nova_n)<6):
                                                    print ('Opss! Número insuficiente de caracter,requerimos pelo menos 6.')
                                                    continue
                                                if (len(nova_n)>=10):
                                                    print('Opss! Número de caracter ultrapassado,requerimos pelo menos 10. ')
                                                    continue
                                                else:
                                                    cursor.execute('UPDATE JOGADORES SET nome=? WHERE email=?',(nova_n,email))
                                                    con.commit()
                                                    cursor.close()
                                                    con.close()
                                                    print ('- NOME ALTERADA -')
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
                                    return Menu_acesso(email)
    
    def Deletar(self,email):
        try:
            con = sqlite3.connect ('CASSINO (1).db')
            con.execute('PRAGMA foreign_keys = 1') 
            cursor = con.cursor() 
        except Error as ex:
            print (ex)
        else:
            print(email)
            cursor.execute('SELECT * FROM JOGADORES')
            sleep(1)
            while True:
                vmail = str(input('CONFIRME SEU EMAIL:'))
                if ((len(vmail)==0) or vmail.isspace()):
                        print ('Opss! Digite sua email.')
                        continue
                elif vmail!= email:
                    print ('Opss! Email incorreto, tente novmente.')
                    continue
                else:
                    while True:
                        senha= str(input('SENHA:'))
                        if ((len(senha)==0) or senha.isspace()):
                                print ('Opss! Digite sua senha.')
                                continue
                        else:
                            cursor.execute('SELECT email, senha FROM JOGADORES WHERE email=?',(email,))
                            for linha in cursor.fetchall():
                                if linha [1] == senha:
                                            sleep(1)
                                            print ('ACESSO PERMITIDO')
                                            print ('-------------------')
                                            cursor.execute('DELETE FROM JOGADORES WHERE email=?',(email,))  
                                            con.commit()
                                            Msg_delete()
                                            cursor.close()
                                            con.close()
                                            exit()
                                else:
                                    sleep(1)
                                    print ('ACESSO NEGADO')
                                    return Menu_acesso(email)

class Carteira:
    def __init__(self,email) -> None:
        self.email = email

    def Sacar(self):
        try:
            con = sqlite3.connect ('CASSINO (1).db')
            con.execute('PRAGMA foreign_keys = 1') 
            cursor = con.cursor()
        except Error as ex:
            print (ex)
        else:
            while True:
                senha = str(input('SENHA:'))
                cursor.execute('SELECT COUNT(email),senha FROM JOGADORES WHERE email=?',(self.email,))
                for linha in cursor.fetchall():
                    if linha[1] == senha:
                        while True:
                            try:
                                valor = float(input("SACAR:"))
                            except ValueError:
                                print("Opss! Inválido...")
                                continue
                            else: 
                                cursor.execute('SELECT DINAR FROM CARTEIRA WHERE email=?',(self.email,))
                                for vlinha in cursor.fetchall():
                                    x = vlinha[0]
                                    if valor >x:
                                        print('SACAR, não pode ser executado Ð insuficiente.')
                                        return Menu_acesso(self.email)
                                    if valor <=x:
                                        print('PROCESSANDO')
                                        x-=valor
                                        cursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email=?',(x,self.email))
                                        con.commit()
                                        print ('- VALOR REMOVIDO DE CARTEIRA -')
                                        return Menu_acesso(self.email)
                    else:
                        print('- ACESSO NEGADO -')
                        print('------------------- ')
                        continue 

    def Depositar(self):
        try:
            con = sqlite3.connect ('CASSINO (1).db')
            con.execute('PRAGMA foreign_keys = 1') 
            cursor = con.cursor()
        except Error as ex:
            print (ex)
        else:
            while True:
                senha = str(input('SENHA:'))
                cursor.execute('SELECT COUNT(email),senha FROM JOGADORES WHERE email=?',(f"{self.email}",))
                for linha in cursor.fetchall():
                    if linha[1] == senha:
                        while True:
                            try:
                                valor = float(input("DEPOSITAR:"))
                            except ValueError:
                                print("Opss! Inválido...")
                                continue
                            else:
                                if valor > 200:
                                    print ('Só adicionamos valores menores, a Ð:200.')
                                    continue 
                                else:
                                    cursor.execute('SELECT DINAR FROM CARTEIRA WHERE email=?',(self.email,))
                                    for vlinha in cursor.fetchall():
                                        x = vlinha[0]             
                                        x += valor
                                    cursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email=?',(x,self.email))
                                    con.commit()
                                    print ('- VALOR ADICIONADO A CARTEIRA -')
                                    return Menu_acesso(self.email)
                    else:
                        print('- ACESSO NEGADO -')
                        print('------------------- ')
                        continue

