create database bookshop;
use bookshop;


#Creating table with customers
create table customers(
  id_customer int not null auto_increment,
  firstname varchar(30) not null,
  lastname varchar(40) not null,
  gender varchar(10) not null,
  birthday_date date,
  city varchar(50) not null,
  post_code varchar(50) not null,
  street  varchar(50),
  home_number varchar(10) not null, 
  province varchar(50),
  phone_number varchar(20) not null,
  email varchar(30) not null,
  primary key (id_customer)
);

describe customers;
select * from customers;

insert into customers (id_customer, firstname, lastname, gender,
birthday_date,  city, post_code, street, home_number, province, 
phone_number, email) values 
(1, 'Aleksandra', 'Lewandowska', 'female','1978-08-06', 'Krakow', '01-200', 'Radomska', '4', 'malopolskie', '512207055', 'ola_lew@wp.pl'),
(2, 'Jan', 'Nowak','male', '1980-05-12', 'Radom', '04-500', 'Krakowska', '16', 'mazowieckie', '612208044', 'jan_now@wp.pl'),
(3, 'Maciej', 'Wojcik','male', '1970-03-11', 'Bydgoszcz', '11-530', 'Morska', '6', 'pomorskie', '711408334', 'mac_woj@wp.pl'),
(4, 'Agnieszka', 'Jankowska','female', '1969-11-02', 'Lublin', '09-100', 'Slowackiego', '34', 'lubelskie', '811608022', 'agn_jan@wp.pl'),
(5, 'Tomasz', 'Mazur','male', '1989-01-23', 'Jelenia Gora', '01-345', 'Tuwima', '46', 'dolnoslaskie', '815409056', 'tom_maz@wp.pl'),
(6, 'Anna', 'Zielinska','female', '1981-08-30', 'Nowa Wies', '08-320', 'Nowa', '23', 'lubuskie', '513208678', 'ann_ziel@wp.pl'),
(7, 'Artur', 'Rutkowski','male', '1976-01-26', 'Kielce', '03-159', 'Radomska', '67', 'kieleckie', '834508144', 'art_rut@wp.pl'),
(8, 'Mateusz', 'Skorupa','male', '1981-08-31', 'Gdansk', '01-590', 'Nadmorska', '89', 'pomorskie', '712456644', 'mat_skor@wp.pl'),
(9, 'Jerzy', 'Nowak','male', '1968-02-02', 'Rybnik', '05-500', 'Gornicza', '28', 'dolnoslaskie', '515608944', 'jerz_now@wp.pl'),
(10,'Anna', 'Kowalska','female', '1990-09-29', 'Pultusk', '02-410', 'Jagielly', '78', 'mazowieckie', '722108098', 'ann_kow@wp.pl'),
(13,'Marta', 'Kot','female', '1986-09-19', 'Opoczno', '12-110', 'Nowa', '18', 'lodzkie', '888108097', 'mar_kot@wp.pl');



#Creating tables with login and passwort
create table login (
    id_customer int not null,
    login varchar(45) not null unique,
    passwort varchar(32) not null,
    priviliges varchar(15),
    primary key(id_customer),
    foreign key(id_customer) references customers (id_customer)
 );

describe login;
select * from login;

insert into login (id_customer, login, passwort, priviliges) values  
(1, 'login1', 'passwort1','admin'),
(2, 'login2', 'passwort2', 'user'),
(3, 'login3', 'passwort3','user'),
(4, 'login4', 'passwort4', 'user'),
(5, 'login5', 'passwort5', 'user'),
(6, 'login6', 'passwort6', 'user'),
(7, 'login7', 'passwort7', 'user'),
(8, 'login8', 'passwort8', 'user'),
(9, 'login9', 'passwort9', 'user'),
(10,'login10','passwort10', 'user'),
(13,'login13','passwort13', 'user');


