# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 15:57
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : views.py
# @Documents:
from flask import Blueprint

bp = Blueprint('common', __name__, url_prefix='/common')


@bp.route('/')
def index():
    return 'common index'
