# -*- coding: utf-8 -*-
from mod_user import *

class Admin(User):
    def __init__(self, id_customer):
        self.conn = pymysql.connect("localhost", "root", "kwiat23", "bookshop") 
        self.cursor = self.conn.cursor() 
        self.id_customer=id_customer
        self.menu_4()
        
    def menu_4(self):
        decyzja=input("\nKtóre menu chcesz otworzyc? \n(A)-menu administratora z możliwoscią wprowadzania zmian, \n(U)-menu usera z przeglądem danych prywatnych użytkowników, \n(P)-menu usera z przeglądem ogólnych zasobów bazy, \n(Q)-Wyjście\n")
        if(decyzja=='U' or decyzja=='u'):
            print("Wybrano menu Usera (dane prywatne)")
            id=input("Podaj id usera: ")
            self.sql_war= "select id_customer from login where id_customer=%s"
            self.cursor.execute(self.sql_war, id)
            if(self.cursor.rowcount ==1):
                row=self.cursor.fetchone()             
                self.menu_1_1(id)
            else:
                print('Nie ma takiego id w bazie')
                self.menu_4()                
        elif(decyzja=='P' or decyzja=='p'):
            print('Wybrano menu Usera (przegląd zasobów bazy)')
            self.menu_2_1()            
        elif(decyzja=='A' or decyzja=='a'):
            print('Wybrano menu Administratora')
            self.menu_5()
        elif(decyzja=='Q' or decyzja=='q'):
            print('Koniec')               
        else:
            print("Wybór niepoprawny")
            self.menu_4()
        
    def menu_5(self):
        self.i =input('\nKtórą tabelę chcesz wybrać?: \n(1)-Klienci, \n(2)-Logowanie, \n(3)-Książki, \n(4)-Zamówienia, \n(5)-Płatności, \n(6)-Zamówienia według statusów (oczekiwanie/wyslano, widok bez możliwości wprowadzania zmian),\n(7)-Klienci z wybranego województwa  (widok bez możliwości wprowadzania zmian), \n(8)-Powrót do menu \n(Q)-Wyjście\n')
        if(self.i=='1'):
            self.menu_6()
        elif(self.i=='2'):
            self.menu_7()
        elif(self.i=='3'):
            self.menu_8()
        elif(self.i=='4'):
            self.menu_9()
        elif(self.i=='5'):
            self.menu_10()
        elif(self.i=='6'):
            self.widok_ord_stat()
            self.menu_5()
        elif(self.i=='7'):
            self.widok_kl_woj()
            self.menu_5()
        elif(self.i=='8' ):
            print('Powrót do menu')
            self.menu_4()         
        elif(self.i=='Q' or self.i=='q' ):
            print('Koniec')        
        else:
            print("Wybór niepoprawny")
            self.menu_5()                                  
            
    def menu_6(self):
        self.j =input('\nJaką operację chcesz wykonać?: \n(I)-insert, \n(U)-update, \n(D)-delete, \n(M)-powrót do menu \n(Q)-wyjście\n')
        if(self.j=='I' or self.j=='i' ):
            self.wprowadzanie_kl()
            self.menu_6()
        elif(self.j=='U' or self.j=='u' ):
            self.modyfikacja_kl()
            self.menu_6() 
        elif(self.j=='D' or self.j=='d' ):
            self.usuwanie_kl()
            self.menu_6()        
        elif(self.j=='M' or self.j=='m' ):
            print('Powrót do menu')
            self.menu_5()             
        elif(self.j=='Q' or self.j=='q' ):
            print('Koniec')
        else:
            print("Wybór niepoprawny")
            self.menu_6()  
            
            
