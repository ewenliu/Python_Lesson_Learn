# -*- coding: utf-8 -*-
# @Time          : 2019/4/7 15:11
# @Author        : ewen.liu
# @Department    :
# @File          : flaskblog.py.py
# @Function      : Code for Flask tutorial

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)


app.config['SECRET_KEY'] = '647b77c059c0e2990129d962c10f3ae3'

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.debug = True
    app.run()
