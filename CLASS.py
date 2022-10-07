import sys
import random
import sqlite3
from ast import Str
from time import sleep
from sqlite3 import Error
from FUNÇOES import check,Senha,Dados

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

        if x=='0':
                print ('GOLDEN ENCERRADO!')
                exit()
        else:
            print(' AÇÃO INVÁLIDA ')
            x = str(input(' ------- AÇÃO ------- \n'))
            continue 

def Menu_acesso(email):
    print ('====================\033[0;m')
    Dados (email)
    print ('===              ===')
    print ('\033[0;33m  0- SAIR:')
    print ('  1- CARTEIRA')
    print ('  2- JOGOS')
    print ('  3- CONFIGURAÇÕES\033[0;m')
    print ('=======================')
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
            print ('  2- BLACKJACK')
            print ('  3- ROLETA')
            print ('  4- MENU ')
            print ('=======================\033[0;m')
            j= '100'
            j= str(input(' ------- AÇÃO ------- \n'))
            while j!='eeeee1000':
                if j=='1':
                    Guia(email)
                if j=='2':
                    conta1 = Black_Jack(email,Vericar_Black(email))
                    conta1.Black() 
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
                if (len(vnome)<4):
                    print ('Opss! Número insuficiente de caracter, limite mínimo requerido é 4.')
                    continue
                if (len(vnome)>=10):
                    print('Opss! Número de caracter ultrapassado, limite máximo requerido é 10. ')
                    continue
                else:
                    sleep(1)
                    print ('Uma senha de 10 digitos será gerada, guarde essa senha para acessar o sistema!\nDepois que o sistema for acessado você poderá alterar ou manter essa senha.')
                    cursor.execute('INSERT INTO JOGADORES (nome,email,senha) VALUES (?,?,?)',(vnome,vemail,Senha()))
                    con.commit()
                    cursor.execute('INSERT INTO CARTEIRA (DINAR,email) VALUES (?,?)',(0,vemail))
                    con.commit()
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
                            print ('EMAIL NÃO ENCONTRADO!')
                            print ('---------------------')
                            return Menu()
                        elif linha [0] == 1:
                            sleep(1)
                            print ('- ENCONTRADO -')
                            print ('-------------------')
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
                                        n = input('1 - ALTERAR SENHA \n2 - ALTERAR NOME \n3 - SAIR \n')
                                        if n == '1': 
                                            sleep(1)
                                            print ('- ALTERANDO SENHA -')
                                            while True: 
                                                nova_s= str(input('NOVA SENHA:'))
                                                if ((len(nova_s)==0) or nova_s.isspace()):
                                                    print ('Opss! Digite sua nova senha')
                                                    continue
                                                elif (len(nova_s)<6): 
                                                    print ('Opss! Número insuficiente de caracter, limite mínimo requerido é 6.')
                                                    continue
                                                elif len(nova_s)>11:
                                                    print ('Opss! Número de caracter ultrapassado, limite máximo requerido é 11.')
                                                    continue
                                                else:
                                                    if not any(x.isupper() for x in nova_s):
                                                        print('Opss! Requerimos pelo menos uma letra maiúscula.')
                                                        continue
                                                    elif any(x.isspace() for x in nova_s):
                                                        print('Opss! Requirimos que retire os espaços em branco.')
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
                                                if (len(nova_n)<4):
                                                    print ('Opss! Número insuficiente de caracter, limite mínimo requerido é 4.')
                                                    continue
                                                if (len(nova_n)>=10):
                                                    print('Opss! Número de caracter ultrapassado, limite máximo requerido é 10. ')
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
            cursor.execute('SELECT * FROM JOGADORES')
            sleep(1)
            while True:
                vmail = str(input('CONFIRME SEU EMAIL:'))
                if ((len(vmail)==0) or vmail.isspace()):
                        print ('Opss! Digite sua email.')
                        continue
                elif vmail!= email:
                    print ('Opss! Email incorreto, tente novamente.')
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
                                            print ('- ACESSO PERMITIDO -')
                                            print ('-------------------')
                                            cursor.execute('DELETE FROM JOGADORES WHERE email=?',(email,))  
                                            con.commit()
                                            print ('\033[0;31m- CONTA DELETADA -\nEsperamos que sua experiência tenha sido boa!\nConfirmamos que sua conta foi deletada do sistema, os dados referentes ao seu email foram todos apagados.\033[0;m')
                                            cursor.close()
                                            con.close()
                                            exit()
                                else:
                                    sleep(1)
                                    print ('- ACESSO NEGADO -')
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
                while True:
                    senha = str(input('SENHA:'))
                    if ((len(senha)==0) or senha.isspace()):
                        print ('Opss! Digite seu senha.') 
                        continue
                    else:
                        cursor.execute('SELECT COUNT(email),senha FROM JOGADORES WHERE email=?',(self.email,))
                        for linha in cursor.fetchall():
                            if linha[1] == senha:
                                print ('- ACESSO PERMITIDO -')
                                print ('-------------------')
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
                                            elif valor <=0:
                                                print ('Opss! Informe um valor maior que 0.')
                                                continue
                                            elif valor <=x:
                                                print('- PROCESSANDO -')
                                                x-=valor
                                                cursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email=?',(x,self.email))
                                                con.commit()
                                                print (' VALOR REMOVIDO DA CARTEIRA ')
                                                return Menu_acesso(self.email)
                            else:
                                print('- ACESSO NEGADO -')
                                return Menu_acesso(self.email) 

    def Depositar(self):
        try:
            con = sqlite3.connect ('CASSINO (1).db')
            con.execute('PRAGMA foreign_keys = 1') 
            cursor = con.cursor()
        except Error as ex:
            print (ex)
        else:
            while True:
                while True:
                    senha = str(input('SENHA:'))
                    if ((len(senha)==0) or senha.isspace()):
                            print ('Opss! Digite seu senha.') 
                            continue
                    else:
                        cursor.execute('SELECT COUNT(email),senha FROM JOGADORES WHERE email=?',(f"{self.email}",))
                        for linha in cursor.fetchall():
                            if linha[1] == senha:
                                print ('- ACESSO PERMITIDO -')
                                print ('--------------------')
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
                                        elif valor <=0:
                                            print ('Opss! Informe um valor real maior que 0.')
                                            continue
                                        else:
                                            cursor.execute('SELECT DINAR FROM CARTEIRA WHERE email=?',(self.email,))
                                            for vlinha in cursor.fetchall():
                                                x = vlinha[0]             
                                                x += valor
                                            cursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email=?',(x,self.email))
                                            con.commit()
                                            print (' VALOR ADICIONADO A CARTEIRA ')
                                            return Menu_acesso(self.email)
                            else:
                                print('- ACESSO NEGADO -')
                                return Menu_acesso(self.email)


