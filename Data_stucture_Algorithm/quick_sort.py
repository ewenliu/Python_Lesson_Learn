# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 17:51
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : quick_sort.py
# @Documents:

def partition(li, left, right):
    tmp = li[left]
    while left < right:     # 左右指针未重叠
        while left < right and li[right] > tmp:  #从右边找比tmp小的数
            right -= 1
        li[left] = li[right]    # 找到了，放在左边空位上去
        while left < right and li[left] < tmp:   #从左边找比tmp大的数
            left += 1
        li[right] = li[left]    # 找到了，放在右边空位上去
    li[left] = tmp              #最终左右指针重叠，将tmp归位
    print(li)
    return left

def quick_sort(li, left, right):
    print(left, right)
    if left < right:
        mid = partition(li, left, right)
        print(mid)
        if left < mid-1:    #确保左边比mid-1小，排除left和mid-1相等情况
            quick_sort(li, left, mid-1)
        if mid+1 < right:   #确保右边边比mid+1大，排除right和mid+1相等情况
            quick_sort(li, mid+1, right)


li = [4,1,3,2,7,5,6,8]
# li = [6,5]
quick_sort(li, 0, len(li)-1)
