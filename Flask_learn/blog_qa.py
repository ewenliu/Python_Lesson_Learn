# -*- coding: utf-8 -*-
# @Time          : $ {DATE}
# @Author        : ewen.liu
# @Department    :
# @Function      :

from flask import Flask, render_template, request, redirect, url_for, session
import config
from models import User
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone, User.password==password).first()
        if user:
            session['user_id'] = user.id
            #Should login automatically in next 31 days
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return 'Wrong telephone number or password, please enter again!'


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')

        #Phone number verfication
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return 'This phone number has been registered!'
        else:
            #password should equal to password_confirm
            if password != password_confirm:
                return 'Password is not equal to the password confirm!'
            else:
                user = User(telephone=telephone, username=username, password=password)
                db.session.add(user)
                db.session.commit()
                #If registration successful, then skip to login page
                return redirect(url_for('login'))

@app.route('/logout')
def logout():
    #optional
    #session.pop['user_id']
    #del session['user_id']
    session.clear()
    return redirect(url_for('login'))

@app.route('/question/', methods=['GET', 'POST'])
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        pass

@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}

if __name__ == '__main__':
    app.run()