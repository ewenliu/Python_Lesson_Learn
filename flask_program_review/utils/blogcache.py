# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 16:02
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : blogcache.py
# @Documents:
import memcache

cache = memcache.Client(['127.0.0.1:11211'], debug=True)

def set(key, value, timeout=300):
    return cache.set(key, value, timeout)

def get(key):
    return cache.get(key)

def delete(key):
    return cache.delete(key)
