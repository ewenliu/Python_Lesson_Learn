# -*- coding: utf-8 -*-
# @Time          : 2019/4/7 15:11
# @Author        : ewen.liu
# @Department    :
# @Function      :


class Config(object):
    SECRET_KEY = '647b77c059c0e2990129d962c10f3ae3'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'hduewenliu'
    MAIL_PASSWORD = 'ewenliu123!'

