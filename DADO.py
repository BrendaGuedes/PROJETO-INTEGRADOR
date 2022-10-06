import random
import sqlite3
from sqlite3 import Error
from time import sleep

def Verificar(email):
        try:
            con = sqlite3.connect ('CASSINO (1).db')
            con.execute('PRAGMA foreign_keys = 1') 
            cursor = con.cursor()
        except Error as ex:
            print (ex)
        else:
            print('==================')
            print("      APOSTAS     ")
            print('==================')
            print("      VALORES     ")
            print('       Ð:5        ')
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
                    if aposta!=5 and aposta!= 20 and aposta!= 50 and aposta!= 100 and aposta!= 150:
                        print ('Opss! Requirimos que utilize os valoes dentro da tabela!')
                        continue
                    cursor.execute('SELECT DINAR FROM CARTEIRA WHERE email=?',(email,))
                    for vlinha in cursor.fetchall():
                        x = vlinha[0]
                        if x>= aposta:
                            return aposta 
                        if x <aposta:
                            print('APOSTA, não pode ser executado Ð insuficiente.')
                            return Menu_acesso(email)

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
        print ('- VALOR ADICIONADO A CARTEIRA -')
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

def Guia(email):
        try:
            con = sqlite3.connect ('CASSINO (1).db')
            con.execute('PRAGMA foreign_keys = 1') 
            cursor = con.cursor()
        except Error as ex:
            print (ex)
        else:
            print ('ºººººººººººººººººººººººººººººººººººº')
            print ('               DADOS                ')
            print ('ºººººººººººººººººººººººººººººººººººº')
            print ('O objetivo do jogo é simples você poderá apostar um valor de sua escolha, escolhera os números para representar a sua aposta e os dados \nsortearam valores aleatórios para sobrepor os números da sua aposta, se o valor sorteado e os números da sua aposta forem equivalentes.\nParabéns,você recebera o valor da sua aposta duplicado ou até mesmo quadruplicado.\nSenão você poderá tentar novamente por uma nova opurtunidade de turbinar sua carteira.')
            sleep(1)
            print ('- DIFICULDADE -')
            print ('[1]Facíl\n 2 Dados serão usados para sobreposição do valor! Isso duplica sua aposta.')
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
                    pass 
                if fase =='3':
                    conta1= Dado(email,Verificar(email))
                    conta1.Dificil()
                    pass 
                else: 
                    print(' AÇÃO INVÁLIDA ')
                    continue

class Dado:
    def __init__(self,email,aposta) -> None:
        self.email = email 
        self.aposta = aposta 

    def Facil(self):
        print(' DICA: Os dados sortedos contém 6 lados, a soma total desses dados podem chegar até 12. Então escolha por números que sejam iguais a 12 ou menores que 12.')
        while True:
            try:
                valor1 = int(input("NÚMERO PARA REPRESENTAR A APOSTA:"))
            except ValueError:
                print("Opss! Inválido...")
                continue
            else:
                while True:
                    try:
                        valor2 = int(input("NÚMERO PARA REPRESENTAR A APOSTA:"))
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
        print (' DICA: Os dados sortedos contém 12 lados, a soma total desses dados podem chegar até 36. Então escolha por números que sejam iguais ou menores que 36.')
        while True:
            try:
                valor1 = int(input("NÚMERO PARA REPRESENTAR A APOSTA:"))
            except ValueError:
                print("Opss! Inválido...")
                continue
            else:
                while True:
                    try:
                        valor2 = int(input("NÚMERO PARA REPRESENTAR A APOSTA:"))
                    except ValueError:
                        print("Opss! Inválido...")
                        continue
                    else:
                        while True:
                            try:
                                valor3 = int(input("NÚMERO PARA REPRESENTAR A APOSTA:"))
                            except ValueError:
                                print("Opss! Inválido...")
                                continue
                            else: 
                                tupla_vazia = ()
                                tupla_vazia = valor1, valor2, valor3 
                                print (f'\033[31mO jogador escolheu os números {tupla_vazia[0]}, {tupla_vazia[1]}, {tupla_vazia[2]}  para representar sua aposta.') 
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
        print (' DICA: Os dados sortedos contém 12 lados, a soma total desses dados podem chegar até 60. Então escolha por números que sejam iguais ou menores que 60.')
        while True:
            try:
                valor1 = int(input("NÚMERO PARA REPRESENTAR A APOSTA:"))
            except ValueError:
                print("Opss! Inválido...")
                continue
            else:
                while True:
                    try:
                        valor2 = int(input("NÚMERO PARA REPRESENTAR A APOSTA:"))
                    except ValueError:
                        print("Opss! Inválido...")
                        continue
                    else:
                        while True:
                            try:
                                valor3 = int(input("NÚMERO PARA REPRESENTAR A APOSTA:"))
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
