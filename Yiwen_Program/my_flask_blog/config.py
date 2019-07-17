# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 15:51
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : config.py
# @Documents: flask configuration including db

import os

DEBUG = True
port = 5000


# 正式上线需要用urandom，不能采用固定session密钥
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

# ueditor upload infos
UEDITOR_QINIU_ACCESS_KEY = "W2ydQ1qDpNZpzJG1SaseiTrgdjpIPNhZ3hfR3cVN"
UEDITOR_QINIU_SECRET_KEY = "oGG5ocZ9UP66gANQh0eZk9I2odKu1iN9iyGQdKcW"
UEDITOR_QINIU_BUCKET_NAME = "flask-blog"
UEDITOR_QINIU_DOMAIN = "http://pu28slkuf.bkt.clouddn.com/"

# flask pagination 的相关配置
PER_PAGE = 10

#celery配置
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'