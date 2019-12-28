# -*- coding: utf-8 -*-#
# 目的：演示多线程之间通过队列进行通信

from threading import Thread
from queue import Queue
import random
import time


class Producer(Thread):

    def __init__(self, queue):
        super(Producer, self).__init__()
        self.queue = queue

    def run(self):
        for i in range(100):
            item = random.randint(0, 256)
            self.queue.put(item=item)
            print('Produce %s items\n' % item)
        for i in range(3):
            self.queue.put('Null')

class Consumer(Thread):

    def __init__(self, queue):
        super(Consumer, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            if item == 'Null':
                print('%s break' % self.name)
                break
            print('Consumer %s pop % items\n' % (self.name, item))
            self.queue.task_done()


if __name__ == '__main__':
    q = Queue()
    producer = Producer(q)
    consumer1 = Consumer(q)
    consumer2 = Consumer(q)
    consumer3 = Consumer(q)

    producer.start()
    consumer1.start()
    consumer2.start()
    consumer3.start()

    producer.join()
    consumer1.join()
    consumer2.join()
    consumer3.join()
