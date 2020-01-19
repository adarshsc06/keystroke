from flask import Flask
from public import public
from admin import admin
from user import user
from register import register
app=Flask(__name__)
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(user,url_prefix="/user")
app.register_blueprint(register,url_prefix="/registerhome")
app.run(debug="true",port="5000")
