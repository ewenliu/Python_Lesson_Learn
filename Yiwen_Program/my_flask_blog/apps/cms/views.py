# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 15:56
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : views.py
# @Documents:

from flask import Blueprint, views, render_template

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/')
def index():
    return 'cms index'


class LoginView(views.MethodView):

    @staticmethod
    def get():
        return render_template('cms/cms_login.html')

    def post(self):
        pass


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
