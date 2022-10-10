import sys
import random
import sqlite3
from ast import Str
from time import sleep
from sqlite3 import Error
from FUNÇOES import check,Senha,Dados
from colorama import Fore, Back, Style

normal = Fore.RESET

emailparamim = ''

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
                    jogo = Roleta("", 0, emailparamim, 'CASSINO (1).db', 'con', 'cursor')
                    jogo.inicio()
                    jogo.fichasEOpcoes()
                    return Menu_acesso(email) 
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
                        if linha[0] == 0:
                            sleep(1)
                            print ('EMAIL NÃO ENCONTRADO!')
                            print ('---------------------')
                            return Menu()
                        elif linha[0] == 1:
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
                                            global emailparamim
                                            emailparamim = vemail
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
                    print ('Opss! Email incorreto, retornado ao Menu.')
                    return Menu_acesso(email)
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
                    print ('Opss! Email incorreto, retornando ao Menu.')
                    return Menu_acesso(email)
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
                                                print ('Opss! Informe um valor real maior que 0.')
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
        print('\033[0;33m-------------------')
        print(" MOEDA       VALORES")
        print('  Ð ----------- 20')
        print('  Ð ----------- 50')
        print('  Ð ----------- 100')
        print('  Ð ----------- 500')
        print('  Ð ----------- 1000')    
        print('==================\033[0;m\n')
        aposta = "0"
        while aposta!='20' and aposta!='50'and aposta!='100'and aposta!='500'and aposta!='1000':
            aposta = str(input('Escolha algum valor da tabela para apostar\n\033[0;33m>> \033[0;m'))
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
                    remover(self.email,int(self.aposta))

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
                    remover(self.email,int(self.aposta))

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


