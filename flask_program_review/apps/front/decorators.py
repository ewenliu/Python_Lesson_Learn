# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 18:39
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
        if config.FRONT_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('front.signin'))
    return inner
