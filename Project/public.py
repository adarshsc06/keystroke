from flask import *
from db import *
public=Blueprint("public",__name__)
@public.route('/',methods=['post','get'])
def home():
	return render_template("publichome.html")
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
		return redirect(url_for('register.regis'))
	return render_template("login.html")
@public.route('/registerhome',methods=['post','get'])
def register():
	return render_template("registerhome.html")