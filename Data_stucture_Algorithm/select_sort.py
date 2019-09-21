# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 11:15
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : select_sort.py
# @Documents:

def select_sort(li):
    for i in range(0, len(li)-1):
        for j in range(i+1, len(li)):  #从i后面开始选取元素
            if li[j] < li[i]:  #每次都和i位置元素比较
                li[j], li[i] = li[i], li[j]
    return li

li = [6, 3, 2, 7, 5]
print(select_sort(li))