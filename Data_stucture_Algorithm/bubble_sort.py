# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 18:51
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : bubble_sort.py
# @Documents:

def bubble_sort(li):
    for i in range(0, len(li)-1):
        flag = False  # 标志位
        for j in range(len(li)-1-i):
            if li[j]>li[j+1]:
                li[j], li[j+1]=li[j+1], li[j]
                flag = True    #如果发生改变
        if not flag:    #如果本轮没有发生交换
            return li
    return li


# li = [1, 3, 2, 7, 5]
li = [0, 1, 3, 2, 5, 5, 6, 8]
print(bubble_sort(li))