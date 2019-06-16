# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 15:51
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : config.py
# @Documents: flask configuration including db

import os

DEBUG = True
port = 5000
# PERMANENT_SESSION_LIFETIME =

SECRET_KEY = os.urandom(24)

DB_DIALECT = 'mysql'
DB_DRIVER = 'pymysql'
DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_DATABASE = 'my_flask_website'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DB_DIALECT,
                                                                       DB_DRIVER, DB_USERNAME, DB_PASSWORD, DB_HOST,
                                                                       DB_PORT, DB_DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
