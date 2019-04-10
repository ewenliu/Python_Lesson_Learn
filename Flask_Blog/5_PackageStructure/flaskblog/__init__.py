# -*- coding: utf-8 -*-
# @Time          : 2019/4/7 15:11
# @Author        : ewen.liu
# @Department    :
# @Function      :

from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = '647b77c059c0e2990129d962c10f3ae3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes