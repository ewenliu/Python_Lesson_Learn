# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 18:17
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : insertion_sort.py
# @Documents:

def insertion_sort(li):
    for i in range(1, len(li)):
        for j in range(i, 0, -1):
            if li[j] < li[j-1]:
                li[j], li[j-1] = li[j-1], li[j]
    return li

li = [1, 3, 2, 7, 5,4]
print(insertion_sort(li))