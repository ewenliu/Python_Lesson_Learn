# -*- coding: utf-8 -*-
# @Time          : 2019/4/7 15:11
# @Author        : ewen.liu
# @Department    :
# @File          : flaskblog.py.py
# @Function      : Code for Flask tutorial

from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author' : 'Ewen Liu',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'April 7, 2019'
    },
    {
        'author' : 'Ewen Lee',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'April 8, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.debug = True
    app.run()
