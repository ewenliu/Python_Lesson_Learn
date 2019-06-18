# -*- coding: utf-8 -*-
# @Time    : 2019/6/18 15:49
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : restful.py
# @Documents:
from flask import jsonify


class HttpCode(object):
    ok = 200
    unautherror = 401
    paramserror = 400
    servererror = 500


def restful_result(code, message, data):
    return jsonify({'code':code, 'message':message, 'data':data or {}})


def success(message='', data=None):
    return restful_result(HttpCode.ok, message=message, data=data)

def unauth_error(message=''):
    return restful_result(HttpCode.unautherror, message=message, data=None)

def params_error(message=''):
    return restful_result(HttpCode.paramserror, message=message, data=None)

def server_error(message=''):
    return restful_result(HttpCode.servererror, message=message or '服务器内部错误', data=None)


