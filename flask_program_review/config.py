# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 15:26
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : config.py
# @Documents:
import os

PORT = 5000
DEBUG = True


DB_DIALECT = 'mysql'
DB_DRIVER = 'mysqldb'
DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_DATABASE = 'flask_program_review'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DB_DIALECT, DB_DRIVER, DB_USERNAME, DB_PASSWORD,
                                                                       DB_HOST, DB_PORT,
                                                                       DB_DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 使用os.urandom(24)生成
SECRET_KEY = b'\xd9\xa0\x8f\xa1o\x92o8*\xc3\xdc\x01\x0f\x7f\x98\xf2\xe1\t\xc0\x9f\x8a]\x10\xb1'

# CMS session用的key
CMS_USER_ID = 'ASDFADFSJ'
# Front session用的key
FRONT_USER_ID = 'jvoiaj214314'


MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = '465'
MAIL_USE_SSL = True
#MAIL_USE_TLS = True
MAIL_USERNAME = 'hduewenliu@163.com'
MAIL_PASSWORD = 'hduewen1122'
MAIL_DEFAULT_SENDER = 'hduewenliu@163.com'


# ueditor
# UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'images')
# 不要乱填，否则migration操作会到错误的路径，ueditor里面有个操作路径的命令
UEDITOR_UPLOAD_PATH = os.path.join('images')

# flask_pagination 设置
PER_PAGE = 10

# celery 相关配置
CELERY_RESULT_BACKEND = 'redis://:111111@10.140.14.105:6379/0'
CELERY_BROKER_URL = 'redis://:111111@10.140.14.105:6379/0'


# 腾讯云对象存储相关配置
TENCENT_CLOUD_SECRET_ID = 'XXX'  # 替换为用户的 secretId
TENCENT_CLOUD_SECRET_KEY = 'XXX'  # 替换为用户的 secretKey
TENCENT_CLOUD_REGION = 'ap-shanghai'
TENCENT_CLOUD_BUCKET = 'flask-blog-1259649563'
