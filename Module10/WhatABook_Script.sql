use whatabook;

drop table if exists wishlist;
drop table if exists book;
drop table if exists user;
drop table if exists store;

create table store( 
	store_id INT NOT NULL PRIMARY KEY, 
	locale VARCHAR(500) NOT NULL 
); 

create table user( 
	user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	first_name VARCHAR (75) NOT NULL, 
	Last_name VARCHAR (75) NOT NULL 
); 

create table book( 
	book_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	book_name VARCHAR (200) NOT NULL, 
	details VARCHAR(500), 
	author VARCHAR(200) NOT NULL 
); 

create table wishlist( 
	wishlist_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	user_id INT NOT NULL, 
	book_id INT NOT NULL,  
    constraint foreign key(user_id) references user(user_id),  
	constraint foreign key(book_id) references book(book_id) 
); 

insert into store(store_id, locale) values(1, '123 Fake Street, FakeTown, USA'); 

insert into book(book_name, details, author) values('Happiness', 'Book on happiness', 'John Johnson'); 
insert into book(book_name, details, author) values('Much Happiness', 'Book on much happiness', 'John Johnson'); 
insert into book(book_name, details, author) values('Lots of Happiness', 'Book on lots of happiness', 'John Johnson'); 
insert into book(book_name, details, author) values('Big Happiness', 'Book on big happiness', 'John Johnson'); 
insert into book(book_name, details, author) values('Mighty Happiness', 'Book on mighty happiness', 'John Johnson'); 
insert into book(book_name, details, author) values('Crazy Happiness', 'Book on crazy happiness', 'John Johnson'); 
insert into book(book_name, details, author) values('Super Happiness', 'Book on super happiness', 'John Johnson'); 
insert into book(book_name, details, author) values('Happy Happiness', 'Book on happy happiness', 'John Johnson'); 
insert into book(book_name, details, author) values('Wild Happiness', 'Book on wild happiness', 'John Johnson Sr.'); 

insert into user(first_name, last_name) values('Aaron', 'Aaronson'); 
insert into user(first_name, last_name) values('Daren', 'Aaronson'); 
insert into user(first_name, last_name) values('Maron', 'Aaronson'); 
 
insert into wishlist(user_id, book_id) values(1, 1); 
insert into wishlist(user_id, book_id) values(2, 7); 
insert into wishlist(user_id, book_id) values(3, 5); 

