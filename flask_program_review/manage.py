# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 15:27
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : manage.py
# @Documents:

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from blog import create_app
from exts import db
from apps.cms import models as cms_models
from apps.front import models as front_models
from apps import models as app_models

CMSUser = cms_models.CMSUser
CMSRole = cms_models.CMSRole
CMSPermission = cms_models.CMSPermission

FrontUser = front_models.FrontUser

app = create_app()

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


# python manage.py create_cms_user -u xxx -p xxx -e xxx
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username, password, email):
    user = CMSUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()


# python manage.py create_role
@manager.command
def create_role():
    # 1.访问者，可以修改个人信息
    visitor = CMSRole(name='visitor', desc='only visit permission')
    visitor.permissions = CMSPermission.VISITOR
    # 2.运营，可以修改个人信息，管理post，comments，前台用户
    operator = CMSRole(name='operator', desc='manage info, posts, comments permissions')
    operator.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.COMMENTER | \
                           CMSPermission.FRONTUSER
    # 3.管理员，拥有绝大部分权限
    admin = CMSRole(name='admin', desc='own most permissions')
    admin.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.COMMENTER | \
                        CMSPermission.BOARDER | CMSPermission.FRONTUSER | CMSPermission.CMSUSER
    # 4.开发者，拥有全部权限
    developer = CMSRole(name='developer', desc='own all permissions')
    developer.permissions = CMSPermission.ALL_PERMISSION

    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()


@manager.option('-e', '--email', dest='email')
@manager.option('-n', '--name', dest='name')
def add_user_to_role(email, name):
    user = CMSUser.query.filter_by(email=email).first()
    if user:
        role = CMSRole.query.filter_by(name=name).first()
        if role:
            role.users.append(user)
            db.session.commit()
            print('Add user to role successfully')
        else:
            print('No such role')
    else:
        print('No such user')


@manager.command
def test_permission():
    user = CMSUser.query.filter_by(id=2).first()
    if user.has_permission(CMSPermission.VISITOR):
        print('Has visit permission')
    else:
        print('Does not have visit permission')

#  ------------------------------------------------------- #
#  ------------------------------------------------------- #
#  ---------------下面是前台用户相关操作-------------------- #
#  ------------------------------------------------------- #
#  ------------------------------------------------------- #
@manager.option('-e', '--email', dest='email')
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
def create_front_user(email, username, password):
    user = FrontUser(email=email, username=username, password=password)
    db.session.add(user)
    db.session.commit()


@manager.command
def create_test_post():
    pass
    for i in range(1, 300):
        title = 'Title %s' %i
        content = 'Content %s' %i
        board = app_models.BoardModel.query.first()
        author = FrontUser.query.first()
        post = app_models.PostModel(title=title, content=content)
        post.board = board
        post.author = author
        db.session.add(post)
        db.session.commit()


if __name__ == '__main__':
    manager.run()