def Verificar(email):
        try:
            con = sqlite3.connect ('CASSINO (1).db')
            con.execute('PRAGMA foreign_keys = 1') 
            cursor = con.cursor()
        except Error as ex:
            print (ex)
        else:
            sleep(1)
            print('==================')
            print("      APOSTAS     ")
            print('==================')
            print("      VALORES     ")
            print('       Ð:10       ')
            print('       Ð:20       ')
            print('       Ð:50       ')
            print('       Ð:100      ')
            print('       Ð:150      ')
            print('==================')
            while True:
                try:
                    aposta = int(input('APOSTAR:'))
                except ValueError:
                    print("Opss! Inválido...")
                    continue    
                else:
                    if aposta!=10 and aposta!=20 and aposta!=50 and aposta!=100 and aposta!=150:
                        sleep(1)
                        print ('Opss! Requirimos que utilize os valores dentro da tabela.')
                        continue
                    cursor.execute('SELECT DINAR FROM CARTEIRA WHERE email=?',(email,))
                    for vlinha in cursor.fetchall():
                        x = vlinha[0]
                        if x>= aposta:
                            return aposta 
                        if x <aposta:
                            sleep(1)
                            print('APOSTA, não pode ser executado Ð insuficiente.')
                            return Menu_acesso(email)

def Guia(email):
        try:
            con = sqlite3.connect ('CASSINO (1).db')
            con.execute('PRAGMA foreign_keys = 1') 
            cursor = con.cursor()
        except Error as ex:
            print (ex)
        else:
            print ('')
            print ('\033[0;36mºººººººººººººººººººººººººººººººººººº')
            print ('               DADOS                ')
            print ('ºººººººººººººººººººººººººººººººººººº\033[0;m')
            print ('O objetivo do jogo é simples você poderá apostar um valor de sua escolha, escolhera os números para representar a sua aposta e os dados \nsortearam valores aleatórios para sobrepor os números da sua aposta, se o valor sorteado e os números da sua aposta forem equivalentes.\nParabéns,você recebera o valor da sua aposta duplicado ou até mesmo quadruplicado.\nSenão você poderá tentar novamente por uma nova opurtunidade de turbinar sua carteira.')
            sleep(1)
            print ('- DIFICULDADE -')
            print ('[1]Fácil\n 2 Dados serão usados para sobreposição do valor! Isso duplica sua aposta.')
            sleep(1)
            print ('[2]Médil\n 3 Dados serão usados para a sobreposição do valor! Isso triplica sua aposta.')
            sleep(1)
            print ('[3]Difícil\n 5 Dados serão usados para a sobreposição do valor! Isso quadruplica sua aposta.')
            fase = '100'
            while fase!='eeeeee1000':
                fase = str(input('- ESCOLHA A DIFICULDADE DESEJADA: \n'))
                if fase =='1':
                    conta1= Dado(email,Verificar(email))
                    conta1.Facil()
                if fase =='2':
                    conta1= Dado(email,Verificar(email))
                    conta1.Medio() 
                if fase =='3':
                    conta1= Dado(email,Verificar(email))
                    conta1.Dificil() 
                else: 
                    print(' AÇÃO INVÁLIDA ')
                    continue

def aplicar(email,valor):
    try:
        con = sqlite3.connect ('CASSINO (1).db')
        con.execute('PRAGMA foreign_keys = 1') 
        cursor = con.cursor()
    except Error as ex:
        print (ex)
    else:
        cursor.execute('SELECT DINAR FROM CARTEIRA WHERE email=?',(email,))
        for vlinha in cursor.fetchall():
            x = vlinha[0]             
            x += valor
        cursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email=?',(x,email))
        con.commit()
        return Menu_acesso(email)

def remover(email,valor):
    try:
        con = sqlite3.connect ('CASSINO (1).db')
        con.execute('PRAGMA foreign_keys = 1') 
        cursor = con.cursor()
    except Error as ex:
        print (ex)
    else:
        cursor.execute('SELECT DINAR FROM CARTEIRA WHERE email=?',(email,))
        for vlinha in cursor.fetchall():
            x = vlinha[0]       
            x-=valor
            cursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email=?',(x,email))
            con.commit()
            return Menu_acesso(email)

