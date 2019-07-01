# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 15:51
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : config.py
# @Documents: flask configuration including db

import os

DEBUG = True
port = 5000

# SECRET_KEY = os.urandom(24)
SECRET_KEY = b'\x15\xeez8\xb2@\xce\xcb!\xcd68\xe6}\xf7\xe7\x00\xc7\xec2\xbe\x0ft\xe5'

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

CMS_USER_ID = 'asdfafasdf'
FRONT_USER_ID = 'AGOWJGOJ1920VZ'

#发送者邮箱的服务器地址
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = '465'
# MAIL_USE_TLS = True
MAIL_USE_SSL = True
MAIL_USERNAME = 'hduewenliu@163.com'
MAIL_PASSWORD = 'hduewen1122'
MAIL_DEFAULT_SENDER = 'hduewenliu@163.com'



