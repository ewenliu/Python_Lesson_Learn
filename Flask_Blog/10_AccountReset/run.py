# -*- coding: utf-8 -*-
# @Time          : 2019/4/7 15:11
# @Author        : ewen.liu
# @Department    :
# @File          : flaskblog.py.py
# @Function      : Code for Flask tutorial

from flaskblog import app

if __name__ == '__main__':
    app.run(debug = True, port=9000)