class Dado:
    def __init__(self,email,aposta) -> None:
        self.email = email 
        self.aposta = aposta 
    def Facil(self):
        print('\033[0;31m DICA: Os dados sortedos contém 6 lados, a soma total desses dados podem chegar até 12. Então escolha por números que sejam iguais a 12 ou menores que 12.\033[0;m')
        while True:
            try:
                valor1 = int(input("1º NÚMERO PARA REPRESENTAR A APOSTA:"))
            except ValueError:
                print("Opss! Inválido...")
                continue
            else:
                while True:
                    try:
                        valor2 = int(input("2º NÚMERO PARA REPRESENTAR A APOSTA:"))
                    except ValueError:
                        print("Opss! Inválido...")
                        continue
                    else:
                        tupla_vazia = ()
                        tupla_vazia = valor1, valor2 
                        print (f'O jogador escolheu os números {tupla_vazia[0]} e {tupla_vazia[1]} para representar sua aposta.')
                        print ('Serão sorteados 2 Dados de seis lados, a soma desses dados será a sobreposição equivalente ou não para a sua aposta.')
                        sleep(1)
                        x = random.randint(1,6)
                        print(f'1º Dado:{x}')
                        sleep(1)
                        c = random.randint(1,6)
                        print(f'2º Dado:{c}')
                        soma = x + c 
                        sleep(1)

                        if tupla_vazia[0]==soma:
                            print(' - PARABÉNS')
                            print (f'Somando o 1º Dado e o 2º Dado obtemos {soma} que é equivalente a sua aposta! - {tupla_vazia[0]}')
                            duplica= self.aposta*2  
                            sleep(1)
                            print(f'O valor Ð:{duplica} foi adicionado a carteira..')
                            aplicar(self.email,duplica)

                        elif tupla_vazia[1]==soma:
                            print(' - PARABÉNS')
                            print (f'Somando o 1º Dado e o 2º Dado obtemos {soma} que é equivalente a sua aposta! - {tupla_vazia[1]}')
                            duplica= self.aposta*2
                            sleep(1)
                            print(f'O valor Ð:{duplica} foi adicionado a carteira..')
                            aplicar(self.email,duplica) 

                        elif tupla_vazia[0]!=soma and tupla_vazia[1]!=soma : 
                            print (f'Somando o 1º Dado e o 2º Dado obtemos {soma} nenhuma das suas apostas é equivalente a soma!')
                            sleep(1)
                            print(f'O valor Ð:{self.aposta} foi retidado da carteira..\nPara reaver o valor JOGUE NOVAMENTE!')
                            remover(self.email,self.aposta)
    
    def Medio(self):
        print ('\033[0;31m DICA: Os dados sortedos contém 12 lados, a soma total desses dados podem chegar até 36. Então escolha por números que sejam iguais ou menores que 36.\033[0;m')
        while True:
            try:
                valor1 = int(input("1º NÚMERO PARA REPRESENTAR A APOSTA:"))
            except ValueError:
                print("Opss! Inválido...")
                continue
            else:
                while True:
                    try:
                        valor2 = int(input("2º NÚMERO PARA REPRESENTAR A APOSTA:"))
                    except ValueError:
                        print("Opss! Inválido...")
                        continue
                    else:
                        while True:
                            try:
                                valor3 = int(input("3º NÚMERO PARA REPRESENTAR A APOSTA:"))
                            except ValueError:
                                print("Opss! Inválido...")
                                continue
                            else: 
                                tupla_vazia = ()
                                tupla_vazia = valor1, valor2, valor3 
                                print (f'O jogador escolheu os números {tupla_vazia[0]}, {tupla_vazia[1]}, {tupla_vazia[2]}  para representar sua aposta.') 
                                print ('Serão sorteados 3 Dados de doze lados, a soma desses dados será a sobreposição equivalente ou não para a sua aposta.')
                                sleep(1)
                                x = random.randint(1,12)
                                print(f'1º Dado:{x}')
                                sleep(1)
                                c = random.randint(1,12)
                                print(f'2º Dado:{c}')
                                sleep(1)
                                d = random.randint(1,12)
                                print(f'3º Dado:{d}')
                                soma = x + c + d 
                                sleep(1)

                                if tupla_vazia[0]==soma:
                                    print(' - PARABÉNS')
                                    print (f'Somando o 1º Dado, 2º Dado e 3º Dado obtemos {soma} que é equivalente a sua aposta! - {tupla_vazia[0]}')
                                    triplica= self.aposta*3 
                                    sleep(1)
                                    print(f'O valor Ð:{triplica} foi adicionado a carteira..')
                                    aplicar(self.email,triplica)

                                elif tupla_vazia[1]==soma:
                                    print(' - PARABÉNS')
                                    print (f'Somando o 1º Dado, 2º Dado e 3º Dado obtemos {soma} que é equivalente a sua aposta! - {tupla_vazia[1]}')
                                    triplica= self.aposta*3 
                                    sleep(1)
                                    print(f'O valor Ð:{triplica} foi adicionado a carteira..')
                                    aplicar(self.email,triplica)

                                elif tupla_vazia[2]==soma:
                                    print(' - PARABÉNS')
                                    print (f'Somando o 1º Dado, 2º Dado, 3º Dado obtemos {soma} que é equivalente a sua aposta! - {tupla_vazia[2]}')
                                    triplica= self.aposta*3 
                                    sleep(1)
                                    print(f'O valor Ð:{triplica} foi adicionado a carteira..')
                                    aplicar(self.email,triplica)

                                elif tupla_vazia[0]!=soma and tupla_vazia[1]!=soma and tupla_vazia[2]!=soma: 
                                    print (f'Somando o 1º Dado, 2º Dado e 3º Dado obtemos {soma} nenhuma das suas apostas é equivalente a soma!')
                                    sleep(1)
                                    print(f'O valor Ð:{self.aposta} foi retidado da carteira..\nPara reaver o valor JOGUE NOVAMENTE!')
                                    remover(self.email,self.aposta)

    def Dificil(self):
        print ('\033[0;31m DICA: Os dados sortedos contém 12 lados, a soma total desses dados podem chegar até 60. Então escolha por números que sejam iguais ou menores que 60.\033[0;m')
        while True:
            try:
                valor1 = int(input("1º NÚMERO PARA REPRESENTAR A APOSTA:"))
            except ValueError:
                print("Opss! Inválido...")
                continue
            else:
                while True:
                    try:
                        valor2 = int(input("2º NÚMERO PARA REPRESENTAR A APOSTA:"))
                    except ValueError:
                        print("Opss! Inválido...")
                        continue
                    else:
                        while True:
                            try:
                                valor3 = int(input("3º NÚMERO PARA REPRESENTAR A APOSTA:"))
                            except ValueError:
                                print("Opss! Inválido...")
                                continue
                            else: 
                                tupla_vazia = ()
                                tupla_vazia = valor1, valor2, valor3
                                print (f'O jogador escolheu os números {tupla_vazia[0]}, {tupla_vazia[1]}, {tupla_vazia[2]}  para representar sua aposta.') 
                                print ('Serão sorteados 5 Dados de doze lados, a soma desses dados será a sobreposição equivalente ou não para a sua aposta.')
                                sleep(1)
                                x = random.randint(1,12)
                                print(f'1º Dado:{x}')
                                sleep(1)
                                c = random.randint(1,12)
                                print(f'2º Dado:{c}')
                                sleep(1)
                                d = random.randint(1,12)
                                print(f'3º Dado:{d}')
                                sleep(1)
                                e = random.randint(1,12)
                                print(f'4º Dado:{e}')
                                sleep(1)
                                i = random.randint(1,12)
                                print(f'5º Dado:{i}')
                                sleep(1)
                                soma = x + c + d + e + i
                                sleep(1)

                                if tupla_vazia[0]==soma:
                                    print(' - PARABÉNS')
                                    print (f'Somando o 1º Dado, 2º Dado, 3º Dado, 4º Dado e 5º Dado obtemos {soma} que é equivalente a sua aposta! - {tupla_vazia[0]}')
                                    quadruplica= self.aposta*4  
                                    sleep(1)
                                    print(f'O valor Ð:{quadruplica} foi adicionado a carteira..')
                                    aplicar(self.email,quadruplica)

                                elif tupla_vazia[1]==soma:
                                    print(' - PARABÉNS')
                                    print (f'Somando o 1º Dado, 2º Dado, 3º Dado, 4º Dado e 5º Dado obtemos {soma} que é equivalente a sua aposta! - {tupla_vazia[1]}')
                                    quadruplica= self.aposta*4  
                                    sleep(1)
                                    print(f'O valor Ð:{quadruplica} foi adicionado a carteira..')
                                    aplicar(self.email,quadruplica)

                                elif tupla_vazia[2]==soma:
                                    print(' - PARABÉNS')
                                    print (f'Somando o 1º Dado, 2º Dado, 3º Dado, 4º Dado e 5º Dado obtemos {soma} que é equivalente a sua aposta! - {tupla_vazia[2]}')
                                    quadruplica= self.aposta*4  
                                    sleep(1)
                                    print(f'O valor Ð:{quadruplica} foi adicionado a carteira..')
                                    aplicar(self.email,quadruplica)

                                elif tupla_vazia[0]!=soma and tupla_vazia[1]!=soma and tupla_vazia[2]!=soma: 
                                    print (f'Somando o 1º Dado, 2º Dado, 3º Dado, 4º Dado e 5º Dado obtemos {soma} nenhuma das suas apostas é equivalente a soma!')
                                    sleep(1)
                                    print(f'O valor Ð:{self.aposta} foi retidado da carteira..\nPara reaver o valor JOGUE NOVAMENTE!')
                                    remover(self.email,self.aposta)


