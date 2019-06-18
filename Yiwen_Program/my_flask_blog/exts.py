# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 15:52
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : exts.py
# @Documents: extra file to init db to avoid the import clash

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


db = SQLAlchemy()
mail = Mail()
