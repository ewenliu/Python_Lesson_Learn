# -*- coding: utf-8 -*-
# @Time    : 2019/6/18 14:47
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : forms.py
# @Documents:

from wtforms import Form

class BaseForm(Form):
    def get_error(self):
        message = self.errors.popitem()[1][0]
        return message
