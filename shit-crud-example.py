# simple CRUD python and MySQL
# Developed by Patricia Nunes Dourado in December 2019

import pymysql.cursors
import base64

#CREATE DATABASE for python crud:
""" create database crud_python; """

#connect to database:
connector = 'mysql+pymysql'
db_user = 'root'
pwd = 'abc123'
host = 'localhost'
database = 'crud_py'

connection = pymysql.connect(host = host,user = db_user, password = pwd,db = database)

#CREATE TABLE users:
""" my_db = connection.cursor()
query = "create table users(
id int(11) not null AUTO_INCREMENT,
email varchar(255) not null unique,
password varchar(255) not null,
PRIMARY KEY(id))AUTO_INCREMENT=1;"

my_db.execute(query) """

try:
    my_db = connection.cursor()
    #CREATE
    pwd = base64.b64encode(bytes('pwd123','utf-8'))
    query = "INSERT INTO users (`email`,`password`) VALUES (%s,%s)"
    my_db.execute(query,('name@surname.com',pwd))
	query = "INSERT INTO users (`email`,`password`) VALUES (%s,%s)"
	my_db.execute(query,('name1@surname.com',pwd))
	query = "INSERT INTO users (`email`,`password`) VALUES (%s,%s)"
	my_db.execute(query,('name2@surname.com',pwd))
    #READ
    my_db.execute('select * from users;')
    rows = my_db.fetchall()
    print(rows)
    #UPDATE
    query = "UPDATE users SET email = %s WHERE email = %s"
    my_db.execute(query,('your@domain.com','name1@surname.com'))
    #DELETE
    query = "DELETE FROM users WHERE email = %s"
    my_db.execute(query,('name2@surname.com'))
except pymysql.Error as e:
    print(e)
    connection.rollback()
    connection.close()
else:
    connection.commit()
    connection.close()