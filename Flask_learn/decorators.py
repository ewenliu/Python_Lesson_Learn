# -*- coding: utf-8 -*-
# @Time          : 2019/5/21
# @Author        : ewen.liu
# @Department    :
# @Function      :
from functools import wraps
from flask import session, redirect, url_for


#Login limitation decorator
def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper