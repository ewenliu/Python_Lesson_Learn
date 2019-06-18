# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 15:56
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : views.py
# @Documents:

from flask import (
    Blueprint,
    views,
    render_template,
    request,
    session,
    redirect,
    url_for,
    g
)
from .forms import LoginForm, ResetpwdForm
from .models import CMSUser
from .decorators import login_required
import config
from exts import db, mail
from flask_mail import Message
from utils import restful
import string
import random


bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')


@bp.route('/logout/')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))


@bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')


@bp.route('/email_captcha/')
def email_captcha():
    # /email_captcha/?email=xxx@xxx.com
    email = request.args.get('email')
    if not email:
        return restful.params_error('请传递邮箱参数！')
    # 给邮箱发送邮件
    source = list(string.ascii_letters)
    source.extend(map(lambda x:str(x), range(0, 10)))
    captcha = ''.join(random.sample(source, 6))

    message = Message('CMS password forget', recipients=[email], body='You captcha is : %s'%captcha)
    try:
        mail.send(message)
    except:
        return restful.server_error()
    return restful.success()


@bp.route('/email/')
def send_mail():
    message = Message('刘逸文是傻逼吗', recipients=['xuefang.zhu@nokia.com'], body='确定过眼神，是傻逼本人')
    mail.send(message)



class LoginView(views.MethodView):

    def get(self, message=None):
        return render_template('cms/cms_login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    # 过期时间31天
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message='邮箱或者密码错误')
        else:
            # 随机取错误信息内容
            message = form.get_error()
            return self.get(message=message)


class ResetPwdView(views.MethodView):
    decorators=[login_required]
    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        form = ResetpwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                return restful.success()
            else:
                return restful.params_error(message='旧密码错误！')
        else:
            message = form.get_error()
            return restful.params_error(message=message)


class ResetEmailView(views.MethodView):
    decorators = [login_required]
    def get(self):
        return render_template('cms/cms_resetemail.html')

    def post(self):
        pass


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))
bp.add_url_rule('/resetemail/', view_func=ResetEmailView.as_view('resetemail'))
