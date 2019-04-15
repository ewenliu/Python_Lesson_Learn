# -*- coding: utf-8 -*-
# @Time          : 2019/4/15 22:25
# @Author        : ewen.liu
# @Department    : 
# @File          : handlers.py
# @Function      :

from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/404.html'), 500



