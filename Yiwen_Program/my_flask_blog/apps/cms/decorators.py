# -*- coding: utf-8 -*-
# @Time    : 2019/6/16 11:29
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : decorators.py
# @Documents:

from flask import session, redirect, url_for
from functools import wraps
import config

def login_required(func):

    @wraps(func)
    def inner(*args, **kwargs):
        if config.CMS_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('cms.login'))
    return inner