#Metody dla tabeli klienci            
    def wprowadzanie_kl(self):        
        self.firstname=input('Wprowadz imię: ')
        self.lastname=input('Wprowadz nazwisko: ')
        self.birthday_date=input('Wprowadz datę urodzenia: ')
        self.city=input('Wprowadz miasto: ')
        self.post_code=input('Wprowadz kod pocztowy: ')
        self.street=input('Wprowadz ulicę: ')
        self.home_number=input('Wprowadz nr domu: ')
        self.province=input('Wprowadz województwo: ')
        self.phone_number=input('Wprowadz nr telefonu: ')
        self.email=input('Wprowadz adres e-mail: ')                       
        if (self.firstname[len(self.firstname)-1]=='a'):
            self.gender='female'
        else:
            self.gender='male'                
        self.potwierdzenie= input('\nCzy na pewno chcesz dodać dane? (t/n)')        
        if(self.potwierdzenie=='t'):
            self.sql_wpr_kl= 'insert into customers (firstname, lastname, gender,birthday_date,city,post_code, street, home_number, province, phone_number, email) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(self.sql_wpr_kl,(self.firstname, self.lastname, self.gender, self.birthday_date, self.city, self.post_code, self.street, self.home_number, self.province, self.phone_number, self.email))
            self.conn.commit()
            print('\nDane wprowadzono')
        else:
            print('\nWstrzymano wpisywanie nowego użytkownika')
            
    def modyfikacja_kl(self):
        self.id_customer=input('Podaj id użytkownika do modyfikacji: ')
        self.sql_war= "select id_customer from customers where id_customer=%s"
        self.cursor.execute(self.sql_war, self.id_customer)
        if(self.cursor.rowcount ==1):
            row=self.cursor.fetchone()            
            self.firstname=input('Wprowadz imię: ')
            self.lastname=input('Wprowadz nazwisko: ')
            self.gender=input('Wprowadz płeć(male/female): ')
            self.birthday_date=input('Wprowadz datę urodzenia: ')
            self.city=input('Wprowadz miasto: ')
            self.post_code=input('Wprowadz kod pocztowy: ')
            self.street=input('Wprowadz ulicę: ')
            self.home_number=input('Wprowadz nr domu: ')
            self.province=input('Wprowadz województwo: ')
            self.phone_number=input('Wprowadz nr telefonu: ')
            self.email=input('Wprowadz adres e-mail: ')        
            self.potwierdzenie= input('\nCzy na pewno chcesz dodać dane? (t/n)')        
            if(self.potwierdzenie=='t'):        
                self.sql_mod_kl="update customers set firstname=%s, lastname=%s, gender=%s, birthday_date=%s, city=%s, post_code=%s, street=%s, home_number=%s, province=%s, phone_number=%s, email=%s where id_customer=%s"
                self.cursor.execute(self.sql_mod_kl,(self.firstname, self.lastname, self.gender, self.birthday_date, self.city, self.post_code, self.street, self.home_number, self.province, self.phone_number, self.email,self.id_customer))
                self.conn.commit()
                print('\nDane zmodyfikowano')
            else:
                print('\nWstrzymano modyfikowanie danych użytkownika')
        else:
            print("Nie ma takiego id w bazie")
        
    def usuwanie_kl(self):
        self.id_customer=input('Podaj id użytkownika do usunięcia: ')
        self.sql_war= "select id_customer from customers where id_customer=%s"
        self.cursor.execute(self.sql_war, self.id_customer)
        if(self.cursor.rowcount ==1):
            row=self.cursor.fetchone()                
            self.potwierdzenie= input('Czy na pewno chcesz usunąć? (t/n)')
            if(self.potwierdzenie=='t'):                
                self.sql_us_kl="delete from customers where id_customer=%s"
                self.cursor.execute(self.sql_us_kl,(self.id_customer))
                self.conn.commit()
                print('Użytkownik o Id: '+str(self.id_customer)+ ' został usunięty')
            else:
                print('Wstrzymano usuwanie użytkownika')
        else:
            print("Nie ma takiego id w bazie")
            
            
