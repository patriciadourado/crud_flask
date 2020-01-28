# CRUD web app using Flask and SQLAlchemy with MySQL
# Developed by Patricia Nunes Dourado in January 2020

from flask import Flask,render_template,request,redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc


connector = 'mysql+pymysql'
db_user = 'root'
pwd = 'abc123'
host = 'localhost'
database = 'crud_py'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = connector+'://'+db_user+':'+pwd+'@'+host+'/'+database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

db = SQLAlchemy() #initialize SQLAlchemy as our db.
db.init_app(app) #initialize by passing our app into it.

class User(db.Model):
	
	__tablename__ = 'user'
	
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(80),unique = True)
	email = db.Column(db.String(80),unique=True)
	address = db.Column(db.String(150), nullable=False)
	phone = db.Column(db.String(15), nullable=False)
	
	def __init__(self,username,email,address,phone):
		self.username = username
		self.email = email
		self.address = address
		self.phone = phone

@app.route('/')
def index():
	user = 'null'
	mode = "Add"
	return render_template('index.html',user=user,mode=mode)
	
@app.route('/users')
def users():
	user = User.query.all()
	return render_template('table.html',users=user)

@app.route('/add-user',methods=['POST','GET'])
def userAdded():
	new_id = request.form.get("id")
	new_name = request.form.get("username")
	new_email = request.form.get("email")
	new_address = request.form.get("address")
	new_phone = request.form.get("phone")
	
	
	new_user = User(username=new_name,email=new_email,address=new_address,phone=new_phone)
	
	if db.session.query(db.exists().where(User.id == new_id)).scalar():
		user = User.query.filter_by(id=new_id).first()
		user.username = new_name
		user.email = new_email
		user.address = new_address
		user.phone = new_phone
		db.session.commit()
		message = "Successfully edited!"
		return render_template('add-edit.html',user=new_user,message=message)
		
	else:
		try:
			db.session.add(new_user)
			db.session.commit()
			message = "Successfully added!"
			return render_template('add-edit.html',user=new_user,message=message)
			
		except exc.IntegrityError as e:
			
			db.session.rollback()
			message="Already registered!"
			return render_template('add-edit.html',user=new_user,message=message)

@app.route('/delete-user',methods=['POST'])
def deleteUser():
	id = request.form['id']
	user = User.query.filter_by(id=id).one()
	db.session.delete(user)
	db.session.commit()
	return redirect('users')

@app.route('/edit-user',methods=['GET','POST'])
def editUser():
	id = request.form['id']
	user = User.query.filter_by(id=id).one()
	mode = "Modify"
	return render_template('index.html',user=user,mode=mode)
	
if __name__ == '__main__':
    app.run(debug=True)