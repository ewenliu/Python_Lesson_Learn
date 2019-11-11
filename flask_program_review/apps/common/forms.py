# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 16:14
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : forms.py
# @Documents:
from apps.forms import BaseForm
from wtforms.validators import regexp, Email, InputRequired
from wtforms import StringField
from hashlib import md5


class EmailCaptchaForm(BaseForm):
    salt = 'ajsdoifjaoIFJOIWEF199#!'
    email = StringField(validators=[Email(message='Please enter right format email')])
    # UNIX 时间戳格式: 13位以15开头的数字
    timestamp = StringField(validators=[regexp(r'\d{13}')])
    sign = StringField(validators=[InputRequired()])

    def validate(self):
        result = super(EmailCaptchaForm, self).validate()
        if not result:
            return False

        email = self.email.data
        timestamp = self.timestamp.data
        sign = self.sign.data

        # sign2: 根据email, timestamp, salt生成一个md5码，和传过来的sign对比
        # md5必须传递的是bytes类型的字符串
        sign2 = md5((email+timestamp+self.salt).encode('utf-8')).hexdigest()
        if sign == sign2:
            return True
        else:
            return False
