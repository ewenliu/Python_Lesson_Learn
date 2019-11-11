# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 20:02
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : hooks.py
# @Documents:
from flask import session, g, render_template
from .views import bp
from .models import FrontUser
import config


@bp.before_request
def front_before_request():
    if config.FRONT_USER_ID in session:
        user_id = session.get(config.FRONT_USER_ID)
        user = FrontUser.query.get(user_id)
        if user:
            g.front_user = user


# 404 只能用app_errorhandler, 蓝图的errorhandler只能捕获非404错误
@bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('front/front_404.html'), 404


@bp.errorhandler(500)
def post_not_found(e):
    return render_template('front/front_404.html'), 500
