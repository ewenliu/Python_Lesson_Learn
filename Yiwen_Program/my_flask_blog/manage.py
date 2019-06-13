# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 16:28
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : manage.py
# @Documents:

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from my_flask_website import create_app
from exts import db
from apps.cms import models as cms_models

CMSUser = cms_models.CMSUser

app = create_app()

manager = Manager(app)

Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username, password, email):
    user = CMSUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print('cms用户添加成功')


if __name__ == '__main__':
    manager.run()
