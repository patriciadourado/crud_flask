create database crud_py;

grant all on crud_py.* to 'root'@'%' identified by 'abc123';

use crud_py;

create table user(
id int(11) not null AUTO_INCREMENT,
username varchar(80) not null unique, 
email varchar(80) not null unique, 
address varchar(150) not null, 
phone varchar(15) not null,
PRIMARY KEY(id)) AUTO_INCREMENT = 1;