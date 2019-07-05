# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 16:31
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : decorators.py
# @Documents:
from functools import wraps
from flask import session, redirect, url_for
import config


def login_required(func):

    @wraps(func)
    def inner(*args, **kwargs):
        if config.FRONT_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('front.signin'))
    return inner