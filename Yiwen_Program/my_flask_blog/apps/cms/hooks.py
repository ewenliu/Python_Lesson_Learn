# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 19:59
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : hooks.py
# @Documents:

from .views import bp
import config
from flask import session, g
from .models import CMSUser, CMSPermission


@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.get(user_id)
        if user:
            g.cms_user = user

@bp.context_processor
def cms_context_processor():
    # 后台传参给模板
    return {'CMSPermission': CMSPermission}
