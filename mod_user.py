# -*- coding: utf-8 -*-
import pymysql

class User:
    
    def __init__(self,id_customer):
        self.conn = pymysql.connect("localhost", "root", "kwiat23", "bookshop") 
        self.cursor = self.conn.cursor() 
        self.id_customer=id_customer
        self.menu_1()
        
    def menu_1(self):
        self.d=input('\nCo chcesz zrobić? \n(1)-Przeglądać dane prywatne \n(2)-Przeglądać zasoby bazy, \n(Q)-Wyjście\n')
        if(self.d=='1'):
            self.menu_3()         
        elif(self.d=='2'):
            self.menu_2()        
        elif(self.d=='Q' or self.d=='q'):
            print('Koniec')             
        else:
            print("Wybór niepoprawny")
            self.menu_1()
            
    def menu_2(self, id_customer=None):
        if id_customer is None:
            id_customer=self.id_customer        
        self.i =input('\nKtórą tabelę chcesz wybrać?: \n(1)-Dostępne pozycje, \n(2)-Dostępne pozycje z wybranej kategori, \n(3)-Nowości, \n(4)-Szukaj po frazie, \n(5)-Bestsellers,\n(6)-Powrót do menu, \n(Q)-Wyjście\n')
        
        if(self.i=='1'):
            self.widok3()
            self.menu_2()            
        elif(self.i=='2'):
            self.widok4()
            self.menu_2()
        elif(self.i=='3'):
            self.widok5()
            self.menu_2()
        elif(self.i=='4'):
            self.widok6()
            self.menu_2() 
        elif(self.i=='5'):
            self.widok7()
            self.menu_2()
        elif(self.i=='6'):
            print('Powrót do menu')
            self.menu_1()
        elif(self.i=='Q' or self.i=='q' ):
            print('Koniec')        
        else:
            print("Wybór niepoprawny")
            self.menu_2()           
            
    def menu_3(self, id_customer=None):
            if id_customer is None:
                id_customer=self.id_customer            
                self.i =input('\nKtórą tabelę chcesz wybrać?: \n(1)-Dane kontaktowe, \n(2)-Ostatnie zamówienia,\n(3)-Ostatnie płatności,\n(4)-Niezapłacone płatności,\n(5)-Powrót do menu, \n(Q)-Wyjście\n')
                if(self.i=='1'):
                    self.widok1(id_customer)
                    self.menu_3()
                elif(self.i=='2'):
                    self.widok2(id_customer)
                    self.menu_3()
                elif(self.i=='3'):
                    self.widok8(id_customer)
                    self.menu_3()
                elif(self.i=='4'):
                    self.widok9(id_customer)
                    self.menu_3()
                elif(self.i=='5'):
                    print('Powrót do menu')
                    self.menu_1()
                elif(self.i=='Q' or self.i=='q' ):
                    print('Koniec')        
                else:
                    print("Wybór niepoprawny")
                    self.menu_3()

            
#Widok dane kontaktowe     
    def widok1(self, id_customer=None):
        if id_customer is None:
            id_customer=self.id_customer
        
        self.sql1= "select * from personal_details where personal_details.id_customer=%s"                                                     
        self.cursor.execute(self.sql1, (id_customer))
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
            print('Nie ma w bazie usera o takim id')
            
            
#Widok ostatnie zamówienia
    def widok2(self,id_customer=None):
        if id_customer is None:
            id_customer=self.id_customer 
        self.sql2= "select * from last_orders where last_orders.id_customer=%s"                                                     
        self.cursor.execute(self.sql2, (id_customer))
        if(self.cursor.rowcount>=1):
            self.results=self.cursor.fetchall()           
            print("%-15s%-15s%-40s%-15s%-25s%-20s\n" % ("Id klienta","Nr zamówienia", "Tytuł książki", "Cena", "Data zamówienia", "Status zamówienia"))
    
            for row in self.results:
                self.id_customer=row[0]
                self.id_order=row[1]
                self.title=row[2]
                self.price=row[3]
                self.order_date=row[4]
                self.order_status=row[5]
                print("%-15s%-15s%-40s%-15s%-25s%-20s" % (self.id_customer,self.id_order, self.title, self.price, self.order_date, self.order_status))
        else:
            print("Brak zamówień")    


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
            print("%-15s%-45s%-15s%-25s%-15s%-15s%-15s%-20s%-20s\n" % ("Kategoria", "Tytuł książki", "Imie autora", "Nazwisko autora", "Cena", "ISBN","Wydawnictwo", "Ilość", "Status"))
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
                print("%-15s%-45s%-15s%-25s%-15s%-15s%-15s%-20s%-20s" % (self.category, self.title, self.author_name, self.author_surname, self.price, self.ISBN, self.publisher, 
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
                self.status_book=row[7]            
                print("%-40s%-15s%-15s%-15s%-15s%-15s%-20s%-20s" % (self.title, self.author_name, self.author_surname, self.price, self.ISBN, self.publisher, 
            self.quantity, self.status_book ))
        else:
            print('Szukana fraza nie została znaleziona')
             
                             
#Widok bestsellery                                                    
    def widok7(self):
        self.sql7= "select * from bestsellers_total"                                                     
        self.cursor.execute(self.sql7)                                                               
        self.results=self.cursor.fetchall()
        print("%-40s%-15s%-15s%-15s%-25s%-15s\n" % ( "Tytuł książki", "Imie autora", "Nazwisko autora", "Cena", "Status", "Ilość") )            
        for row in self.results:
            self.title=row[0]
            self.author_name=row[1]
            self.author_surname=row[2]
            self.price=row[3]
            self.status=row[4]
            self.quantity=row[5]               
            print("%-40s%-15s%-15s%-15s%-25s%-15s" % (self.title, self.author_name, self.author_surname, self.price, self.status, self.quantity ))


#Widok ostatnie płatności
    def widok8(self,id_customer=None):
        if id_customer is None:
            id_customer=self.id_customer              
        self.sql8= "select * from last_payments where last_payments.id_customer=%s"                                                              
        self.cursor.execute(self.sql8, (id_customer))         
        if(self.cursor.rowcount>=1):        
            self.results=self.cursor.fetchall()        
            print("%-15s%-15s%-30s%-15s%-15s\n" % ("Id klienta","Id zamówienia", "Tytuł książki", "Ilość", "Status płatności"))
            for row in self.results:
                self.id_customer=row[0]
                self.id_order=row[1]
                self.title=row[2]
                self.amount=row[3]
                self.payment_status=row[4]
                print("%-15s%-15s%-30s%-15s%-15s" % (self.id_customer,self.id_order, self.title, self.amount, self.payment_status))
        else:
            print("Brak płatności")
       

#Widok niezapłacone płatności     
    def widok9(self,id_customer=None):
        if id_customer is None:
            id_customer=self.id_customer        
        self.sql9= "select * from not_paid_payments where not_paid_payments.id_customer=%s"                                                              
        self.cursor.execute(self.sql9, (id_customer))         
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
            print("Brak niopłaconych płatności")
        
       
        
            
    