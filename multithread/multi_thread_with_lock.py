# -*- coding: utf-8 -*-#
# 目的：测试有锁的多线程是怎么跑的


import threading
num = 0


def producer(count, lock):
    global num
    for i in range(count):
        lock.acquire()
        num += 1
        lock.release()


def consumer(count, lock):
    global num
    for i in range(count):
        lock.acquire()
        num -= 1
        lock.release()


if __name__ == '__main__':

    count = 1000000
    lock = threading.Lock()

    thread_add = threading.Thread(target=producer, args=(count, lock, ))
    thread_minus = threading.Thread(target=consumer, args=(count, lock, ))

    thread_add.start()
    thread_minus.start()

    thread_add.join()
    thread_minus.join()

    print('Finally num: \n')
    print(num)
