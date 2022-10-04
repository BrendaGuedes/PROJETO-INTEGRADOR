import sqlite3
from sqlite3 import Error

email = 'teteu@gmail.com'
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
            opc = 0
            while opc!=1:
                senha = str(input('SENHA:'))
                cursor.execute('SELECT COUNT(email),senha FROM JOGADORES WHERE email=?',(self.email,))
                for linha in cursor.fetchall():
                    if linha[1] == senha:
                        while True:
                            try:
                                valor = int(input("SACAR:"))
                            except ValueError:
                                print("Oops! Número inválido...")
                                continue
                            else: 
                                cursor.execute('SELECT DINAR FROM CARTEIRA WHERE email=?',(self.email,))
                                for vlinha in cursor.fetchall():
                                    x = vlinha[0]
                                    if valor >x:
                                        print('SACAR, não pode ser executado Ð insuficiente.')
                                        return Menu_acesso
                                    if valor <=x:
                                        print('PROCESSANDO')
                                        x-=valor
                                        cursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email=?',(x,self.email))
                                        con.commit()
                                        print ('- VALOR REMOVIDO DE CARTEIRA -')
                                        return Menu_acesso
                    else:
                        print('ACESSO NEGADO')
                        continue 

    def Depositar(self):
        try:
            con = sqlite3.connect ('CASSINO (1).db')
            con.execute('PRAGMA foreign_keys = 1') 
            cursor = con.cursor()
        except Error as ex:
            print (ex)
        else:
            opc = 0
            while opc!=1:
                senha = str(input('SENHA:'))
                cursor.execute('SELECT COUNT(email),senha FROM JOGADORES WHERE email=?',(f"{self.email}",))
                for linha in cursor.fetchall():
                    if linha[1] == senha:
                        while True:
                            try:
                                valor = int(input("DEPOSITAR:"))
                            except ValueError:
                                print("Oops! Número inválido...")
                                continue
                            else: 
                                cursor.execute('SELECT DINAR FROM CARTEIRA WHERE email=?',(self.email,))
                                for vlinha in cursor.fetchall():
                                    x = vlinha[0]             
                                    x += valor
                                cursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email=?',(x,self.email))
                                con.commit()
                                print ('- VALOR ADICIONADO A CARTEIRA -')
                                return Menu_acesso
                    else:
                        print('ACESSO NEGADO')
                        continue
