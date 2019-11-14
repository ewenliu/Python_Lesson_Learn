# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 15:25
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : blog.py
# @Documents:

from flask import Flask
import config
from apps.cms import bp as cms_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp
from ueditor import bp as ueditor_bp
from exts import db, mail
from flask_wtf import CSRFProtect


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object(config)
    flask_app.register_blueprint(cms_bp)
    flask_app.register_blueprint(common_bp)
    flask_app.register_blueprint(front_bp)
    flask_app.register_blueprint(ueditor_bp)
    db.init_app(flask_app)
    mail.init_app(flask_app)
    CSRFProtect(flask_app)

    return flask_app


app = create_app()


if __name__ == '__main__':
    app = create_app()
    app.run()
