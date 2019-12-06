# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 17:28
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : link_list.py
# @Documents:

"""
本代码实现了一个链表节点，并演示了如何进行链表的创建(头插法)和遍历
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


# 头插法创建链表
def create_link_list_head(li):
    head = Node(li[0])
    for i in li[1:]:
        node = Node(i)
        node.next = head
        head = node
    return head


# 尾插法创建链表
def create_link_list_tail(li):
    head = tail = Node(li[0])
    for i in li[1:]:
        node = Node(i)
        tail.next = node
        tail = node
    return head