#Metody dla tabeli login     
    def menu_7(self):
        self.j =input('\nJaką operację chcesz wykonać?: \n(I)-insert, \n(U)-update, \n(D)-delete, \n(M)-powrót do menu \n(Q)-wyjście\n')
        if(self.j=='I' or self.j=='i' ):
            self.wprowadzanie_log()
            self.menu_7()
        elif(self.j=='U' or self.j=='u' ):
            self.modyfikacja_log()
            self.menu_7() 
        elif(self.j=='D' or self.j=='d' ):
            self.usuwanie_log()
            self.menu_7()        
        elif(self.j=='M' or self.j=='m' ):
            print('Powrót do menu')
            self.menu_5()             
        elif(self.j=='Q' or self.j=='q' ):
            print('Koniec')
        else:
            print("Wybór niepoprawny")
            self.menu_7()
            
    def wprowadzanie_log(self):
        self.id_customer=input('Podaj id użytkownika do wprowadzenia: ')
        self.sql_warunek= "select id_customer from customers where id_customer=%s"
        self.cursor.execute(self.sql_warunek, self.id_customer)
        if(self.cursor.rowcount==1):
            row=self.cursor.fetchone() 
            self.sql_warunek1= "select login from login where id_customer=%s"
            self.cursor.execute(self.sql_warunek1, self.id_customer)
            if(self.cursor.rowcount!=1):
                row=self.cursor.fetchone()
            
                self.login=input('Wprowadz login: ')
                self.passwort=input('Wprowadz hasło: ')
                self.priviliges=input('Wprowadz rodzaj uprawnień: ')
                self.potwierdzenie= input('\nCzy na pewno chcesz dodać nowego użytkownika? (t/n)')
                if(self.potwierdzenie=='t'):
                    self.sql_wpr_log= 'insert into login (id_customer,login,passwort, priviliges) values (%s,%s,%s,%s)'
                    self.cursor.execute(self.sql_wpr_log,(self.id_customer, self.login, self.passwort, self.priviliges))
                    self.conn.commit()
                    print('\nWprowadzono dane dla nowego użytkownika o Id: '+str(self.id_customer))
                else:
                    print('\nWstrzymano dodawanie nowego użytkownika')
            else:
                print('Użytkownik o tym id znajduje się już w tabeli')
        else:
            print('Nie możesz stworzyć nowego id bo w tabeli customers nie ma jeszcze klienta o takim numerze id')
            
    def modyfikacja_log(self):
        self.id_customer=input('Podaj id użytkownika do modyfikacji: ')
        self.sql_war= "select id_customer from login where id_customer=%s"
        self.cursor.execute(self.sql_war, self.id_customer)
        if(self.cursor.rowcount ==1):
            row=self.cursor.fetchone()        
            self.login=input('Wprowadz login: ')
            self.passwort=input('Wprowadz hasło: ')
            self.priviliges=input('Wprowadz rodzaj uprawnień: ')                    
            self.potwierdzenie= input('\nCzy na pewno chcesz zmodyfikować dane? (t/n)')       
            if(self.potwierdzenie=='t'):        
                self.sql_mod_log="update login set login=%s, passwort=%s, priviliges=%s where id_customer=%s"
                self.cursor.execute(self.sql_mod_log,(self.login, self.passwort, self.priviliges,self.id_customer))
                self.conn.commit()
                print('\nDane zmodyfikowano')
            else:
                print('\nWstrzymano modyfikowanie danych użytkownika')
        else:
            print("Nie ma takiego id w bazie")        
        
    def usuwanie_log(self):
        self.id_customer=input('Podaj id użytkownika do usunięcia: ')
        self.sql_war= "select id_customer from login where id_customer=%s"
        self.cursor.execute(self.sql_war, self.id_customer)
        if(self.cursor.rowcount ==1):
            row=self.cursor.fetchone()       
            self.potwierdzenie= input('Czy na pewno chcesz usunąć? (t/n)')
            if(self.potwierdzenie=='t'):                 
                self.sql_us_log="delete from login where id_customer=%s"
                self.cursor.execute(self.sql_us_log,(self.id_customer))
                self.conn.commit()
                print('Użytkownik o Id: '+str(self.id_customer)+ ' został usunięty')
            else:
                print('Wstrzymano usuwanie użytkownika')
        else:
            print("Nie ma takiego id w bazie") 
            
