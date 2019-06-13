# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 15:56
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : views.py
# @Documents:

from flask import Blueprint

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/')
def index():
    return 'cms index'
