# Flask CRUD web app using SQLAlchemy with MySQL

To create the database and table used in application is necessary to run dbcreate.sql file, if you want to run it locally for example.
You can use the simple command line: mysql -u root -p < path/to/dbcreate.sql or just create a new database and table with the especifications as the user table but with your own credentials (user,password,database name);

## Virtual Environment

I've used virtual environment to install necessary packages and setup a proper environment independent of the packages installed globaly. To install just run:     
**pip install virtualenv**

Create an environment:
* mkdir crud_flask
* cd crud_flask
* python3 -m venv venv**

Activate the environment:
venv\Scripts\activate

## Flask

Install Flask:
**pip install Flask**

## SQLAlchemy

I've used SQLAlchemy as ORM to represent the table from database as class. This is useful for not worrying about the commands (statements) in SQL language. The programming interface will manage all persistence work.

To install it, run: 
**pip install --user sqlalchemy flask-sqlalchemy**

To run the application locally, just run app.py;
