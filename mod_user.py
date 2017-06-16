# -*- coding: utf-8 -*-
import pymysql

class User:
    def __init__(self):
        self.conn = pymysql.connect("localhost", "root", "kwiat23", "bookshop") 
        self.cursor = self.conn.cursor() 
        self.menu1()
           
    def menu1(self):
        self.i =input('\nKtórą tabelę chcesz wybrać?: \n(1)-Dane kontaktowe, \n(2)-Ostatnie zamówienia, \n(3)-Dostępne pozycje, \n(4)-Dostępne pozycje z wybranej kategori, \n(5)-Nowości, \n(6)-Szukaj po frazie, \n(7)-Bestsellers, \n(8)-Ostatnie płatności,\n(9)-Niezapłacone płatności, \n(Q)-Wyjście\n')
        if(self.i=='1'):
            self.widok1()
            self.menu1()
        elif(self.i=='2'):
            self.widok2()
            self.menu1()
        elif(self.i=='3'):
            self.widok3()
            self.menu1()            
        elif(self.i=='4'):
            self.widok4()
            self.menu1()
        elif(self.i=='5'):
            self.widok5()
            self.menu1()
        elif(self.i=='6'):
            self.widok6()
            self.menu1() 
        elif(self.i=='7'):
            self.widok7()
            self.menu1()
        elif(self.i=='8'):
            self.widok8()
            self.menu1()
        elif(self.i=='9'):
            self.widok9()
            self.menu1() 
        elif(self.i=='Q' or self.i=='q' ):
            print('Koniec')        
        else:
            print("Wybór niepoprawny")
            self.menu1()
            
#Widok dane kontaktowe     
    def widok1(self):
        self.passwort=input('Wprowadź hasło: ')
        self.sql1= "select * from personal_details where personal_details.id_customer=(select id_customer from login where login.passwort=%s)"                                                     
        self.cursor.execute(self.sql1, (self.passwort))
        if(self.cursor.rowcount ==1):
                        
            self.results=self.cursor.fetchall()
            print("%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s\n" % ("Id klienta","Name", "Surname", "Date", "City", "Post code", "Street", "Home no.", "Province", "Phone no.", "E-mail"))
            
            for row in self.results:
                self.id_customer=row[0]
                self.firstname=row[1]
                self.lastname=row[2]
                self.birthday_date=row[3]
                self.city=row[4]
                self.post_code=row[5]
                self.street=row[6]
                self.home_number=row[7]
                self.province=row[8]
                self.phone_number=row[9]
                self.email=row[10] 
                print("%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s" % (self.id_customer,self.firstname, self.lastname,self.birthday_date, self.city, self.post_code, self.street, self.home_number, self.province, self.phone_number,self.email))
        else:
            print('Wprowadzone dane są niepoprawne')
            
            
#Widok ostatnie zamówienia
    def widok2(self):
    
        self.passwort=input('Wprowadź hasło: ')
        self.sql2= "select * from last_orders where last_orders.id_customer=(select id_customer from login where login.passwort=%s)"                                                     
        self.cursor.execute(self.sql2, (self.passwort))
        if(self.cursor.rowcount>=1):
    
            self.results=self.cursor.fetchall()        
    
            print("%-15s%-15s%-40s%-15s%-15s%-15s\n" % ("Id klienta","Nr zamówienia", "Tytuł książki", "Cena", "Data zamówienia", "Status zamówienia"))
    
            for row in self.results:
                self.id_customer=row[0]
                self.id_order=row[1]
                self.title=row[2]
                self.price=row[3]
                self.order_date=row[4]
                self.order_status=row[5]
                print("%-15s%-15s%-40s%-15s%-20s%-20s" % (self.id_customer,self.id_order, self.title, self.price, self.order_date, self.order_status))
        else:
            print("Wprowadzono niepoprawne dane lub brak zamówień")
    


#Widok dostępne książki     
    def widok3(self):
        
        self.sql3= "select * from available_books"                                                     
        self.cursor.execute(self.sql3)                                                               
        self.results=self.cursor.fetchall()
        print("%-40s%-15s%-15s%-15s%-15s%-15s%-20s%-20s\n" % ( "Tytuł książki", "Imie autora", "Nazwisko autora", "Cena", "ISBN","Wydawnictwo", "Ilość", "Status") )
                         
        for row in self.results:
            
            self.title=row[0]
            self.author_name=row[1]
            self.author_surname=row[2]
            self.price=row[3]
            self.ISBN=row[4]
            self.publisher=row[5]
            self.quantity=row[6]
            self.status_book =row[7]
                               
            print("%-40s%-15s%-15s%-15s%-15s%-15s%-20s%-20s" % (self.title, self.author_name, self.author_surname, self.price, self.ISBN, self.publisher, 
        self.quantity, self.status_book ))            
            
                 
#Widok książki według kategorii            
    def widok4(self):
        self.category=input('Wybierz kategorię książek: (Bibliografie/Informatyka/Kulinaria/Kryminaly)')
        
        self.sql4= "select * from books_category where category=%s"                                                     
        self.cursor.execute(self.sql4, (self.category))         
         
        if(self.cursor.rowcount>=1):
                        
            self.results=self.cursor.fetchall()
            print("%-15s%-35s%-15s%-15s%-15s%-15s%-15s%-20s%-20s\n" % ("Kategoria", "Tytuł książki", "Imie autora", "Nazwisko autora", "Cena", "ISBN","Wydawnictwo", "Ilość", "Status") )
            
            for row in self.results:
                self.category[0]
                self.title=row[1]
                self.author_name=row[2]
                self.author_surname=row[3]
                self.price=row[4]
                self.ISBN=row[5]
                self.publisher=row[6]
                self.quantity=row[7]
                self.status_book =row[8]
                                   
                 
                print("%-15s%-35s%-15s%-15s%-15s%-15s%-15s%-20s%-20s" % (self.category, self.title, self.author_name, self.author_surname, self.price, self.ISBN, self.publisher, 
            self.quantity, self.status_book ))
        
        else:
            print('Nie ma takiej kategorii')