#Creating table with books
create table books (
  id_book int not null auto_increment,
  title varchar (45) not null,
  category varchar (45) not null,
  description text not null,
  author_name varchar (45) not null,
  author_surname varchar (45) not null,
  price float not null,
  ISBN varchar (45) not null,
  publisher varchar (45) not null,
  quantity int not null default 0,
  status_book varchar (45) not null default 'product niedostepny', 
  publishing_date date,
  primary key (id_book)
);

describe books;
select* from books;


insert into books (id_book, title, category, description, 
author_name, author_surname, price, ISBN, publisher,quantity,status_book, publishing_date) values
(1, 'HTML i CSS','Informatyka','Twoj przewodnik po swiecie webmasterow!','John','Duckett', 58.99,'9788324665204', 'Helion', 150, 'produkt dostepny', '2017-04-16' ),
(2, 'JavaScript dla dzieci','Informatyka','Dla dzieci od lat 10 i ich rodzicow.','Nick','Morgan', 59.99,'9788301183165', 'PWN',200, 'produkt dostepny', '2017-04-19'),
(3, 'Dieta Paleo','Kulinaria','Odzywiaj sie w zgodzie z natura.','Pete','Evans', 14.59,'9788376425269', 'Pascal',230, 'produkt dostepny', '2017-05-06'),
(4, 'Kochajac Pabla, nienawidzac Escobara','Bibliografie','Historia, która wydarzyła się naprawdę.','Virginia','Valejo', 59.99,'9788301183165', 'Agora',47, 'produkt dostepny', '2017-05-08'),
(5, 'Trzeci klucz','Kryminaly','Bezwzgledny przestepca z zabija młoda kasjerke.','Jo','Nesbo', 21.79,'9788324589937', 'Dolnoslaskie',0, 'produkt niedostepny', '2017-05-09'),
(6, 'Java w pigulce','Informatyka','Poznaj nowosci jezyka Java','Benjamin','Evans', 43.99,'9788328306233', 'Helion',90, 'produkt dostepny', '2017-05-11'),
(7, 'Thinking in Java','Informatyka','Poznaj najnowsza wersje jezyka Java','Bruce','Eckel', 115.99,'9788328334427', 'Helion',111, 'produkt dostepny', '2017-05-12'),
(8, 'Apteka zywnosci','Kulinaria','Korzystne wlasciwosci 55 powszechnie spozywanych pokarmow.','Jean','Carper', 21.99,'9788361524076', 'Vesper',256, 'produkt dostepny', '2017-05-12'),
(9, 'Elon Musk','Bibliografie','agadkowy wizjoner, kontrowersyjny biznesmen, niestrudzony pracoholik','Ashlee','Vance', 36.99,'9788324034406', 'Znak',189,'produkt dostepny', '2017-05-20'),
(10,'PHP MySQL i JavaScript','Informatyka','Przewodnik tworcy stron i aplikacji sieciowych!','Robert','Nixon', 73.99,'9788328308428', 'Helion',99, 'produkt dostepny', '2017-05-20'),
(11, 'Salatki','Kulinaria','Niezwykla popularnosc salatek to zasluga ich uniwersalnosci.','Andrzej','Fiedoruk', 11.89,'9788363559045', 'Dragon',125, 'produkt dostepny', '2017-05-23'),
(12, 'PHP i MySQL dla kazdego','Informatyka','W tej książce znajdziesz informacje potrzebne do opanowania podstaw języka PHP oraz MySQL.','Marcin','Lis', 79.99,'9788328324794', 'Helion',112, 'produkt dostepny' , '2017-05-25');


#Creating table with orders
create table orders(
  id_order int not null auto_increment,
  id_customer int not null,
  id_book int not null,
  order_date date not null,
  order_status varchar(20) not null,
  primary key(id_order),
  foreign key(id_book) references books(id_book),
  foreign key(id_customer) references customers(id_customer)
);

describe orders;
select * from orders;

