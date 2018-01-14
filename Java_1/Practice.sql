create table Customers(
  customer_id INTEGER CONSTRAINT customers_pk PRIMARY KEY,
  first_name varchar2(30),
  last_name varchar2(30),
  dob date,
  phone varchar2(11)
);
describe Customers;
insert into Customers values(
5,
'Cisco',
'Ramon',
'31-Jan-1984',
'7735894165'
);

create table product_types(
  product_type_id INTEGER CONSTRAINT product_types_pk PRIMARY KEY,
  name varchar2(30) NOT NULL
);

insert into product_types values(
5,
'Pen Drive'
);

select * from product_types;
create table products(
  product_id INTEGER CONSTRAINT products_pk PRIMARY KEY,
  product_type_id CONSTRAINT products_fk_product_types
  REFERENCES product_types(product_type_id),
  name varchar2(30),
  description varchar2(30),
  price number(5,2)
);
alter table products modify description varchar2(100);
insert into products values(
4,
2,
'Doctor Strange',
'The origin story of the mystical and magical superhero, who fights against Doramamu',
200
);

select * from products;

create table purchases(
  product_id INTEGER 
    CONSTRAINT purchaes_fk_products
    REFERENCES products(product_id),
  customer_id INTEGER 
    CONSTRAINT purchases_fk_customers
    REFERENCES Customers(customer_id),
  quantity INTEGER NOT NULL,
  CONSTRAINT purchases_pk PRIMARY KEY(product_id, customer_id)
);

describe purchases;

insert into purchases values(
  1,
  3,
  1
);

select * from purchases;

create table employees(
  employee_id INTEGER CONSTRAINT employees_pk PRIMARY KEY,
  manager_id INTEGER,
  first_name varchar2(30),
  last_name varchar2(30),
  title varchar2(30),
  salary number(6,0)
);

describe employees;

insert into employees values(
  4,
  2,
  'Julian',
  'Dorn',
  'Sales Person',
  150000
);

select * from employees;

create table salary_grades(
  salary_grade_id INTEGER CONSTRAINT salary_grades_pk PRIMARY KEY,
  low_salary NUMBER(6,0),
  high_salary NUMBER(6,0)
);

describe SALARY_GRADES;

insert into salary_grades values(
  4,
  200001,
  700000
);

select * from SALARY_GRADES;

select ROWID,customer_id
from Customers;

select first_name || ' ' || last_name as FULL_NAME from CUSTOMERS;
/*Trying the operators*/

select * from Customers
where customer_id > ALL(2,3,4);

/*LIKE OPERATOR IN ORACLE PRACTICE*/

select FIRST_NAME ||' '|| LAST_NAME as FULL_NAME from CUSTOMERS
where FIRST_NAME LIKE '%o%';

select p.name, pt.name
from products p, product_types pt
where p.product_type_id=pt.product_type_id
order by p.name;

/*TYpes of join in oracle sql
Equijoins and Non-equijoins
inner joins, outer joins, self joins
*/

select product_id,name,price
from products
where PRODUCT_ID=&v_product_id;

/*lets do some subqueries bro*/

/*
Single Row subquery
Multiple Row Sub queries
nested Subqueries
Corrleated subqueries
*/

/*Single Row Sub Query*/

select first_name,last_name
from Customers
where CUSTOMER_ID=(select CUSTOMER_ID from Customers where last_name='Queen');

/*show the product_id, name and price of the product having price greater than the average price*/

select product_id,name, price
from products
where price >(select avg(price) from products);

/*Let us see how we can use subquery in having clause*/

select product_type_id, avg(price)
from products
group by product_type_id
having avg(price) <(select max(avg(price))
from products
group by product_type_id)
order by product_type_id;

/*Multiple-Row Sub query*/

select product_id,name
from products
where product_id in(select product_id from products where name like '%a%');

--regular expression functions
/*
1965
1968
1971
1970
we can use the following regular expression:
^196[5-8]$
^-matches the begining postion of the string
$-matches the string at the end
Example:
But, soft! What light through yonder window breaks?
We weant to fin fthe substring "ligh"in the above string
we use the following regular expression:
l[[:alpha:]]{4}
REGEXP_LIKE(x, pattern,[,match_option])
REGEXP_INSTR(x, pattern [,start,occurence,return_option,match_option,subexp_option])
*/
--Regexp_Like() syntax
SELECT customer_id, first_name, last_name, dob
FROM customers
WHERE REGEXP_LIKE(TO_CHAR(dob, 'YYYY'), '^199[2-5]$');

SELECT
REGEXP_INSTR('But, soft! What light through yonder window breaks?',
'l[[:alpha:]]{4}') AS result
FROM dual;

/*Aggregate function*/

select AVG(PRICE) as Average_Price from products;

/*how to create a copy of the original table/or backup of the original table*/
create table products1 as 
select * from products;

--GRoup by clause
select product_type_id
from products
group  by product_type_id;










create table location(
  city varchar2(30),
  longitude integer,
  EastWest varchar2(2),
  latitude integer,
  NorthSouth varchar2(2)
);

create table weather(
  city varchar2(30),
  condition varchar2(30),
  temperature integer
);


insert into weather values(
  'SPARTA',
  'CLOUDY',
  74
);

select * from weather;

insert into location values(
  'MADRID', 3.41, 'W', 40.24, 'N'
);

select * from location

/*Let us see how to create views in oracle sql*/

create view invasion as 
  select weather.city,condition,temperature,latitude,NorthSouth,Longitude,EastWest
  from weather, location
  where weather.city=location.city;
describe invasion;
select * from invasion;

update invasion 
  set city='GREECE' 
  where city='SPARTA';
  
/*You cannot updcate the view instead it ask to update the base table on which the view is created*/

/* Regular Expression in Oracle SQL*/

select REGEXP_SUBSTR('123-456-7890', '-[^-]+' )
"REGEXP_SUBSTR"
from DUAL;

select REGEXP_SUBSTR
('MY LEDGER: Debits, Credits, and Invoices 1940',
'[:punct:]' ) "REGEXP_SUBSTR"
from DUAL;

create table bookshelf_checkout(
  name varchar2(30),
  title varchar2(30),
  checkout date,
  returned date
);

insert into bookshelf_checkout values(
  'ROLAND BRANDT', 'THE DISCOVERERS', '12-JAN-02', '01-MAR-02'

);

select * from BOOKSHELF_CHECKOUT;

select name, title, returned-checkout as daysout
from bookshelf_checkout
order by daysout desc;

create table trouble(
  city varchar2(30) NOT NULL,
  sampledate date NOT NULL,
  noon number(3,1),
  midnight number(3,1),
  precipitation number
);

insert into TROUBLE values
(
'PLEASANT LAKE','22-DEC-03',
-17.445, -10.4, 2.4
);

select * from trouble;
/*UNIQUE and PRIMARY KEY constraints create indexes*/
/* In check constraint included in syntax:check(rating <=9)*/
drop table trouble;

/*Indexes in ORACLE Bro*/

create table BOOKSHELF_AUTHOR
(Title VARCHAR2(100),
AuthorName VARCHAR2(50),
constraint TitleFK Foreign key (Title) references BOOKSHELF(Title),
constraint AuthorNameFK Foreign key (AuthorName)
references AUTHOR(AuthorName));

/* Dont run the above query*/

create unique index BA$TITLE_AUTHOR
on BOOKSHELF_AUTHOR(Title, AuthorName);

/* Let us see the the method to create clusters*/


cluster BOOKandAuthor(Title);


/*Creating a sequence*/
create table CUSTOMER_DEMO(
  Name varchar2(30),
  Contact Integer,
  ID Integer
);
create sequence CustomerID increment by 1 start with 1000;
drop table CUSTOMER_DEMO;
insert into CUSTOMER_DEMO (Name ,Contact,ID)
values('COLE CONSTRUCTION','VERONICA',CustomerID.NextVal);


CREATE TABLE more_products (
prd_id INTEGER
CONSTRAINT more_products_pk PRIMARY KEY,
prd_type_id INTEGER
CONSTRAINT more_products_fk_product_types
REFERENCES product_types(product_type_id),
name VARCHAR2(30) NOT NULL
);
drop table more_products;
/* UNION ALL operator*/
select * from PRODUCTS;

create table category(
  CategoryName varchar2(50) CONSTRAINT cg_name_pk PRIMARY KEY,
  ParentCategory varchar2(30) NOT NULL,
  SubCategory varchar2(30) NOT NULL
);
create table BOOKSHELF
(
Title VARCHAR2(100) primary key,
Publisher VARCHAR2(20),
CategoryName VARCHAR2(20),
Rating VARCHAR2(2),
constraint CATFK foreign key (CategoryName)
references CATEGORY(CategoryName));

insert into category 
values(
  'CHILDRENNF',
  'CHILDREN',
  'NON FICTION'
);

insert into BOOKSHELF values(
  'LETTERS AND PAPERS FROM PRISON',
  'SCRIBNER',
  'ADULTNF',
  4
); 

/*Partitioning in ORACLE*/

create table BOOKSHELF_RANGE_PART(
  Title VARCHAR2(100) primary key,
  Publisher VARCHAR2(20),
  CategoryName VARCHAR2(20),
  Rating VARCHAR2(2),
    constraint CATFK foreign key (CategoryName)
    references CATEGORY(CategoryName)
)
partition by range(CategoryName)
  (partition PART1 values less than ('B')
      tablespace PART1_TS,
    partition PART2 values less than(MAXVALUE)
      tablespace PART2_TS
    );

-----------------------------------------------
--PLSQL Programming
--Character Set and Lexical Units
-----------------------------------------------
DECLARE
 x NUMBER := 10;
 y NUMBER := 5;
 max NUMBER;
 BEGIN
 -- Easier to read:
 IF x > y THEN
 max:=x;
 ELSE
 max:=y;
 END IF;
 END;
 
 --Variables--
 declare
 
birthday date;
emp_count smallint :=0;
pi real := 3.0;
radius real := 1;
area real := pi*radius**2;
begin 
  null;
end;

--Constants--