class Roleta():
    valor = 0
    apostar = []
    def __init__(self, jogador:str, carteira:int, email:str, nomeconexao, variavelConexao, variavelCursor):
        self.jogador = jogador
        self.carteira = carteira
        self.email = email
        self.nomeconexao = nomeconexao
        self.variavelConexao = variavelConexao
        self.variavelCursor = variavelCursor
    def criar(self):
        self.variavelConexao = sqlite3.connect(self.nomeconexao)
        self.variavelConexao.execute("PRAGMA foreign_keys = 1")
        self.variavelCursor = self.variavelConexao.cursor()
        self.variavelCursor.execute('SELECT DINAR FROM CARTEIRA WHERE email=?', (emailparamim,))
        for linha in self.variavelCursor.fetchall():
            self.carteira = linha
            res = float(''.join(map(str, self.carteira)))
            self.carteira = res
    def mesa(self):
        a = Back.RED
        b = Back.BLACK
        no = Back.RESET
        letraPreta = Fore.RESET
        verde = Back.LIGHTGREEN_EX
        preto = Fore.BLACK
        print(" ___________________________________________________________________________________________"
              "\n|"+verde+"   "+no+"|"
              ,a,"3",no,
                 "|"
              ,b,"6",no,
                 "|"
              ,a,"9",no,
                 "|"
               ,a,"12",no,
                 "|"
              ,b,"15",no,
                 "|"
              ,a,"18",no,
                 "|"
              ,a,"21",no,
                 "|"
              ,b,"24",no,
                 "|"
              ,a,"27",no,
                 "|"
              ,a,"30",no,
                 "|"
              ,b,"33",no,
                 "|"
              ,a,"36",no,
                 "|"+verde+preto+" 2to1 "+no+letraPreta+"|"
              "\n|"+verde+preto+" 0 "+no+letraPreta+"|"
              ,b,"2",no,
                 "|"
              ,a,"5",no,
                 "|"
              ,b,"8",no,
                 "|"
              ,b,"11",no,
                 "|"
              ,a,"14",no,
                 "|"
              ,b,"17",no,
                 "|"
              ,b,"20",no,
                 "|"
              ,a,"23",no,
                 "|"
              ,b,"26",no,
                 "|"
              ,b,"29",no,
                 "|"
              ,a,"32",no,
                 "|"
              ,b,"35",no,
                 "|"+verde+preto+" 2to1 "+no+letraPreta+"|"
              "\n|"+verde+"   "+no+"|"
              ,a,"1",no,
                 "|"
              ,b,"4",no,
                 "|"
              ,a,"7",no,
                 "|"
              ,b,"10",no,
                 "|"
              ,b,"13",no,
                 "|"
              ,a,"16",no,
                 "|"
              ,a,"19",no,
                 "|"
              ,b,"22",no,
                 "|"
              ,a,"25",no,
                 "|"
              ,b,"28",no,
                 "|"
              ,b,"31",no,
                 "|"
              ,a,"34",no,
                "|"+verde+preto+" 2to1 "+no+letraPreta+"|"
              "\n -------------------------------------------------------------------------------------------"
              "\n    |"+verde+preto+"         1st 12         "+no+letraPreta+"|"+verde+preto+"           2nd 12          "+no+letraPreta+"|"+verde+preto+"          3rd 12           "+no+letraPreta+"|"
              "\n     ------------------------------------------------------------------------------- ",no,letraPreta,
              "\n    |"+verde+preto+"   1 - 18  "+no+letraPreta+"|"+verde+preto+"    EVEN    "+no+letraPreta+"|"+verde+preto+"     RED     "+no+letraPreta+"|"+verde+preto+"    BLACK    "+no+letraPreta+"|"+verde+preto+"     Odd     "+no+letraPreta+"|"+verde+preto+"   19 - 36   "+no+letraPreta+"|"
              "\n     --------------------------------------------------------------------------------")

    def inicio(self, primeiro:int=1):
        global cor
        print(f"Olá Jogador {self.jogador} e bem-vindo ao Jogo da Roleta"
              f"\nPara começar a jogar, primeiro escolha a sua cor:")
        sleep(0.5)
        print("[1]-Verde"
              "\n[2]-Vermelho"
              "\n[3]-Azul"
              "\n[4]-Amarelo"
              "\n[5]-Cinza"
              "\n[6]-Preto")
        while True:
            #Ver Depois
            escolha = str(input("Digite a cor da sua escolha aqui: "))
            try:
                global cor
                if escolha == "1" or escolha == "verde":
                    cor = Fore.GREEN
                    print("Cor escolhida")
                    break
                elif escolha == "2" or escolha == "vermelho":
                    cor = Fore.RED
                    print("Cor escolhida")
                    break
                elif escolha == "3" or escolha == "azul":
                    cor = Fore.BLUE
                    print("Cor escolhida")
                    break
                elif escolha == "4" or escolha == "amarelo":
                    cor = Fore.YELLOW
                    print("Cor escolhida")
                    break
                elif escolha == "5" or escolha == "cinza":
                    cor = Fore.CYAN
                    print("Cor escolhida")
                    break
                elif escolha == "6" or escolha == "Preto":
                    cor = Fore.BLACK
                    print("Cor escolhida")
                    break
                else:
                    print(Fore.RED+"Nenhuma cor foi escolhida, Digite um valor valido"+normal)
            except Exception is SyntaxError:
                print()
    def multiplicadores(self):
        multiplicadores = [50, 100, 500]
        self.valor_amplificador1 = 1
        self.valor_amplificador2 = 1
        self.valor_amplificador3 = 1
        self.valor_amplificador4 = 1
        self.lugar_aplificador1 = 0
        self.lugar_aplificador2 = 0
        self.lugar_aplificador3 = 0
        self.lugar_aplificador4 = 0
        qtda_amplificador = random.randint(1, 4)
        if qtda_amplificador == 1:
            self.valor_amplificador1 = random.choice(multiplicadores)
            self.lugar_aplificador1 = random.randint(0, 36)
            print(
                Fore.LIGHTMAGENTA_EX + f"\nHá um numero amplificado em {self.valor_amplificador1}x na casa {self.lugar_aplificador1}" + normal)
        elif qtda_amplificador == 2:
            self.valor_amplificador1 = random.choice(multiplicadores)
            self.lugar_aplificador1 = random.randint(0, 36)
            self.valor_amplificador2 = random.choice(multiplicadores)
            self.lugar_aplificador2 = random.randint(0, 36)
            print(
                Fore.LIGHTMAGENTA_EX + f"Há um numero amplificado em {self.valor_amplificador1}x na casa {self.lugar_aplificador1}" + normal)
            print(
                Fore.GREEN + f"Há um numero amplificado em {self.valor_amplificador2}x na casa {self.lugar_aplificador2}" + normal)
        elif qtda_amplificador == 3:
            self.valor_amplificador1 = random.choice(multiplicadores)
            self.lugar_aplificador1 = random.randint(0, 36)
            self.valor_amplificador2 = random.choice(multiplicadores)
            self.lugar_aplificador2 = random.randint(0, 36)
            self.valor_amplificador3 = random.choice(multiplicadores)
            self.lugar_aplificador3 = random.randint(0, 36)
            print(
                Fore.LIGHTMAGENTA_EX + f"Há um numero amplificado em {self.valor_amplificador1}x na casa {self.lugar_aplificador1}" + normal)
            print(
                Fore.GREEN + f"Há um numero amplificado em {self.valor_amplificador2}x na casa {self.lugar_aplificador2}" + normal)
            print(
                Fore.LIGHTYELLOW_EX + f"Há um numero amplificado em {self.valor_amplificador3}x na casa {self.lugar_aplificador3}" + normal)
        elif qtda_amplificador == 4:
            self.valor_amplificador1 = random.choice(multiplicadores)
            self.lugar_aplificador1 = random.randint(0, 36)
            self.valor_amplificador2 = random.choice(multiplicadores)
            self.lugar_aplificador2 = random.randint(0, 36)
            self.valor_amplificador3 = random.choice(multiplicadores)
            self.lugar_aplificador3 = random.randint(0, 36)
            self.valor_amplificador4 = random.choice(multiplicadores)
            self.lugar_aplificador4 = random.randint(0, 36)
            print(
                Fore.LIGHTMAGENTA_EX + f"Há um numero amplificado em {self.valor_amplificador1}x na casa {self.lugar_aplificador1}" + normal)
            print(
                Fore.GREEN + f"Há um numero amplificado em {self.valor_amplificador2}x na casa {self.lugar_aplificador2}" + normal)
            print(
                Fore.LIGHTYELLOW_EX + f"Há um numero amplificado em {self.valor_amplificador3}x na casa {self.lugar_aplificador3}" + normal)
            print(
                Fore.CYAN + f"Há um numero amplificado em {self.valor_amplificador4}x na casa {self.lugar_aplificador4}" + normal)
        else:
            print("\nNão há nenhum numero Amplificado")

    def jogo(self, valorFicha):
        tentativa = 0
        tamanho = 0
        true = True
        self.criar()
        while true:
            print("\nDeseja fazer que tipo(s) de aposta"
                  "\n[1]-Interna"
                  "\n[2]-Externa"
                  "\n[3]-Encerrar Programa")
            jogada = str(input("\nDigite uma opção: "))
            try:
                jogada = int(jogada)
            except:
                print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
            else:
                true = False
        #Aposta Interna
        if jogada == 1:
            self.criar()
            self.multiplicadores()
            tentativa = 0
            sim = True
            quantidade = 0
            aq = 0
            c = 0
            while True:
                print(f"\nDigite em quantas casas deseja apostar")
                try:
                    quantidade = int(input("Digite aqui um valor maior ou igual a zero e menor que 36: "))
                    if 0 > quantidade or quantidade > 36:
                        print("Valor Muito Alto/Baixo, Favor Digitar Novamente")
                    else:
                        self.variavelCursor.execute('SELECT DINAR FROM CARTEIRA WHERE email = ?', (emailparamim,))
                        for linha in self.variavelCursor.fetchall():
                            coisa = float(''.join(map(str, linha)))
                            if quantidade * valorFicha > coisa:
                                print(f"A quantidades de vezes n bate com o valor da sua carteira")
                                sim = False
                            else:
                                sim = True
                        if sim == True:
                            break
                except:
                    print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
            while c < quantidade:
                print("\nDigite a casa(s) que deseja de 0-36")
                casa = str(input("Casa nº: "))
                try:
                    casa = int(casa)
                except:
                    print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                    continue
                if tentativa == 0:
                    if casa > 36 or casa < 0:
                        print(Fore.RED+"\nValor muito alto ou muito baixo, favor digitar o valor Corretamente"+normal)
                        continue
                    self.apostar.append(casa)
                    tentativa += 1
                    c += 1
                elif tentativa == 1:
                    if casa > 36 or casa < 0:
                        print(Fore.RED+"Valor muito alto ou muito baixo, favor digitar o valor Corretamente"+normal)
                        continue
                    aq = 0
                    for indice in range(0, len(self.apostar)):
                        if self.apostar[indice] == casa:
                            print(f"Valor Já existe, favor digitar novamente um valor valido")
                            aq += 1
                            break
                    if aq == 0:
                        self.apostar.append(casa)
                        c += 1
                    elif aq >= 1:
                        continue
            randomizador = random.randint(0, 36)
            perdeu = 0
            print(self.carteira)
            print(f"O numero sorteado foi o {randomizador}")
            for i in range(0, len(self.apostar)):
                if self.lugar_aplificador1 == self.apostar[i] and self.apostar[i] == randomizador:
                    self.carteira += valorFicha * self.valor_amplificador1
                    print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * self.valor_amplificador1} com um amplificador de {self.valor_amplificador1}x")
                    self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                    self.variavelConexao.commit()
                    perdeu += 1
                elif self.lugar_aplificador2 == self.apostar[i] and self.apostar[i] == randomizador:
                    self.carteira += valorFicha * self.valor_amplificador2
                    print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * self.valor_amplificador2} com um amplificador de {self.valor_amplificador2}x")
                    self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                    self.variavelConexao.commit()
                    perdeu += 1
                elif self.lugar_aplificador3 == self.apostar[i] and self.apostar[i] == randomizador:
                    self.carteira += valorFicha * self.valor_amplificador3
                    print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * self.valor_amplificador3} com um amplificador de {self.valor_amplificador3}x")
                    self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                    self.variavelConexao.commit()
                    perdeu += 1
                elif self.lugar_aplificador4 == self.apostar[i] and self.apostar[i] == randomizador:
                    self.carteira += valorFicha * self.valor_amplificador4
                    print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * self.valor_amplificador4} com um amplificador de {self.valor_amplificador4}x")
                    self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                    self.variavelConexao.commit()
                    perdeu += 1
                elif self.apostar[i] == randomizador:
                    self.carteira += (valorFicha * (36 / quantidade))
                    print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * (36 / quantidade)}")
                    self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                    self.variavelConexao.commit()
                    perdeu += 1
            if perdeu == 0:
                print("\nVocê Perdeu")
                self.carteira -= valorFicha
                self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                self.variavelConexao.commit()


        elif jogada == 2:
            self.variavelCursor.execute('SELECT DINAR FROM CARTEIRA WHERE email = ?', (emailparamim,))
            for linha in self.variavelCursor.fetchall():
                coisa = float(''.join(map(str, linha)))
                if coisa < valorFicha:
                    print(f"O dinheiro da sua carteira é muito baixo para fazer qualquer tipo de aposta nesse valor de ficha"
                          f"SAINDO DO CASSINO")
                    quit()
            print("\nQual a jogada externa deseja fazer"
                  "\n[1]-Colunas"
                  "\n[2]-Duzias"
                  "\n[3]-Cor"
                  "\n[4]-Par/Impar"
                  "\n[5]-1-18/19-36")
            while True:
                responda = str(input("\nDigite aqui: "))
                try:
                    responda = int(responda)
                except:
                    print("Digite um valor válido")
                else:
                    break
            if responda == 1:
                self.criar()
                colunas = [[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36], [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
                           [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Coluna Você deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Primeira Coluna (3,6...)"
                          f"\n[2]-Para a Segunda Coluna (2,5...)"
                          f"\n[3]-Para a Terceira Coluna (1,4...)")
                    try:
                        digite = int(input("\nEscolha a sua coluna: "))
                        if digite > 3 or digite <= 0:
                            continue
                    except:
                        print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 12):
                    if colunas[digite][l] == randomizador:
                        self.carteira += valorFicha * 3
                        print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * 3}")
                        self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                        self.variavelConexao.commit()
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Você Perdeu, o dinheiro que você perdeu nessa aposta foi de R${valorFicha}")
                    self.carteira -= valorFicha
                    self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                    self.variavelConexao.commit()

            elif responda == 2:
                self.criar()
                duzia = [[1,2,3,4,5,6,7,8,9,10,11,12], [13,14,15,16,17,18,19,20,21,22,23,24], [25,26,27,28,29,30,31,32,33,34,35,36]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Duzia Você deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Primeira Duzia"
                          f"\n[2]-Para a Segunda Duzia"
                          f"\n[3]-Para a Terceira Duzia")
                    try:
                        digite = int(input("\nEscolha a sua duzia: "))
                        if digite > 3 or digite <= 0:
                            continue
                    except:
                        print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 12):
                    if duzia[digite][l] == randomizador:
                        self.carteira += valorFicha * 3
                        print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * 3}")
                        self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                        self.variavelConexao.commit()
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Você Perdeu, o dinheiro que você perdeu nessa aposta foi de R${valorFicha}")
                    self.carteira -= valorFicha
                    self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                    self.variavelConexao.commit()

            elif responda == 3:
                self.criar()
                cor = [[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35], [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Cor Você deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Cor Preta"
                          f"\n[2]-Para a Cor Vermelha")
                    try:
                        digite = int(input("\nEscolha a sua cor: "))
                        if digite > 2 or digite <= 0:
                            continue
                    except:
                        print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 18):
                    if cor[digite][l] == randomizador:
                        self.carteira += valorFicha * 2
                        print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * 2}")
                        self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                        self.variavelConexao.commit()
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Você Perdeu, o dinheiro que você perdeu nessa aposta foi de R${valorFicha}")
                    self.carteira -= valorFicha
                    self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                    self.variavelConexao.commit()

            elif responda == 4:
                self.criar()
                conjuntos = [[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36],
                       [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Escolha Você deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Par"
                          f"\n[2]-Para a Impar")
                    try:
                        digite = int(input("\nEscolha Par ou Impar: "))
                        if digite > 2 or digite <= 0:
                            continue
                    except:
                        print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 18):
                    if conjuntos[digite][l] == randomizador:
                        self.carteira += valorFicha * 2
                        print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * 2}")
                        self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                        self.variavelConexao.commit()
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Você Perdeu, o dinheiro que você perdeu nessa aposta foi de R${valorFicha}")
                    self.carteira -= valorFicha
                    self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                    self.variavelConexao.commit()

            elif responda == 5:
                self.criar()
                altos = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
                             [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Escolha Você deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Numeros Baixos (1-18)"
                          f"\n[2]-Para a Numeros Altos (19-36)")
                    try:
                        digite = int(input("\nEscolha Alto ou Baixo: "))
                        if digite > 2 or digite <= 0:
                            continue
                    except:
                        print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 18):
                    if altos[digite][l] == randomizador:
                        self.carteira += valorFicha * 2
                        print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * 2}")
                        self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                        self.variavelConexao.commit()
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Você Perdeu, o dinheiro que você perdeu nessa aposta foi de R${valorFicha}")
                    self.carteira -= valorFicha
                    self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email= ?',(self.carteira, emailparamim))
                    self.variavelConexao.commit()


        elif jogada == 3:
            print("Obrigado por jogar o nosso jogo")
            print("Tenha um otimo dia")
            quit()







    def fichasEOpcoes(self):
        sim = True
        true = True
        while true:
            print("\n"+ "-=" * 100)
            print(f"Agora está na hora de apostar, e por isso lhe daremos duas opções a partir daqui:"
                  f"\n1-Livro de Regras"
                  f"\n2-Jogar"
                  f"\n3-Encerrar Programa")
            n = str(input("Qual você escolhe: ")).lower()
            try:
                n = str(n)
            except:
                print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                continue
            #Regras de Apostas
            if n == "1" or n == "livro de regras":
                print("\nA roleta que é jogada aqui é a roleta europeia, que conta com 37 numeros na roleta."
                      "\n"
                      "\nA roleta na Roleta European contém 37 posições, numeradas de zero a 36. Isso significa que os jogadores são ofertados com melhores \nprobabilidades do que em outras mesas de roleta, como a Americana, que tem mais posições."
                      "\nAs duas principais seções da mesa nas quais as apostas são colocadas são a 'seção interna' e a 'seção externa'. Cada uma com diversas \nformas diferentes para apostar."
                      "\nA seção interna oferece apostas em números individuais que estão próximos um do outro no layout da mesa, ou grupos de até seis números."
                      "\nA seção externa contém pares de apostas para vermelho ou preto, alto ou baixo e par ou ímpar (cada uma cobrindo 18 números). Você também \npode fazer seis diferentes apostas de 12 números (três de cada, conhecidas como apostas de 'Coluna' e 'Dúzia')."
                      "\nAlém disso, existem grupos de apostas que abrangem de sete a 17 números, localizadas em diferentes segmentos da roleta. Estas apostas \npodem ser colocadas com um simples clique na 'racetrack', a parte do layout da mesa de roleta que representa a roleta verdadeira \ne a ordem na qual os números são mostrados, em vez da ordem numérica do layout de apostas principal."
                      "\n"
                      "\nO Jogo e as Regras do Jogo"
                      "\nUma vez que entrar na mesa, cada jogador é solicitado a selecionar uma cor de ficha para utilizar durante a sessão. Você pode então \nselecionar facilmente o valor das fichas ao colocar as apostas, e variar o número colocado de uma vez em uma determinada área de aposta."
                      "\nAcompanhamos automaticamente os valores apostados, e não permitirá que apostas abaixo do limite mínimo da mesa sejam colocadas. Se o \nvalor nominal escolhido for menor do que o mínimo permitido, o seu primeiro clique na área de apostas irá colocar a aposta mínima da mesa."
                      "\nUtilizando apostas internas ou externas, você pode apostar em qualquer número, ou combinação de números. Lembre-se que cada aposta \nexterna deve ser de pelo menos o valor do mínimo da mesa; a mesma regra se aplica ao total apostado nas apostas internas. \nLembre-se também que cada uma é independente da outra em relação ao mínimo da mesa."
                      "\nPara as apostas ganhadoras, a aposta original é retornada para a sua conta, mais o pagamento que você recebe baseado no valor investido \ne as informações das probabilidades (relacionada abaixo). As apostas perdedoras serão perdidas."
                      "\nO software reconhece automaticamente que as apostas internas são acumulativas, assim as apostas podem ser colocadas na seção interna \nda mesa até que o mínimo seja atingido. Caso ele não seja atingido, as apostas abaixo do mínimo serão removidas quando a roleta for girada (depois que o cronômetro de apostas encerrar)."
                      "\nAo jogar em uma mesa de Jogadores Múltiplos, todas as apostas serão elegíveis a ganhar ou perder uma vez que o cronômetro de apostas \nencerrar. Nas mesas de Jogador Único, as apostas não serão consideradas ativas até que a ação seja confirmada e o botão Girar tenha sido clicado."
                      "\n"
                      "\n                 Pagamento das Apostas Internas - Roleta"
                      "\nNome Da Aposta         Números Cobertos           Probabilidade de Pagamento"
                      "\n Pleno                        1                             35 para 1"
                      "\n Dividir                      2                             17 para 1"
                      "\n Linha                        3                             11 para 1"
                      "\n Quadrado                     4                             8 para 1"
                      "\n Linha Dupla                  6                             5 para 1"
                      "\n"
                      "\n                 Pagamento Das Apostas Externas - Roleta"
                      "\nNome Da Aposta         Números Cobertos           Probabilidade de Pagamento"
                      "\n Vermelho                     18                            1 para 1"
                      "\n Preto                        18                            1 para 1"
                      "\n Ímpar                        18                            1 para 1"
                      "\n Par                          18                            1 para 1"
                      "\n Baixo(1-18)                  18                            1 para 1"
                      "\n Alto(19-36                   18                            1 para 1"
                      "\n 1ª, 2ª ou 3ª duzia           12                            2 para 1"
                      "\n 1ª, 2ª ou 3ª coluna          12                            2 para 1"
                      "\n"
                      "\nApostas Divididas e Racetrack"
                      "\nAlém das seções Interna e Externa, as apostas também podem ser colocadas na área 'racetrack' da mesa. Esta seção do layout da mesa de \nroleta representa a ordem real que os números aparecem na própria roleta. Clique em um dos números para colocar fichas nele, \nmais os dois números adjacentes (conhecidos como 'vizinhos') dos dois lados deste número."
                      "\nA 'racetrack' pode ser utilizada para colocar outras quatro apostas especiais, cada qual coloca automaticamente várias fichas no layout,\n como mostrado na tabela a seguir."
                      "\n"
                      "\nNome Da Aposta         Custo Da Ficha          Números Cobertos                              Distribuição"
                      "\n Vizinhos do Zero       Nove Fichas                   17                              0/2/3 (duas fichas), 4/7, 12/15, 18/21, 19/22, 25/26/28/29 (duas fichas), 32/35"
                      "\n Terço da Roleta        Seis Fichas                   12                              5/8, 10/11, 13/16, 23/24, 27/30, 33/36"
                      "\n Orphelins en Plein     Oito Fichas                   8                               1, 6, 9, 14, 17, 20, 31, 34"
                      "\n Zero                   Quatro Fichas                 7                               0/3, 12/15, 26, 32/35"
                      "\n"
                      "\nApostas em dois números adjacentes (divididos) da mesma cor no layout principal (ex. vermelho ou preto) podem ser apostadas em uma ação\n utilizando os controles para apostas divididas encontrados perto da área 'racetrack' da mesa."
                      "\n"
                      "\nDivididos Vermelhos(Quatro Apostas)                   Divididos Pretos(Sete Apostas)"
                      "\n 9/12                                                          8/11"
                      "\n 16/19                                                         10/11"
                      "\n 18/21                                                         10/13"
                      "\n 27/30                                                         17/20"
                      "\n                                                               26/29"
                      "\n                                                               28/29"
                      "\n                                                               28/31"
                      "\n"
                      "\nLimites De Apostas"
                      "\nSeguindo uma convenção semelhante à maioria dos cassinos modernos em todo o mundo, os limites de apostas nas mesas de roleta variam, \ndependendo se elas cobrem as apostas internas ou externas."
                      "\nA aposta externa máxima exibida em cada mesa indica o maior valor que pode ser colocado em cada (ou todas) as posições de apostas externas. Não existe um máximo acumulativo."
                      "\nA aposta interna máxima de uma mesa se refere ao valor permitido para ser colocado em cada aposta de número individual (ou direta)."
                      "\nTodos os outros tipos de apostas internas (por exemplo a dividida, linha dupla, linha, etc.) têm o seu próprio valor máximo de aposta, \nrelativo ao máximo do direto da mesa. A regra geral é que quanto mais números forem cobertos por uma aposta, maiores serão os limites. \nPor exemplo, uma aposta Pleno cobre um número e a aposta máxima pode ser de 25 fichas. Uma aposta Dividida cobre dois números e assim o dobro do máximo é permitido (50 fichas). \nUma aposta de Linha cobre três números e neste exemplo a aposta máxima seria de 75 fichas, e assim por diante."
                      "\nEm uma mesa com um limite de aposta máxima no pleno de 25 fichas, é possível colocar até 40 apostas de 25 fichas em torno de um número \nposicionado na coluna do meio do layout, como o 17 (apostas em um pleno (1), quatro divididos (8), uma linha (3), quatro quadrados (16), e duas linhas duplas (12), para um total de 1.000 fichas."
                      "\n"
                      "\nVantagem Da Casa"
                      "\nOs jogos de Roleta têm uma vantagem da casa (calculada como a diferença entre as probabilidades reais e as probabilidades de pagamento) de 2,70%."
                      "\nOs jogos de American Roulette têm uma vantagem da casa de 5,26%. A aposta Five Line na American Roulette tem uma vantagem da casa de 7,89%."
                      "\n"
                      "\nApostas Salvas"
                      "\nEm mesas de Jogador Único, é possível salvar suas apostas favoritas, então você pode fazer apostas de combinação específica de forma rápida e conveniente. \nSelecione ‘Salvar Aposta Atual’ para adicioná-la aos seus favoritos. Você pode gerenciar apostas salvas no menu ‘Minhas Apostas’."
                      "\n"
                      "\nMesas De Jogadores Múltiplos"
                      "\nAs Mesas de Jogadores Múltiplos oferecem a você e seus amigos a oportunidade de jogarem juntos e aproveitar a emoção de um jogo social. Exatamente como nos cassinos da vida real, \nas mesas de Jogadores Múltiplos transformam o jogo online em uma experiência interativa divertida.")
            elif n == "2" or n == "jogar":
                self.criar()
                self.mesa()
                sleep(1.5)
                while true:
                    print(cor+f"\nEscolha a sua ficha"
                          f"\n[1]-R$0.5"
                          f"\n[2]-R$2.5"
                          f"\n[3]-R$5"
                          f"\n[4]-R$25"
                          f"\n[5]-R$100"
                          f"\n[6]-R$500"
                          f"\n[7]-R$2K"
                          f"\n[8]-R$5K"
                          f"\n[9]-Encerrar Programa"+normal)
                    fichas = str(input("\nDigite: "))
                    try:
                        fichas = int(fichas)
                    except:
                        print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                        continue
                    if fichas == 1:
                        self.valor = 0.5
                        self.variavelCursor.execute('SELECT DINAR FROM CARTEIRA WHERE email = ?', (emailparamim,))
                        for linha in self.variavelCursor.fetchall():
                            coisa = float(''.join(map(str, linha)))
                            if coisa < self.valor:
                                print(f"Você n tem o dinheiro necessario para fazer esse tipo de jogada")
                                sim = False
                            else:
                                sim = True
                        if sim == True:
                            self.jogo(self.valor)
                    elif fichas == 2:
                        self.valor = 2.5
                        self.variavelCursor.execute('SELECT DINAR FROM CARTEIRA WHERE email = ?', (emailparamim,))
                        for linha in self.variavelCursor.fetchall():
                            coisa = float(''.join(map(str, linha)))
                            if coisa < self.valor:
                                print(f"Você n tem o dinheiro necessario para fazer esse tipo de jogada")
                                sim = False
                            else:
                                sim = True
                        if sim == True:
                            self.jogo(self.valor)
                    elif fichas == 3:
                        self.valor = 5
                        self.variavelCursor.execute('SELECT DINAR FROM CARTEIRA WHERE email = ?', (emailparamim,))
                        for linha in self.variavelCursor.fetchall():
                            coisa = float(''.join(map(str, linha)))
                            if coisa < self.valor:
                                print(f"Você n tem o dinheiro necessario para fazer esse tipo de jogada")
                                sim = False
                            else:
                                sim = True
                        if sim == True:
                            self.jogo(self.valor)
                    elif fichas == 4:
                        self.valor = 25
                        self.variavelCursor.execute('SELECT DINAR FROM CARTEIRA WHERE email = ?', (emailparamim,))
                        for linha in self.variavelCursor.fetchall():
                            coisa = float(''.join(map(str, linha)))
                            if coisa < self.valor:
                                print(f"Você n tem o dinheiro necessario para fazer esse tipo de jogada")
                                sim = False
                            else:
                                sim = True
                        if sim == True:
                            self.jogo(self.valor)
                    elif fichas == 5:
                        self.valor = 100
                        self.variavelCursor.execute('SELECT DINAR FROM CARTEIRA WHERE email = ?', (emailparamim,))
                        for linha in self.variavelCursor.fetchall():
                            coisa = float(''.join(map(str, linha)))
                            if coisa < self.valor:
                                print(f"Você n tem o dinheiro necessario para fazer esse tipo de jogada")
                                sim = False
                            else:
                                sim = True
                        if sim == True:
                            self.jogo(self.valor)
                    elif fichas == 6:
                        self.valor = 500
                        self.variavelCursor.execute('SELECT DINAR FROM CARTEIRA WHERE email = ?', (emailparamim,))
                        for linha in self.variavelCursor.fetchall():
                            coisa = float(''.join(map(str, linha)))
                            if coisa < self.valor:
                                print(f"Você n tem o dinheiro necessario para fazer esse tipo de jogada")
                                sim = False
                            else:
                                sim = True
                        if sim == True:
                            self.jogo(self.valor)
                    elif fichas == 7:
                        self.valor = 2000
                        self.variavelCursor.execute('SELECT DINAR FROM CARTEIRA WHERE email = ?', (emailparamim,))
                        for linha in self.variavelCursor.fetchall():
                            coisa = float(''.join(map(str, linha)))
                            if coisa < self.valor:
                                print(f"Você n tem o dinheiro necessario para fazer esse tipo de jogada")
                                sim = False
                            else:
                                sim = True
                        if sim == True:
                            self.jogo(self.valor)
                    elif fichas == 8:
                        self.valor = 5000
                        self.variavelCursor.execute('SELECT DINAR FROM CARTEIRA WHERE email = ?', (emailparamim,))
                        for linha in self.variavelCursor.fetchall():
                            coisa = float(''.join(map(str, linha)))
                            if coisa < self.valor:
                                print(f"Você n tem o dinheiro necessario para fazer esse tipo de jogada")
                                sim = False
                            else:
                                sim = True
                        if sim == True:
                            self.jogo(self.valor)
                    elif fichas == 9:
                        print("\nObrigado por jogar o nosso jogo")
                        print("Tenha um otimo dia")
                        quit()
            elif n == '3':
                print("\nObrigado por jogar o nosso jogo")
                print("Tenha um otimo dia")
                quit()
            else:
                print(f"Digite um valor válido")
