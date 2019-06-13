# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 15:49
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : my_flask_website.py
# @Documents:

from flask import Flask
from apps.cms import bp as cms_bp
from apps.front import bp as front_bp
from apps.common import bp as common_bp
import config

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(cms_bp)
app.register_blueprint(front_bp)
app.register_blueprint(common_bp)

if __name__ == '__main__':
    app.run()
