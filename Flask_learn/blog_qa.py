# -*- coding: utf-8 -*-
# @Time          : $ {DATE}
# @Author        : ewen.liu
# @Department    :
# @Function      :

from flask import Flask, render_template, request, redirect, url_for, session
import config
from models import User, Question, Answer
from exts import db
from decorators import login_required

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    context = {
        'questions' : Question.query.order_by('create_time').all()
    }
    return render_template('index.html', **context)

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
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id==user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/detail/<question_id>/')
def detail(question_id):
    question_model = Question.query.filter(Question.id==question_id).first()
    return render_template('detail.html', question=question_model)

@app.route('/add_answer/', methods=['POST'])
@login_required
def add_answer():
    comments_content = request.form.get('comments_content')
    question_id = request.form.get('question_id')
    answer = Answer(content=comments_content)
    user_id = session.get('user_id')
    user = User.query.filter(User.id==user_id).first()
    answer.author = user

    question=Question.query.filter(Question.id==question_id).first()
    answer.question=question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))


@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)