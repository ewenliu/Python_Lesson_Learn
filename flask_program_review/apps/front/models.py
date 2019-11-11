# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 15:29
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : models.py
# @Documents:

from exts import db
import shortuuid
from werkzeug.security import generate_password_hash, check_password_hash
import enum
from datetime import datetime


# 性别枚举类
class GenderEnum(enum.Enum):
    MALE = 1
    FEMALE = 2
    SECRET = 3
    UNKNOW = 4


class FrontUser(db.Model):
    __tablename__ = 'front_user'
    id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid)
    # telephone = db.Column(db.String(11), unique=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    # 真实姓名
    realname = db.Column(db.String(50))
    # 头像
    avatar = db.Column(db.String(50))
    signature = db.Column(db.String(50))
    gender = db.Column(db.Enum(GenderEnum), default=GenderEnum.UNKNOW)
    join_time = db.Column(db.String(50), default=datetime.now)

    def __init__(self, *args, **kwargs):
        if 'password' in kwargs:
            self.password = kwargs.get('password')
            kwargs.pop('password')
        super(FrontUser, self).__init__(*args, **kwargs)

    # 这个装饰的作用是让函数可以通过属性访问
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        # 加密后的非明文密码才能存到数据库中
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result
