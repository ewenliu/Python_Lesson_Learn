# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 15:57
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : forms.py
# @Documents:

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length


class LoginForm(Form):
    email = StringField(validators=[Email(message='请输入正确的'
                                                  '邮箱格式'), InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(6, 20, message='请输入正确格式的密码')])
    remember = IntegerField()