insert into orders (id_order, id_customer, id_book, order_date, order_status) values
(1, 1, 3, '2017-03-16', 'wyslano'),
(2, 1, 4, '2017-03-16', 'wyslano'),
(3, 1, 12, '2017-03-16', 'wyslano'),
(4, 1, 10, '2017-03-16', 'wyslano'),
(5, 5, 2, '2017-03-21', 'wyslano'),
(6, 5, 6, '2017-03-27', 'wyslano'),
(7, 2, 11, '2017-04-03', 'wyslano'),
(8, 7, 5, '2017-04-09', 'wyslano'),
(9, 4, 6, '2017-04-14', 'wyslano'),
(10, 8, 1, '2017-04-19', 'wyslano'),
(11, 3, 5, '2017-04-21', 'wyslano'),
(12, 9, 7, '2017-04-21', 'wyslano'),
(13, 5, 5, '2017-04-23', 'wyslano'),
(14, 5, 8, '2017-04-27', 'wyslano'),
(15, 7, 9, '2017-04-28', 'wyslano'),
(16, 2, 2, '2017-05-08', 'wyslano'),
(17, 6, 4, '2017-05-09', 'wyslano'),
(18, 3, 3, '2017-05-10', 'wyslano'),
(19, 6, 2, '2017-05-14', 'wyslano'),
(20, 9, 7, '2017-05-14', 'oczekiwanie'),
(21, 6, 2, '2017-05-14', 'wyslano'),
(22, 7, 2, '2017-05-14', 'oczekiwanie'),
(23, 10, 2, '2017-05-15', 'oczekiwanie'),
(24, 10, 2, '2017-05-15', 'oczekiwanie'),
(25, 6, 10, '2017-05-15', 'oczekiwanie'),
(26, 4, 1, '2017-05-16', 'oczekiwanie'),
(27, 4, 12, '2017-05-16', 'oczekiwanie');



#Creating table with payments
create table payments (
id_order int not null,
payment_date date,
amount float not null default 0,
payment_status varchar(20) not null,
primary key(id_order),
foreign key(id_order) references orders(id_order)
);

describe payments;
select * from payments;


insert into payments (id_order, payment_date, amount, payment_status) values
(1, '2017-03-13', 14.59, 'zaplacono'),
(2, '2017-03-13', 14.59, 'zaplacono'),
(3, '2017-03-13', 14.59, 'zaplacono'),
(4, '2017-03-13', 14.59, 'zaplacono'),
(5, '2017-03-17', 14.59, 'zaplacono'),
(6, '2017-03-24', 21.79, 'zaplacono'),
(7, '2017-04-01', 43.99, 'zaplacono'),
(8, '2017-04-08', 11.89, 'zaplacono'),
(9, '2017-04-12', 21.79, 'zaplacono'),
(10, '2017-04-17', 43.99, 'zaplacono'),
(11, '2017-04-19', 58.99, 'zaplacono'),
(12, '2017-04-19', 21.79, 'zaplacono'),
(13, '2017-04-21', 115.99, 'zaplacono'),
(14, '2017-04-25', 21.79, 'zaplacono'),
(15, '2017-04-26', 21.99, 'zaplacono'),
(16, '2017-04-25', 36.99, 'zaplacono'),
(17, '2017-05-06', 9.99,  'zaplacono'),
(18, '2017-05-06', 59.99, 'zaplacono'),
(19, '2017-05-07', 14.59, 'zaplacono'),
(21, '2017-05-12', 59.99, 'zaplacono');


insert into payments (id_order,amount, payment_status) values
(20, 115.99,'niezaplacono'),
(22, 115.99,'niezaplacono'),
(23, 59.99, 'niezaplacono'),
(24, 59.99,'niezaplacono'),
(25,  73.99, 'niezaplacono'),
(26, 58.99, 'niezaplacono'),
(27, 79.99, 'niezaplacono');

select* from payments;


# FOR ADMIN
#Creating view presenting open orders
CREATE VIEW orders_status AS
    SELECT 
        id_order,
        title,
        DATE_FORMAT(order_date, '%d %M %Y') AS order_date,
        order_status
    FROM
        books,
        orders
    WHERE
        books.id_book = orders.id_book;

