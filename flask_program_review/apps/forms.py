# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 18:01
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : FORMS.py
# @Documents:

# define base class element

from wtforms import Form


class BaseForm(Form):
    '''
    errors 中的键值对长这样
    ('password', ['Please enter right format password'])
    [1][0] 表示取'Please enter right format password'
    '''
    def get_error(self):
        return self.errors.popitem()[1][0]

    def validate(self):
        return super(BaseForm, self).validate()