#Metody dla tabeli książki
    def menu_8(self):
        self.j =input('\nJaką operację chcesz wykonać?: \n(I)-insert, \n(U)-update, \n(D)-delete,\n(M)-powrót do menu,\n(Q)-wyjście\n')
        if(self.j=='I' or self.j=='i' ):
            self.wprowadzanie_ks()
            self.menu_8()
        elif(self.j=='U' or self.j=='u' ):
            self.modyfikacja_ks()
            self.menu_8() 
        elif(self.j=='D' or self.j=='d' ):
            self.usuwanie_ks()
            self.menu_8()        
        elif(self.j=='M' or self.j=='m' ):
            print('Powrót do menu')
            self.menu_5()    
        elif(self.j=='Q' or self.j=='q' ):
            print('Koniec')            
        else:
            print("Wybór niepoprawny")
            self.menu_8()
            
    def wprowadzanie_ks(self):        
        self.title=input('Wprowadz tytuł: ')
        self.category=input('Wprowadz kategorię: ')
        self.description=input('Wprowadz opis: ')
        self.author_name=input('Podaj imię autora: ')
        self.author_surname=input('Wprowadz nazwisko autora: ')
        self.price=input('Wprowadz cenę: ')
        self.ISBN=input('Wprowadz rodzaj nr ISBN: ')   
        self.publisher=input('Wprowadz wydawcę: ')
        self.quantity=input('Wprowadz ilość: ')
        self.status_book=input('Wprowadz status: ')
        self.publishing_date =input('Wprowadz datę publikacji: ')                      
        self.potwierdzenie= input('\nCzy na pewno chcesz dodać nową książkę? (t/n)')
        if(self.potwierdzenie=='t'):
            self.sql_wpr_ks= 'insert into books (title, category, description, author_name, author_surname, price, ISBN, publisher,quantity,status_book, publishing_date  ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(self.sql_wpr_ks,(self.title, self.category, self.description, 
            self.author_name, self.author_surname, self.price, self.ISBN, self.publisher, self.quantity, self.status_book, self.publishing_date))
            self.conn.commit()
            print('\nWprowadzono nową książkę')
        else:
            print('\nWstrzymano dodawanie nowej książki')
            

    def modyfikacja_ks(self):
        self.id_book=input('Podaj id książki do modyfikacji: ')
        self.sql_war= "select id_book from books where id_book=%s"
        self.cursor.execute(self.sql_war, self.id_book)
        if(self.cursor.rowcount ==1):
            row=self.cursor.fetchone()             
            self.title=input('Wprowadz tytuł: ')
            self.category=input('Wprowadz kategorię: ')
            self.description=input('Wprowadz opis: ')
            self.author_name=input('Podaj imię autora: ')
            self.author_surname=input('Wprowadz nazwisko autora: ')
            self.price=input('Wprowadz cenę: ')
            self.ISBN=input('Wprowadz rodzaj nr ISBN: ')   
            self.publisher=input('Wprowadz wydawcę: ')
            self.quantity=input('Wprowadz ilość: ')
            self.status_book=input('Wprowadz status: ')
            self.publishing_date =input('Wprowadz datę publikacji: ')                         
            self.potwierdzenie= input('\nCzy na pewno chcesz zmodyfikować dane? (t/n)')        
            if(self.potwierdzenie=='t'):        
                self.sql_mod_ks="update books set title=%s, category=%s, description=%s, author_name=%s, author_surname=%s, price=%s, ISBN=%s, publisher=%s, quantity=%s, status_book=%s, publishing_date=%s where id_book=%s"
                self.cursor.execute(self.sql_mod_ks,(self.title, self.category, self.description, 
                self.author_name, self.author_surname, self.price, self.ISBN, self.publisher, self.quantity, self.status_book, self.publishing_date,self.id_book))
                self.conn.commit()
                print('\nDane zmodyfikowano')
            else:
                print('\nWstrzymano modyfikowanie danych')    
        else:
            print("Nie ma takiego id w bazie") 
            
    def usuwanie_ks(self):
        self.id_book=input('Podaj id książki do usunięcia: ')
        self.sql_war= "select id_book from books where id_book=%s"
        self.cursor.execute(self.sql_war, self.id_book)
        if(self.cursor.rowcount ==1):
            row=self.cursor.fetchone()        
            self.potwierdzenie= input('Czy na pewno chcesz usunąć? (t/n)')
            if(self.potwierdzenie=='t'):                
                self.sql_us_ks="delete from books where id_book=%s"
                self.cursor.execute(self.sql_us_ks,(self.id_book))
                self.conn.commit()
                print('Książka o Id: '+str(self.id_book)+ ' została usunięta')
            else:
                print('Wstrzymano usuwanie książki')
        else:
            print("Nie ma takiego id w bazie")
           
            
