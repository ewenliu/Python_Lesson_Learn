# -*- coding: utf-8 -*-#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import string
import random
from functools import wraps
import time


app = Flask(__name__)


DB_DIALECT = 'mysql'
DB_DRIVER = 'mysqldb'
DB_USERNAME = 'root'
DB_PASSWORD = 'hduewen1122!'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_DATABASE = 'sql_optimize'

SQLALCHEMY_DATABASE_URI: str = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DB_DIALECT, DB_DRIVER,
                                                                            DB_USERNAME, DB_PASSWORD,
                                                                            DB_HOST, DB_PORT,
                                                                            DB_DATABASE)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Course(db.Model):
    __tablename__ = 'course'
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cname = db.Column(db.String(20))
    tid = db.Column(db.Integer)


class Teacher (db.Model):
    __tablename__ = 'teacher'
    tid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tname = db.Column(db.String(20))
    tcid = db.Column(db.Integer)


class TeacherCard (db.Model):
    __tablename__ = 'teacherCard'
    tcid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tcdesc = db.Column(db.String(200))


# 时间装饰器
def time_cal(func):
    @wraps(func)
    def inner():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print('总共花了%f秒' % (end-start))
    return inner


# 清空所有表
def drop_tables():
    db.drop_all()
    print('Drop tables finished!')


# 创建所有表
def create_tables():
    db.create_all()
    print('Create tables finished!')


# 创建测试数据
# 数据各4条
@time_cal
def create_course_data():
    cname_l = ['python', 'sql', 'c++', 'javascript']
    tid_l = [1, 2, 3, 4]
    for (cname, tid) in zip(cname_l, tid_l):
        course = Course(cname=cname, tid=tid)
        db.session.add(course)
    db.session.commit()


@time_cal
def create_teacher_data():
    tname_l = ['a', 'b', 'c', 'd']
    tcid_l = [1, 2, 3, 4]
    for (tname, tcid) in zip(tname_l, tcid_l):
        teacher = Teacher(tname=tname, tcid=tcid)
        db.session.add(teacher)
    db.session.commit()


@time_cal
def create_teacher_card_data():
    for i in range(4):
        t_c = TeacherCard(tcdesc='no desc')
        db.session.add(t_c)
    db.session.commit()


if __name__ == '__main__':
    drop_tables()
    create_tables()
    create_course_data()
    create_teacher_data()
    create_teacher_card_data()
