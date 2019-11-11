# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 15:45
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : hooks.py
# @Documents:
from flask import session, g
from .views import bp
from .models import CMSUser, CMSPermission
import config


@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.get(user_id)
        if user:
            g.cms_user = user

# 有了下面这个上下文处理器和所有cms有关的模板文件，都能访问CMSPermission这个类
@bp.context_processor
def cms_context_processor():
    return {"CMSPermission": CMSPermission}
