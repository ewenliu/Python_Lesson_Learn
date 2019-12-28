# -*- coding: utf-8 -*-#
# 目的：测试没有锁多线程是怎么跑的


import threading
num = 0


def producer(count):
    global num
    for i in range(count):
        num += 1


def consumer(count):
    global num
    for i in range(count):
        num -= 1


if __name__ == '__main__':

    count = 1000000

    thread_add = threading.Thread(target=producer, args=(count,))
    thread_minus = threading.Thread(target=consumer, args=(count,))

    thread_add.start()
    thread_minus.start()

    thread_add.join()
    thread_minus.join()

    print('Finally num: \n')
    print(num)
