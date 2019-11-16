# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 19:32
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : models.py
# @Documents:
from exts import db
from datetime import datetime


class BannerModel(db.Model):
    __tablename__ = 'banner'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    link_url = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime, default=datetime.now)


class BoardModel(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)


class PostModel(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    num_comment = db.Column(db.Integer, default=0, nullable=False)

    board_id = db.Column(db.Integer, db.ForeignKey("board.id"))
    author_id = db.Column(db.String(100), db.ForeignKey("front_user.id"), nullable=False)

    board = db.relationship('BoardModel', backref='posts')
    author = db.relationship('FrontUser', backref='posts')


class HighlightPostModel(db.Model):
    __tablename__ = 'highlight_post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id", ondelete='CASCADE'))
    create_time = db.Column(db.DateTime, default=datetime.now)

    post = db.relationship('PostModel', backref='highlight')



class CommentModel(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id", ondelete='CASCADE'))
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.String(100), db.ForeignKey("front_user.id"), nullable=False)

    post = db.relationship('PostModel', backref='comments')
    author = db.relationship('FrontUser', backref='comments')
