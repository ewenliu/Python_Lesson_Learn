# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 11:09
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : restful.py
# @Documents:
from flask import jsonify


class HttpCode(object):
    ok = 200
    unautherror = 401
    paramerror = 400
    servererror = 500


def restful_result(code, message, data=None):
    return jsonify({'code': code, 'message': message, 'data': data or {}})


# 只有在请求成功的情况下返回data数据
def success(message='', data=None):
    return restful_result(code=HttpCode.ok, message=message, data=data)


def unauth_error(message=''):
    return restful_result(code=HttpCode.unautherror, message=message)


def params_error(message=''):
    return restful_result(code=HttpCode.paramerror, message=message)


def server_error(message=''):
    return restful_result(code=HttpCode.servererror, message=message or 'Server internal error!')