#Metody dla tabeli zamówienia
    def menu_9(self):
        self.j =input('\nJaką operację chcesz wykonać?: \n(I)-insert, \n(U)-update, \n(D)-delete, \n(M)-powrót do menu \n(Q)-wyjście\n')
        if(self.j=='I' or self.j=='i' ):
            self.wprowadzanie_zam()
            self.menu_9()
        elif(self.j=='U' or self.j=='u' ):
            self.modyfikacja_zam()
            self.menu_9() 
        elif(self.j=='D' or self.j=='d' ):
            self.usuwanie_zam()
            self.menu_9()        
        elif(self.j=='M' or self.j=='m' ):
            print('Powrót do menu')
            self.menu_5()             
        elif(self.j=='Q' or self.j=='q' ):
            print('Koniec')
        else:
            print("Wybór niepoprawny")
            self.menu_9()                  
           
    def wprowadzanie_zam(self):        
        self.id_customer=input('Wprowadz Id klienta: ')
        self.sql_warunek1= "select id_customer from login where id_customer=%s"
        self.cursor.execute(self.sql_warunek1, self.id_customer)
        if(self.cursor.rowcount ==1):
            row=self.cursor.fetchone()
            self.id_book=input('Wprowadz Id książki: ')
            self.sql_warunek2= "select id_book from books where id_book=%s"
            self.cursor.execute(self.sql_warunek2, self.id_book)
            if(self.cursor.rowcount ==1):
                row1=self.cursor.fetchone()                    
                self.order_date=input('Wprowadz datę zamówienia: ')
                self.order_status=input('Wprowadź status zamówienia: ')                
                self.potwierdzenie= input('\nCzy na pewno chcesz dodać nowe zamówienie? (t/n)')
                if(self.potwierdzenie=='t'):
                    self.sql_wpr_zam= 'insert into orders (id_customer, id_book, order_date, order_status) values (%s,%s,%s,%s)'
                    self.cursor.execute(self.sql_wpr_zam,(self.id_customer, self.id_book, self.order_date, self.order_status))
                    self.conn.commit()
                    print('\nWprowadzono nowe zamówienie')
                else:
                    print('\nWstrzymano dodawanie nowejgo zamówienia')
            else:
                print('Nie ma takiego id książki')
        else:
            print('Nie ma takiego id użytkownika')
            
    def modyfikacja_zam(self):
        self.id_order=input('Podaj id zamówienia do modyfikacji: ')
        self.sql_war= "select id_order from orders where id_order=%s"
        self.cursor.execute(self.sql_war, self.id_order)
        if(self.cursor.rowcount ==1):
            row=self.cursor.fetchone()
            self.id_customer=input('Wprowadz Id klienta: ')
            self.id_book=input('Wprowadz Id książki: ')
            self.order_date=input('Wprowadz datę zamówienia: ')
            self.order_status=input('Wprowadź status zamówienia: ')                               
            self.potwierdzenie= input('\nCzy na pewno chcesz zmodyfikować zamówienie? (t/n)')   
            if(self.potwierdzenie=='t'):        
                self.sql_mod_zam="update orders set id_customer=%s, id_book=%s, order_date=%s, order_status=%s where id_order=%s"
                self.cursor.execute(self.sql_mod_zam,(self.id_customer, self.id_book, self.order_date, self.order_status, self.id_order))
                self.conn.commit()
                print('\nDane zmodyfikowano')
            else:
                print('\nWstrzymano modyfikowanie danych')    
        else:
            print("Nie ma takiego id w bazie")
            
    def usuwanie_zam(self):
        self.id_order=input('Podaj id zamówienia do usunięcia: ')
        self.sql_war= "select id_order from orders where id_order=%s"
        self.cursor.execute(self.sql_war, self.id_order)
        if(self.cursor.rowcount ==1):
            row=self.cursor.fetchone()        
            self.potwierdzenie= input('Czy na pewno chcesz usunąć? (t/n)')
            if(self.potwierdzenie=='t'):                 
                self.sql_us_zam="delete from orders where id_order=%s"
                self.cursor.execute(self.sql_us_zam,(self.id_order))
                self.conn.commit()
                print('Zamówienie o Id: '+str(self.id_order)+ ' zostało usuniętę')
            else:
                print('Wstrzymano usuwanie zamówienia')
        else:
            print("Nie ma takiego id w bazie")      
     
        
