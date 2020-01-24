from flask import *
from db import *
public=Blueprint("public",__name__)
@public.route('/',methods=['post','get'])
def home():
	return render_template("index.html")
@public.route('/login',methods=['post','get'])
def login():
	if 'submit' in request.form:
		uname=request.form['uname']
		pwd=request.form['password']
		q="select * from login where username ='%s' and password='%s'"%(uname,pwd)
		res=select(q)
		if res:
			if res[0]['type']=="admin":
				return redirect(url_for('admin.home'))
			else:
				return redirect(url_for('user.home'))

	if 'register' in request.form:
		return redirect(url_for('register.home'))
	return render_template("login.html")

@public.route('/registerhome',methods=['post','get'])
def registerhome():
	
	if 'submit1'in request.form:
		uname=request.form['uname']
		pwd=request.form['pwd']
		fname=request.form['fname']
		lastname=request.form['lname']
		dob=request.form['dob']
		gender=request.form['gender']
		phone=request.form['phone']
		email=request.form['email']
		q="insert into login values(null,'%s','%s','user')"%(uname,pwd)
		id=insert(q)
		q="insert into user values(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lastname,dob,gender,phone,email)
		insert(q)
	return render_template('registerhome.html')