# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 15:30
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : forms.py
# @Documents:

from wtforms import StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length, EqualTo
from ..forms import BaseForm
from utils import blogcache
from wtforms import ValidationError
from flask import g


class LoginForm(BaseForm):
    email = StringField(
        validators=[Email(message='Please enter right format email'), InputRequired(message='Please enter email')])
    password = StringField(validators=[Length(6, 20, message='Please enter right format password')])
    remember = IntegerField()


class ResetpwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(6, 20, message='Please enter right format old password')])
    newpwd = StringField(validators=[Length(6, 20, message='Please enter right format new password')])
    newpwd2 = StringField(validators=[EqualTo('newpwd')])


class ResetEmailForm(BaseForm):
    email = StringField(validators=[Email(message='Please enter right format email')])
    captcha = StringField(validators=[Length(6, 6, message='Check length of captcha')])

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_cache = blogcache.get(email)
        if not captcha or captcha.lower() != captcha_cache.lower():
            raise ValidationError('Wrong mail captcha')

    def validate_email(self, field):
        email = field.data
        user = g.cms_user
        if user.email == email:
            raise ValidationError('Fail because same to current email address')


class AddBannerForm(BaseForm):
    name = StringField(validators=[InputRequired(message='Please type in banner picture name!')])
    image_url = StringField(validators=[InputRequired(message='Please type in banner picture link!')])
    link_url = StringField(validators=[InputRequired(message='Please type in banner picture skip link!')])
    priority = StringField(validators=[InputRequired(message='Please type in banner picture priority!')])


class UpdateBannerForm(AddBannerForm):
    banner_id = StringField(validators=[InputRequired(message='Please type in banner id')])


class AddBoardForm(BaseForm):
    name = StringField(validators=[InputRequired(message='Please type in board name!')])


class UpdateBoardForm(AddBoardForm):
    board_id = StringField(validators=[InputRequired(message='Please type in board id')])


class DeleteBoardForm(BaseForm):
    board_id = StringField(validators=[InputRequired(message='Please type in board id')])
