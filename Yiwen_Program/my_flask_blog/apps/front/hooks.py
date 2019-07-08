# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 18:51
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : hooks.py
# @Documents:
from .views import bp
from flask import session, g, render_template
from .models import FrontUser
import config


@bp.before_request
def my_before_request():
    if config.FRONT_USER_ID in session:
        user_id = session.get(config.FRONT_USER_ID)
        user = FrontUser.query.get(user_id)
        if user:
            g.front_user = user


@bp.errorhandler(404)
def page_not_found(error):
    return render_template('front/front_404.html')
