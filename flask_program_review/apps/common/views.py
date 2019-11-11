# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 15:29
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : views.py
# @Documents:
from flask import Blueprint, request, make_response, jsonify
from utils import restful, blogcache
from utils.captcha import Captcha
from io import BytesIO
import string
import random
from flask_mail import Message
from exts import mail
from .forms import EmailCaptchaForm
import qiniu
from tasks import send_email

bp = Blueprint('common', __name__, url_prefix='/common')


@bp.route('/')
def index():
    return 'common index'


@bp.route('/captcha/')
def gragh_captcha():
    text, image = Captcha.gene_graph_captcha()
    blogcache.set(text.lower(), text.lower())
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp


# @bp.route('/email_captcha/')
# def email_captcha():
#     # 参数传递方式如下
#     # /email_captcha/?email=xxx@xxx.com
#     email = request.args.get('email')
#     if not email:
#         return restful.params_error('Please fill email address!')
#
#     # 产生随机验证码
#     # string.ascii_letters -- > 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     # source 是26个大小写英文字母加上10个数字，验证码随机从这中间取得6位
#     source = list(string.ascii_letters)
#     source.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
#     # random.sample(source, 6) --> [x,x,x,x,x,x] 需要用''.join转化成字符串
#     captcha = ''.join(random.sample(source, 6))
#     message = Message(subject='Blog password email captcha', recipients=[email],
#                       body='[My Blog] Your captcha is %s' % captcha)
#     try:
#         mail.send(message)
#     except:
#         return restful.server_error()
#     blogcache.set(email, captcha)
#     return restful.success()

# 优化邮箱验证码发送api，采用post请求(更加安全)
# @bp.route('/email_captcha/', methods=['POST'])
# def email_captcha():
#     form = EmailCaptchaForm(request.form)
#     if form.validate():
#         email = form.email.data
#         # 产生随机验证码
#         # string.ascii_letters -- > 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         # source 是26个大小写英文字母加上10个数字，验证码随机从这中间取得6位
#         source = list(string.ascii_letters)
#         source.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
#         # random.sample(source, 6) --> [x,x,x,x,x,x] 需要用''.join转化成字符串
#         captcha = ''.join(random.sample(source, 6))
#         message = Message(subject='Blog password email captcha', recipients=[email],
#                           body='[My Blog] Your captcha is %s' % captcha)
#         try:
#             mail.send(message)
#         except:
#             return restful.server_error()
#         blogcache.set(email, captcha)
#         return restful.success()
#     else:
#         return restful.params_error(message='Params error!')


# 采用celery异步发送
@bp.route('/email_captcha/', methods=['POST'])
def email_captcha():
    form = EmailCaptchaForm(request.form)
    if form.validate():
        email = form.email.data
        # 产生随机验证码
        # string.ascii_letters -- > 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # source 是26个大小写英文字母加上10个数字，验证码随机从这中间取得6位
        source = list(string.ascii_letters)
        source.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        # random.sample(source, 6) --> [x,x,x,x,x,x] 需要用''.join转化成字符串
        captcha = ''.join(random.sample(source, 6))
        # message = Message(subject='Blog password email captcha', recipients=[email],
        #                   body='[My Blog] Your captcha is %s' % captcha)
        # try:
        #     mail.send(message)
        # except:
        #     return restful.server_error()
        send_email.delay(subject='Blog password email captcha', recipients=email, body='[My Blog] Your captcha is %s' % captcha)
        blogcache.set(email, captcha)
        return restful.success()
    else:
        return restful.params_error(message='Params error!')


@bp.route('/uptoken/')
def uptoken():
    # access 和 secret key 在七牛云的个人中心--密钥管理
    access_key = 'W2ydQ1qDpNZpzJG1SaseiTrgdjpIPNhZ3hfR3cVN'
    secret_key = 'oGG5ocZ9UP66gANQh0eZk9I2odKu1iN9iyGQdKcW'
    # 对象存储仓库名字
    bucket = 'flask-blog'
    q = qiniu.Auth(access_key, secret_key)
    token = q.upload_token(bucket)
    return jsonify({'uptoken': token})