def Vericar_Black(email):
    try:
        con = sqlite3.connect ('CASSINO (1).db')
        con.execute('PRAGMA foreign_keys = 1') 
        cursor = con.cursor()
    except Error as ex:
        print (ex)
    else:
        print('\033[0;33m-------------------\033[0;m')
        print("\033[0;33mMOEDA       VALORES\033[0;m")
        print('  \033[0;32mÐ\033[0;m ----------- \033[0;32m20\033[0;m')
        print('  \033[0;32mÐ\033[0;m ----------- \033[0;32m50\033[0;m')
        print('  \033[0;32mÐ\033[0;m ---------- \033[0;32m100\033[0;m')
        print('  \033[0;32mÐ\033[0;m ---------- \033[0;32m500\033[0;m')
        print('  \033[0;32mÐ\033[0;m --------- \033[0;32m1000\033[0;m')    
        print('\033[0;33m==================\033[0;m\n')
        aposta = "0"
        while aposta!='20' and aposta!='50'and aposta!='100'and aposta!='500'and aposta!='1000':
            aposta = str(input('Analisando seu jogo e a carta da Banca,\nEscolha algum valor da tabela para apostar\n\033[0;33m>> \033[0;m'))
        cursor.execute('SELECT DINAR FROM CARTEIRA WHERE email=?',(email,))
        for vlinha in cursor.fetchall():
            int(aposta)
            x = vlinha[0]
            if x>= int(aposta):
                return aposta
            if x <int(aposta):
                print('APOSTA, não pode ser executado Ð insuficiente.')
                return Menu_acesso(email)

class Black_Jack:
    def __init__(self,email,aposta) -> None:
        self.email = email
        self.aposta = aposta 
    def Black(self):
        A = 11
        Q = 10
        J = 10
        K = 10
        numbers = [ 2, 3, 4, 5, 6,
                7, 8, 9, 10, Q, J, K, A]
        suits = ["♣", "♦", "♥", "♠"]
        tracinhofofo = ('\033[0;31m-=\033[0;m')*40
        cartas = []
        pontos = []
        menuprincipal = '10'
        print(f"{tracinhofofo}\n           \033[0;33m♣ ♦ ♥ ♠\033[0;m \033[0;1;4mBEM-VINDO(A) AO BLACKJACK (JOGO 21)!\033[0;m \033[0;33m♣ ♦ ♥ ♠\033[0;m\n{tracinhofofo}")
        while menuprincipal != 'eeee100':
            menuprincipal = str(input('\nMENU: \n[1] INSTRUÇÕES DO JOGO\n[2] JOGAR\n\n \033[0;34mDIGITE UMA DAS OPÇÕES ACIMA\033[0;m\n\033[0;33m>> \033[0;m'))
            if menuprincipal == '1':
                print(f"{tracinhofofo}\n                         INSTRUÇÕES DO JOGO:                 \n{tracinhofofo}")
                print('\033[0;36mSeu objetivo no jogo é derrotar a Banca(dealer).\n'
                'Para fazer isso, você deve ter uma sequência em que a pontuação seja mais elevada\ndo que a sequência do dealer,'
                ' mas que não exceda21 pontos no valor total.\n'
                'Como alternativa, você pode ganhar tendo uma pontuação menor\nquando o valor da mão do dealer ultrapassar 21 pontos.\n'
                '\n\033[0;33m►\033[0;m \033[0;36mSe você desistir do jogo, perderá metade do valor apostado;\033[0;m\n'
                '\033[0;33m►\033[0;m \033[0;36mQuando o valor total da sua mão for 22 ou mais,\nvocê automaticamente vai perder qualquer dinheiro apostado;\033[0;m\n'
                '\033[0;33m►\033[0;m \033[0;36mCaso você ganhe, a Banca é obrigada a te dar o valor integral da aposta!\033[0;m')
                continue
            elif menuprincipal == '2':
                print(f"{tracinhofofo}\n                               INICIANDO JOGO...                 \n{tracinhofofo}")
                print('                      ¬¬¬¬¬¬¬¬¬¬  BOA SORTE! ¬¬¬¬¬¬¬¬¬¬  ')
                print('\n\033[0;33m>>\033[0;m GANHANDO CARTAS...\n')
                card1 = random.choice(numbers)
                card_1 = random.choice(suits)
                cartas.append(f"{card1}{card_1}")
                pontos.append(card1)
                print(f"Sua Primeira carta foi: \033[0;41m{card1}{card_1}\033[0;m")
                card2 = random.choice(numbers)
                card_2 = random.choice(suits)
                cartas.append(f"{card2}{card_2}")
                pontos.append(card2)
                print(f"Sua segunda carta foi: \033[0;41m{card2}{card_2}\033[0;m")
                print(f"O total da sua sequencia é de: \033[0;33m{sum(pontos)} pontos\033[0;m\n")
                print(f"\n{tracinhofofo}\n          AGORA CHEGOU A VEZ DA BANCA(dealer) GANHAR CARTA...\n{tracinhofofo}")   
                cardBk1 = random.choice(numbers)
                card_Bk1 = random.choice(suits)
                print(f"\nA primeira carta da Banca foi: \033[0;44m{cardBk1}{card_Bk1}\033[0;m")
                print('\nA segunda carta da Banca ainda está virada\n')
                print(f'\nO VALOR APOSTADO FOI: \033[0;32mÐ {self.aposta} \033[0;m\n')
                opc = '10'
                while opc != "3":
                    opc = str(input("\033[0;34mSUA PRÓXIMA AÇÃO: \n[1]\033[0;m GANHAR MAIS CARTA\n\033[0;34m[2]\033[0;m MANTER PONTUAÇÃO ATUAL\n\033[0;34m[3]\033[0;m DESISTIR DO JOGO\n\033[0;33m>> \033[0;m"))
                    if opc == "1":
                        print('>\n>\n>\nGANHANDO MAIS UMA CARTA...\n')
                        card3 = random.choice(numbers)
                        card_3 = random.choice(suits)
                        cartas.append(f"{card3}{card_3}")
                        pontos.append(card3)
                        print(f"Sua terceira carta foi: \033[0;41m{card3}{card_3}\033[0;m")
                        print(f'Suas cartas foram: \033[0;31m{cartas}\033[0;m')
                        print(f"O total da sua sequência atual é de: \033[0;33m{sum(pontos)} pontos\033[0;m\n")
                        continue
                    elif opc == "2":
                        print (f"Você escolheu ficar com a pontuação de: \033[0;33m{sum(pontos)} pontos\033[0;m\n")
                        print(f'Suas cartas foram: \033[0;31m{cartas}\033[0;m\n\n')
                        vercardBK = "2"
                        while vercardBK != "2":
                            vercardBK = str(input("CHEGOU A HORA DE VER A SEGUNDA CARTA DA BANCA...\nAPERTE [2] PARA PROSSEGUIR\n\033[0;33m>> \033[0;m"))
                        else:
                            cardBk2 = random.choice(numbers)
                            card_Bk2 = random.choice(suits)
                            print(f"A segunda carta da Banca foi: \033[0;44m{cardBk2}{card_Bk2}\033[0;m")
                            print(f"O total da sequencia da Banca é de: \033[0;33m{cardBk1+cardBk2} pontos\033[0;m\n")
                        break
                    elif opc == "3":
                        print(f"{tracinhofofo}\n                    QUE PENA QUE VOCÊ DESISTIU...\n{tracinhofofo}\n")
                        metade_da_aposta = int(self.aposta)/2
                        print(f"Você acaba de perder: \033[0;32mÐ {metade_da_aposta}\033[0;m da sua carteira")
                        print ("\nObrigado por jogar conosco, até a proxima!\n")
                        remover(self.email,metade_da_aposta)

                    else:
                        print('\033[0;31mOpção inválida!\033[0;m')
                        continue 
                print(f"\n{tracinhofofo}\n                                RESULTADO!\n{tracinhofofo}\n")
                playerpts = sum(pontos)
                dealerpts = (cardBk1+cardBk2)
                print(f'\033[0;33mVOCÊ\033[0;m ----------------- \033[0;33m{playerpts} PONTOS\033[0;m\n')
                print(f'\033[0;33mBANCA\033[0;m ---------------- \033[0;33m{dealerpts} PONTOS\033[0;m\n')

                if playerpts > 21:
                    print(f'☹ LAMENTO! ☹\nSua sequência ultrapassou 21 pontos!\nVocê acaba de perder: \033[0;32mÐ {self.aposta}\033[0;m')
                    print('\n \033[1;36m♣ ♦ ♥ ♠\033[0;m  \033[1;4;35mFIM DE JOGO!\033[0;m  \033[1;36m♣ ♦ ♥ ♠\033[0;m\n')
                    remover(self.email,self.aposta)

                elif playerpts > dealerpts and playerpts <= 21:
                    valor_duplicado = int(self.aposta)*2  
                    print(f'PARABÉNS! VOCÊ QUEBROU A BANCA\nVOCÊ É O VENCEDOR(a)!\n\nE acaba de ganhar mais: Ð {valor_duplicado} da Banca.\nNESSA JOGADA VOCÊ SAIU COM: \033[0;32mÐ {valor_duplicado}\033[0;m')
                    print('\n \033[1;36m♣ ♦ ♥ ♠\033[0;m  \033[1;4;35mFIM DE JOGO!\033[0;m  \033[1;36m♣ ♦ ♥ ♠\033[0;m\n')
                    aplicar(self.email,valor_duplicado)

                elif dealerpts > 21:
                    print(f'A BANCA QUEBROU!\nA sequencia dela ultrapassou 21 pontos!\n Você acaba de ganhar mais: Ð {self.aposta} da Banca.\nNESSA JOGADA VOCÊ SAIU COM: \033[0;32mÐ {valor_duplicado}\033[0;m')
                    print('\n \033[1;36m♣ ♦ ♥ ♠\033[0;m  \033[1;4;35mFIM DE JOGO!\033[0;m  \033[1;36m♣ ♦ ♥ ♠\033[0;m\n')
                    aplicar(self.email,valor_duplicado)

                elif dealerpts > playerpts and dealerpts <= 21:  
                    print(f'A BANCA TE VENCEU!\nVocê acaba de perder: \033[0;32mÐ {self.aposta}\033[0;m')
                    print('\n \033[1;36m♣ ♦ ♥ ♠\033[0;m  \033[1;4;35mFIM DE JOGO!\033[0;m  \033[1;36m♣ ♦ ♥ ♠\033[0;m\n')
                    remover(self.email,self.aposta)

                elif playerpts == dealerpts:
                    print('ORA ORA ORA... TIVEMOS UM EMPATE!\n(Cada um receberá metade do valor apostado)')
                    print(f'\nO VALOR APOSTADO FOI: \033[0;32mÐ {self.aposta} \033[0;m\n')
                    metade_da_aposta = int(self.aposta)/2
                    print(f'VOCÊ ----------------- \033[0;32mÐ {metade_da_aposta}\033[0;m\n')
                    print(f'BANCA ---------------- \033[0;32mÐ {metade_da_aposta}\033[0;m\n')
                    print('\n \033[1;36m♣ ♦ ♥ ♠\033[0;m  \033[1;4;35mFIM DE JOGO!\033[0;m  \033[1;36m♣ ♦ ♥ ♠\033[0;m\n')
                    aplicar(self.email,metade_da_aposta)  
            else:
                print(' \033[0;31mOPÇÃO INVÁLIDA!\033[0;m ')
                continue

