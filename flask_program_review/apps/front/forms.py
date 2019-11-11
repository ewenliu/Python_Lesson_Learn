# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 15:30
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : forms.py
# @Documents:
from ..forms import BaseForm
from wtforms.validators import Email, Length, Regexp, EqualTo, InputRequired
from wtforms import StringField, ValidationError, IntegerField
from utils import blogcache


class SignupForm(BaseForm):
    email = StringField(validators=[Email(message='Please enter right format email')])
    email_captcha = StringField(validators=[Length(6, 6, message='Please check email captcha')])
    # 用户名只需要长度2-20之间的任意字符即可
    username = StringField(validators=[Regexp(r".{2,20}", message='Please enter right format username')])
    # 密码必须由大小写和数字组成，最少6位，最多20位
    password = StringField(validators=[Length(6, 20, message='Please enter right format password')])
    password_confirm = StringField(validators=[EqualTo('password', message='Wrong password confirm')])
    # 图形验证码由任意4个字符组成
    graph_captcha = StringField(validators=[Regexp(r"\w{4}", message='Please enter right format graph captcha')])

    def validate_email_captcha(self, field):
        email_captcha = field.data
        email = self.email.data
        email_captcha_cache = blogcache.get(email)
        if not email_captcha_cache or email_captcha.lower() != email_captcha_cache.lower():
            raise ValidationError('Wrong mail captcha')

    def validate_graph_captcha(self, field):
        graph_captcha = field.data
        if not blogcache.get(graph_captcha):
            raise ValidationError('Wrong graph captcha')


class SigninForm(BaseForm):
    email = StringField(validators=[Email(message='Please enter right format email')])
    password = StringField(validators=[Length(6, 20, message='Please enter right format password')])
    remember = StringField()


class AddPostForm(BaseForm):
    title = StringField(validators=[InputRequired(message='Please enter title')])
    content = StringField(validators=[InputRequired(message='Please enter content')])
    board_id = IntegerField(validators=[InputRequired(message='Please enter board id')])


class AddCommentForm(BaseForm):
    content = StringField(validators=[InputRequired(message='Please enter content')])
    post_id = IntegerField(validators=[InputRequired(message='Please enter post id')])
