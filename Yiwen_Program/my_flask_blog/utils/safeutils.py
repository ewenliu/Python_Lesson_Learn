# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 16:30
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : safeutils.py
# @Documents:

from urllib.parse import urlparse,urljoin
from flask import request

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc