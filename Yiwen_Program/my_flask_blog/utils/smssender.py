# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 14:44
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : smssender.py
# @Documents:
import requests


def send(mobile, captcha):
    url = "http://v.juhe.cn/sms/send"
    params = {
        'mobile': mobile,
        'tpl_id': '167536',
        'tpl_value': '#code#=' + captcha,
        'key': '8bfc09b8cf83f09560e3ff40e089d035'
    }
    response = requests.get(url, params)
    response = requests.post(url, params)
    result = response.json()
    if result['error_code'] == 0:
        return True
    else:
        return False
