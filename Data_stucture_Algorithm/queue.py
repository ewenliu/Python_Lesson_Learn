# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 17:04
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : queue.py
# @Documents:

"""
本代码用来实现一个环形队列对象，
以逆时针为方向，即入队和出队都走逆时针
"""

class Queue():

    # 指定队列的长度，初始化一个队列
    def __init__(self, size):
        # 不希望__queue能被直接访问
        self.__queue = [0 for _ in range(size)]
        self.__size = size
        self.__rear = 0
        self.__front = 0

    # 入队，队尾往后走一步
    def push(self, element):
        # 如果队不是满的，才执行入队操作
        if not self.is_full():
            # 环形队列，入队需要对队尾进行取模操作，不然队尾指针会溢出队列的长度
            # 队尾指针移动
            self.__rear = (self.__rear + 1) % self.__size
            self.__queue[self.__rear] = element
        # 如果队满，抛出异常
        else:
            raise IndexError('队满，无法入队')

    # 出队，队首往后走一步
    def pop(self):
        # 如果队不是空的，才执行出队操作
        if not self.is_empty():
            # 环形队列，出队需要对队首进行取模操作，不然队首指针会溢出队列的长度
            self.__front = (self.__front + 1) % self.__size
            return self.__front
        # 如果队列是空的，则队内没有元素，抛出异常
        # 如果队列是空的，则队内没有元素，抛出异常
        else:
            raise IndexError('队空，无法出队')

    # 环形队列队空的条件是队尾指针和队首指针重叠
    def is_empty(self):
        return self.__rear == self.__front

    # 环形队列队满的条件是队尾
    def is_full(self):
        return (self.__rear + 1) % self.__size == self.__front

q = Queue(4)
for i in range(3):
    q.push(i)

print(q.is_full())
print(q.pop())
print(q.pop())
