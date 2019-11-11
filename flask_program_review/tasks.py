# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 15:59
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : tasks.py
# @Documents:

# --pool=solo不是并发，只能作为测试用
# 在windows运行本文件命令行代码：D:\learn_tmp\flask_program_review>celery -A tasks.celery --pool=solo worker --loglevel=info
# 在linux运行本文件命令行代码：Dcelery -A tasks.celery worker --loglevel=info

from celery import Celery
from flask_mail import Message
from exts import mail
from flask import Flask
import config


flask_app = Flask(__name__)
flask_app.config.from_object(config)
mail.init_app(flask_app)


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery = make_celery(flask_app)


@celery.task
def send_email(subject='ewen blog mail send system', recipients='kevin.2.liu@nokia-sbell.com', body='Email captcha test'):
    message = Message(subject=subject, recipients=[recipients],
                      body=body)
    mail.send(message)
    return 'Success'
