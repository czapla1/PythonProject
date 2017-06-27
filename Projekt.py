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
        self.sql1= "select id_customer,priviliges from login where login=%s and passwort=%s"
        self.cursor.execute(self.sql1, (self.login, self.haslo))
        if(self.cursor.rowcount ==1):
            row=self.cursor.fetchone()
            if row[1]=="user":
                print('Poprawne logowanie do panelu użytkownika ')
                o2=User(row[0]) 
            else:
            
                print('Poprawne logowanie do panelu administratora')
                o3=Admin(row[0])
        else:
            print('Niepoprawny login lub hasło')
            o1=MenuDB(input('Podaj login: '),input('Podaj haslo: '))
            
o1=MenuDB(input('Podaj login: '),input('Podaj haslo: '))
