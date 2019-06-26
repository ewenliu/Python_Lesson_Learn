# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 15:57
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : views.py
# @Documents:
from flask import (
    Blueprint,
    request,
    make_response
)
from utils import restful, smssender, blog_cache
from utils.captcha import Captcha
from .forms import SMSCaptchaForm
from io import BytesIO



bp = Blueprint('common', __name__, url_prefix='/c')


@bp.route('/')
def index():
    return 'test'

# @bp.route('/sms_captcha/')
# def sms_captcha():
#     # ?telephone=xxx
#     telephone = request.args.get('telephone')
#     if not telephone:
#         return restful.params_error(message='请输入手机号码')
#
#     captcha = Captcha.gene_text(number=4)
#     if smssender.send(telephone, captcha=captcha):
#         return restful.success()
#     else:
#         return restful.params_error(message='短信验证码发送失败')
@bp.route('/sms_captcha/', methods=['POST'])
def sms_captcha():
    form = SMSCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = Captcha.gene_text(number=4)
        if smssender.send(telephone, captcha=captcha):
            blog_cache.set(telephone, captcha)
            return restful.success()
        else:
            return restful.params_error(message='短信验证码发送失败')
    else:
        return restful.params_error(message='参数错误！')


@bp.route('/captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    blog_cache.set(text.lower(), text.lower())
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp

