from flask import *
from db import *
register=Blueprint("register",__name__)
@register.route('/register',methods=['post','get'])
def home():
	return render_template('registerhome.html')
def regis():
	if 'submit'in request.form:
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
		return render_template("userhome.html")