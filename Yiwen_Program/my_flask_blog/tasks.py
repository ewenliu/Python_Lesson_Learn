# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 15:18
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : tasks.py
# @Documents:

# 运行本文件：
# 在windows操作系统上：
# celery -A tasks.celery worker --pool=solo --loglevel=info
# 在类*nix操作系统上：
# celery -A tasks.celery worker --loglevel=info


from celery import Celery
from flask_mail import Message
from exts import mail
from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)
mail.init_app(app)

def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


celery = make_celery(app)


@celery.task
def send_mail(subject, recipients, body):
    message = Message(subject=subject, recipients=recipients, body=body)
    mail.send(message)