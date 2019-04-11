# -*- coding: utf-8 -*-
# @Time          : 2019/4/7 15:11
# @Author        : ewen.liu
# @Department    :
# @Function      :

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = '647b77c059c0e2990129d962c10f3ae3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'hduewenliu'
app.config['MAIL_PASSWORD'] = 'hduewen1122!'
mail = Mail(app)



from flaskblog import routes