#Metody dla tabeli płatności
    def menu_10(self):
        self.j =input('\nJaką operację chcesz wykonać?: \n(I)-insert, \n(U)-update, \n(D)-delete, \n(M)-powrót do menu \n(Q)-wyjście\n')
        if(self.j=='I' or self.j=='i' ):
            self.wprowadzanie_pl()
            self.menu_10()
        elif(self.j=='U' or self.j=='u' ):
            self.modyfikacja_pl()
            self.menu_10() 
        elif(self.j=='D' or self.j=='d' ):
            self.usuwanie_pl()
            self.menu_10()        
        elif(self.j=='M' or self.j=='m' ):
            print('Powrót do menu')
            self.menu_5()    
        elif(self.j=='Q' or self.j=='q' ):
            print('Koniec')
        else:
            print("Wybór niepoprawny")
            self.menu_10() 
            
    def wprowadzanie_pl(self):
        self.id_order=int(input('Wprowadz Id płatności: '))
        self.sql_warunek= "select id_order from orders where id_order=%s"
        self.cursor.execute(self.sql_warunek, self.id_order)
        if(self.cursor.rowcount==1):
            row=self.cursor.fetchone()
        
       
            self.sql_war= "select id_order from payments where id_order=%s"
            self.cursor.execute(self.sql_war, self.id_order)
            if(self.cursor.rowcount!=1):
                row=self.cursor.fetchone()
                self.amount=input('Wprowadz kwotę: ')
                self.payment_status=input('Wprowadź status płatności: ')               
                self.potwierdzenie= input('\nCzy na pewno chcesz dodać nową płatność? (t/n)')
                if(self.potwierdzenie=='t'):
                    self.sql_wpr_pl= 'insert into payments (id_order, amount, payment_status) values (%s,%s,%s)'
                    self.cursor.execute(self.sql_wpr_pl,(self.id_order, self.amount, self.payment_status))
                    self.conn.commit()
                    print('\nWprowadzono nową płatność')
                else:
                    print('\nWstrzymano dodawanie nowej płatności')
            else:       
                print('Płatnosc o tym id już istnieje w bazie.') 
        else:
            print('Nie możesz stworzyć nowego id bo w tabeli orders nie ma jeszcze zamówienia o takim numerze id         ')   
                
    def modyfikacja_pl(self):
        self.id_order=input('Podaj id płatności do modyfikacji: ')
        self.sql_war= "select id_order from payments where id_order=%s"
        self.cursor.execute(self.sql_war, self.id_order)
        if(self.cursor.rowcount ==1):
            row=self.cursor.fetchone()        
            self.payment_date=input('Wprowadz datę płatności: ')
            self.amount=input('Wprowadz kwotę: ')
            self.payment_status=input('Wprowadź status płatności: ')                                                  
            self.potwierdzenie= input('\nCzy na pewno chcesz zmodyfikować płatność (t/n)')       
            if(self.potwierdzenie=='t'):        
                self.sql_mod_pl="update payments set payment_date=%s, amount=%s, payment_status=%s where id_order=%s"
                self.cursor.execute(self.sql_mod_pl,(self.payment_date, self.amount, self.payment_status, self.id_order))
                self.conn.commit()
                print('\nDane zmodyfikowano')
            else:
                print('\nWstrzymano modyfikowanie danych') 
        else:
            print("Nie ma takiego id w bazie") 
            
    def usuwanie_pl(self):
        self.id_order=input('Podaj id płatności do usunięcia: ')
        self.sql_war= "select id_order from payments where id_order=%s"
        self.cursor.execute(self.sql_war, self.id_order)
        if(self.cursor.rowcount ==1):
            row=self.cursor.fetchone()            
            self.potwierdzenie= input('Czy na pewno chcesz usunąć? (t/n)')
            if(self.potwierdzenie=='t'):                
                self.sql_us_pl="delete from payments where id_order=%s"
                self.cursor.execute(self.sql_us_pl,(self.id_order))
                self.conn.commit()
                print('Płatność o Id: '+str(self.id_order)+ ' została usunięta')
            else:
                print('Wstrzymano usuwanie płatności')
        else:
            print("Nie ma takiego id w bazie")     
  
  
