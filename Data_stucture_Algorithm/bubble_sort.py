# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 18:51
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : bubble_sort.py
# @Documents:

def bubble_sort(li):

    for i in range(0, len(li)-1):
        for j in range(len(li)-1-i):
            if li[j]>li[j+1]:
                li[j], li[j+1]=li[j+1], li[j]
            print(li)
    return li


# li = [1, 3, 2, 7, 5]
li = [4, 1, 3, 2, 7, 5, 6, 8]
bubble_sort(li)