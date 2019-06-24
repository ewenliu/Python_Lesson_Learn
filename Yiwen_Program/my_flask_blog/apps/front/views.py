# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 15:57
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : views.py
# @Documents:

from flask import (
    Blueprint,
    views,
    render_template,
    make_response
)
from io import BytesIO
from utils.captcha import Captcha

bp = Blueprint('front', __name__)


@bp.route('/')
def index():
    return 'front index'


@bp.route('/captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp


class SignupView(views.MethodView):

    def get(self):
        return render_template('front/front_signup.html')


bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))
