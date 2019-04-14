# -*- coding: utf-8 -*-
# @Time          : 2019/4/7 15:11
# @Author        : ewen.liu
# @Department    :
# @Function      : 

from flask import render_template, request, Blueprint
from flaskblog.models import Post


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.data_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts = posts)


@main.route("/about")
def about():
    return render_template('about.html', title = 'About')