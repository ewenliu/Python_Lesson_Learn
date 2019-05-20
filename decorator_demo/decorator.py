# -*- coding: utf-8 -*-
# @Time          : 2019/5/20
# @Author        : ewen.liu
# @Department    :
# @Function
#装饰器其实就是一个函数
#有两个特别之处
#1. 参数是一个函数
#2. 返回值是一个函数

#在所有的函数执行之前，先打印一个hello world


#@装饰器在这里等同于
#run = my_log(run) = wrapper
#即run()等效于wrapper()

@my_log
def run():
    print ('run')

@my_log
def add(a, b):
    c = a + b
    print ('Result is %d' % c)

#def my_log(func):
#
#     def wrapper():
#         print('Hello world')
#         func()
#
#     return wrapper
# # add(1, 2)
#TypeError: wrapper() takes 0 positional arguments but 2 were given
#改写装饰器函数

# def my_log(func):
#
#     def wrapper(a,b):
#         print('Hello world')
#         func(a,b)
#
#     return wrapper
# run()
# Traceback (most recent call last):
#   File "D:/Python_Lesson_Learn/Python_Lesson_Learn/decorator_demo/decorator.py", line 53, in <module>
#     run()
# TypeError: wrapper() missing 2 required positional arguments: 'a' and 'b'
#会影响不需要参数的函数，则改写装饰器函数
run()
add(2,4)