#Widok nowości            
    def widok5(self):
        self.sql5= "select * from newcomers"                                                     
        self.cursor.execute(self.sql5)                                                               
        self.results=self.cursor.fetchall()
        print("%-40s%-15s%-15s%-15s%-15s%-20s%-20s\n" % ( "Tytuł książki", "Imie autora", "Nazwisko autora", "Cena", "ISBN","Wydawnictwo", "Ilość") )
                         
        for row in self.results:
            
            self.title=row[0]
            self.author_name=row[1]
            self.author_surname=row[2]
            self.price=row[3]
            self.ISBN=row[4]
            self.publisher=row[5]
            self.quantity=row[6]
            
                               
            print("%-40s%-15s%-15s%-15s%-15s%-20s%-20s" % (self.title, self.author_name, self.author_surname, self.price, self.ISBN, self.publisher, 
        self.quantity ))
            
#Widok wyszukiwanie po wyrazie           
    def widok6(self):
        self.title=input('Podaj szukany wyraz: ')
        
        self.sql6= "select * from key_word where title like %s"                                                     
        self.cursor.execute(self.sql6, ("%" +self.title+"%"))         
         
        if(self.cursor.rowcount>=1):
                        
            self.results=self.cursor.fetchall()
            print("%-40s%-15s%-15s%-15s%-15s%-15s%-20s%-20s\n" % ("Tytuł książki", "Imie autora", "Nazwisko autora", "Cena", "ISBN","Wydawnictwo", "Ilość", "Status") )
            
            for row in self.results:
                
                self.title=row[0]
                self.author_name=row[1]
                self.author_surname=row[2]
                self.price=row[3]
                self.ISBN=row[4]
                self.publisher=row[5]
                self.quantity=row[6]
                self.status_book =row[7]
                                   
                 
                print("%-40s%-15s%-15s%-15s%-15s%-15s%-20s%-20s" % (self.title, self.author_name, self.author_surname, self.price, self.ISBN, self.publisher, 
            self.quantity, self.status_book ))
        
        else:
            print('Szukana fraza nie została znaleziona')
                             
#Widok bestsellery                                                    
    def widok7(self):
        self.sql7= "select * from bestsellers_total"                                                     
        self.cursor.execute(self.sql7)                                                               
        self.results=self.cursor.fetchall()
        print("%-40s%-15s%-15s%-15s%-15s%-15s\n" % ( "Tytuł książki", "Imie autora", "Nazwisko autora", "Cena", "Status", "Ilość") )
                         
        for row in self.results:
            
            self.title=row[0]
            self.author_name=row[1]
            self.author_surname=row[2]
            self.price=row[3]
            
            self.status=row[4]
            self.quantity=row[5]
            
                               
            print("%-40s%-15s%-15s%-15s%-15s%-15s" % (self.title, self.author_name, self.author_surname, self.price, self.status, 
        self.quantity ))

#Widok ostatnie płatności
    def widok8(self):
        self.passwort=input('Wprowadź hasło: ')
        self.sql8= "select * from last_payments where last_payments.id_customer=(select id_customer from login where login.passwort=%s)"                                                              
        self.cursor.execute(self.sql8, (self.passwort))         
        if(self.cursor.rowcount>=1):        
            self.results=self.cursor.fetchall()        
            print("%-15s%-15s%-30s%-20s%-20s\n" % ("Id klienta","Id zamówienia", "Tytuł książki", "Ilość", "Status płatności"))
             
            for row in self.results:
                self.id_customer=row[0]
                self.id_order=row[1]
                self.title=row[2]
                self.amount=row[3]
                self.payment_status=row[4]
                
                print("%-15s%-15s%-30s%-15s%-15s" % (self.id_customer,self.id_order, self.title, self.amount, self.payment_status))
        else:
            print("Wprowadzono niepoprawne dane")
       

#Widok niezapłacone płatności     
    def widok9(self):
        self.passwort=input('Wprowadź hasło: ')
        self.sql9= "select * from not_paid_payments where not_paid_payments.id_customer=(select id_customer from login where login.passwort=%s)"                                                              
        self.cursor.execute(self.sql9, (self.passwort))         
        if(self.cursor.rowcount>=1):
                              
            self.results=self.cursor.fetchall()
            print("%-15s%-15s%-30s%-15s%-15s\n" % ("Id klienta", "Id zamówienia","Tytuł książki", "Ilość", "Status płatności"))
            
            for row in self.results:
                self.id_customer=row[0]
                self.id_order=row[1]
                self.title=row[2]
                self.amount=row[3]
                self.payment_status=row[4]
                
                print("%-15s%-15s%-30s%-15s%-15s" % (self.id_customer,self.id_order, self.title, self.amount, self.payment_status))
        else:
            print("Wprowadzono niepoprawne hasło lub nie ma płatości do zapłaty")
        
       
        
            
    