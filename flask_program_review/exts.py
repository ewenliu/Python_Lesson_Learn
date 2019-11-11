# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 15:26
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : exts.py
# @Documents: include sql, mail, sms function
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()
