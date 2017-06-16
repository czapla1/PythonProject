# -*- coding: utf-8 -*-


import pymysql
from mod_admin import *



class MenuDB:
    def __init__(self,login, haslo):
        self.conn = pymysql.connect("localhost", "root", "kwiat23", "bookshop") 
        self.cursor = self.conn.cursor() 
        self.login=login
        self.haslo=haslo
        self.logowanie()
    def logowanie(self):
        self.sql1= "select * from login where login=%s and passwort=%s and priviliges='user'"
        self.cursor.execute(self.sql1, (self.login, self.haslo))
        if(self.cursor.rowcount ==1):
            print('Poprawne logowanie do panelu użytkownika ')
            o2=User() 
            
        else:
            self.sql2= "select * from login where login=%s and passwort=%s and priviliges='admin'"
            self.cursor.execute(self.sql2, (self.login, self.haslo))
            if(self.cursor.rowcount ==1):
                print('Poprawne logowanie do panelu administratora')
                o3=Admin()
            else:
                print('Niepoprawny login lub hasło')
      
         
o1=MenuDB(input('Podaj login: '),input('Podaj haslo: '))