#Metoda dla widoku status zamówień           
    def widok_ord_stat(self):
        self.order_status=input("Podaj status zamówienia (oczekiwanie/wyslano) ")
        self.sql_ord_stat= "select * from orders_status where order_status=%s"    
        self.cursor.execute(self.sql_ord_stat,(self.order_status))       
        if(self.cursor.rowcount>=1):                                                                                 
            self.results=self.cursor.fetchall()
            print("%-15s%-40s%-30s%-30s\n" % ( "Id zamówienia", "Tytuł", "Data zamówienia", "Status" ))                            
            for row in self.results:               
                self.id_order=row[0]
                self.title=row[1]
                self.order_date=row[2]
                self.order_status=row[3]
                print("%-15s%-40s%-30s%-30s" % (self.id_order, self.title, self.order_date, self.order_status)) 
        else:
            print('Nie znaleiono wyników dla podanego statusu')      


#Metoda dla widoku klienci z poszczególnych województw                                 
    def widok_kl_woj(self):
        self.province=input("Podaj nazwę województwa bez polskich znaków ")
        self.sql_kl_woj= "select * from cust_prov where province=%s"    
        self.cursor.execute(self.sql_kl_woj,(self.province))        
        if(self.cursor.rowcount>=1):                                                                                 
            self.results=self.cursor.fetchall()
            print("%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s\n" % ( "Id klienta", "Imie", "Nazwisko", "Wiek" , "Miasto","Województwo", "Nr tel", "E-mail"))
                             
            for row in self.results:               
                self.id_customer=row[0]
                self.firstname=row[1]
                self.lastname=row[2]
                self.age=row[3]
                self.city=row[4]
                self.province=row[5]
                self.phone_number=row[6]
                self.email=row[7]                                    
                print("%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s" % (self.id_customer,  self.firstname, self.lastname, self.age, self.city, self.province, self.phone_number, self.email )) 
        else:
            print('Nie znaleiono wyników dla podanego województwa')         

            
    def menu_1_1(self, id_customer=None):
        if id_customer is None:
            id_customer=self.id_customer        
        self.i =input('\nKtórą tabelę chcesz wybrać?: \n(1)-Dane kontaktowe, \n(2)-Ostatnie zamówienia,\n(3)-Ostatnie płatności,\n(4)-Niezapłacone płatności,\n(5)-Powrót do menu, \n(Q)-Wyjście\n')
        if(self.i=='1'):
            self.widok1(id_customer)
            self.menu_1_1(id_customer)
        elif(self.i=='2'):
            self.widok2(id_customer)
            self.menu_1_1(id_customer)
        elif(self.i=='3'):
            self.widok8(id_customer)
            self.menu_1_1(id_customer)
        elif(self.i=='4'):
            self.widok9(id_customer)
            self.menu_1_1(id_customer)
        elif(self.i=='5'):
            print('Powrót do menu')
            self.menu_4()
        elif(self.i=='Q' or self.i=='q' ):
            print('Koniec')        
        else:
            print("Wybór niepoprawny")
            self.menu_1_1(id)                 
                        
    def menu_2_1(self, id_customer=None):
        if id_customer is None:
            id_customer=self.id_customer        
        self.i =input('\nKtórą tabelę chcesz wybrać?: \n(1)-Dostępne pozycje, \n(2)-Dostępne pozycje z wybranej kategori, \n(3)-Nowości, \n(4)-Szukaj po frazie, \n(5)-Bestsellers,\n(6)-Powrót do menu, \n(Q)-Wyjście\n')
        
        if(self.i=='1'):
            self.widok3()
            self.menu_2_1()            
        elif(self.i=='2'):
            self.widok4()
            self.menu_2_1()
        elif(self.i=='3'):
            self.widok5()
            self.menu_2_1()
        elif(self.i=='4'):
            self.widok6()
            self.menu_2_1() 
        elif(self.i=='5'):
            self.widok7()
            self.menu_2_1()
        elif(self.i=='6'):
            print('Powrót do menu')
            self.menu_4()
        elif(self.i=='Q' or self.i=='q' ):
            print('Koniec')        
        else:
            print("Wybór niepoprawny")
            self.menu_2_1()          
                        
                        