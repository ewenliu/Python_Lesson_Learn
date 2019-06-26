# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 16:36
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : forms.py
# @Documents:

from apps.forms import BaseForm
from wtforms import StringField
from wtforms.validators import regexp, input_required
import hashlib


class SMSCaptchaForm(BaseForm):
    salt = 'dfjqowmsajdoviowqriozpdoksa'
    telephone = StringField(validators=[regexp(r'1[345789]\d{9}')])
    timestamp = StringField(validators=[regexp(r'\d{13}')])
    sign = StringField(validators=[input_required()])

    def validate(self):
        result = super(SMSCaptchaForm, self).validate()
        if not result:
            return False

        telephone = self.telephone.data
        timestamp = self.timestamp.data
        sign = self.sign.data

        sign2 = hashlib.md5((timestamp+telephone+self.salt).encode('utf-8')).hexdigest()
        print(sign)
        print(sign2)
        if sign == sign2:
            return True
        else:
            return False