select *from orders_status;


#Creating view presenting customers from province mazowieckie
CREATE VIEW cust_prov AS
    SELECT 
        id_customer,  firstname, lastname, year(current_date())-year(birthday_date) as age, city, province, 
phone_number, email
    FROM
        customers
	ORDER by age;
    
select *from cust_prov;



#FOR USERS
#Creating view presenting personal details for specified user
CREATE VIEW personal_details AS
    SELECT 
		id_customer,
        firstname,
        lastname,
        birthday_date,
        city,
        post_code,
        street,
        home_number,
        province,
        phone_number,
        email
    FROM
        customers;

select * from personal_details;


#Creating view presenting last orders for specified user
CREATE VIEW last_orders AS
    SELECT 
		id_customer,
        orders.id_order,
        books.title,
        books.price,
        orders.order_date,
        orders.order_status      
    FROM
        orders
            NATURAL JOIN
        books
       
    ORDER BY order_date DESC;
    
select * from last_orders;


#Creating view presenting status of last payments for specified user 
CREATE VIEW last_payments AS
    SELECT 
        id_customer, id_order, title, amount, payment_status
    FROM
        payments
            NATURAL JOIN
        orders
            JOIN
        books ON (books.id_book = orders.id_book);

select* from last_payments; 


#Creating view presenting not paid payments for specified user
CREATE VIEW not_paid_payments AS
    SELECT 
        id_customer, id_order, title, amount, payment_status
    FROM
        payments
            NATURAL JOIN
        orders
            JOIN
        books ON (books.id_book = orders.id_book)
    WHERE
        payment_status= 'niezaplacono';

select* from not_paid_payments; 


#Creating view presenting all available books 
CREATE VIEW available_books AS
    SELECT 
        title, author_name, author_surname, price, 
        ISBN, publisher,quantity, status_book
    FROM
        books
    WHERE
        status_book = 'produkt dostepny'
	ORDER by title;
    
select *from available_books;


#Creating view presenting books from category Kulinaria
CREATE VIEW books_category AS
    SELECT 
        category,title, author_name, author_surname, price, 
        ISBN, publisher,quantity, status_book
    FROM
        books
    
	ORDER by price;
    
select *from books_category;


#Creating view presenting books lastly published in bookshop (newcomers)
CREATE VIEW newcomers AS
    SELECT 
        title,
        author_name,
        author_surname,
        price,
        ISBN,
        publisher,
        quantity
    FROM
        books
    ORDER BY publishing_date
    LIMIT 10;
    
select *from newcomers;


#Creating view presenting books with key word 
CREATE VIEW key_word AS
    SELECT 
        title, author_name, author_surname, price,
        ISBN, publisher,quantity, status_book
    FROM
        books
	ORDER by price;
    
select *from key_word; 


#Creating view presenting bestsellers from the beggining of year
CREATE VIEW bestsellers_total AS
    SELECT 
        title,
        author_name,
        author_surname,
        price,
        status_book,
        quantity 
    FROM
        books
            JOIN
        orders ON (books.id_book = orders.id_book)
    WHERE
        order_status = 'wyslano' and status_book= 'produkt dostepny'
        group by orders.id_book
    ORDER BY COUNT(orders.id_book) DESC;
    
select *from bestsellers_total;


#Creating view presenting bestsellers in current month
CREATE VIEW bestsellers_current_month AS
    SELECT 
        title,
        description,
        author_name,
        author_surname,
        price,
        status_book,
        quantity 
    FROM
        books
            JOIN
        orders ON (books.id_book = orders.id_book)
    WHERE
        order_status = 'wyslano' and status_book= 'produkt dostepny' and month(order_date)=5
        group by orders.id_book
    ORDER BY COUNT(orders.id_book) DESC;
    
select *from bestsellers_current_month;




