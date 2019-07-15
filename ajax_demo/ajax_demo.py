# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 16:53
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : ajax_demo.py
# @Documents:

from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('//')
def index():
    return 'hello!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'ewenliu' and password == '123456':
            return jsonify({'code':200, 'message':''})
        else:
            return jsonify({'code':401, 'message':'用户名或密码错误'})


if __name__ == '__main__':
    app.run(debug=True)