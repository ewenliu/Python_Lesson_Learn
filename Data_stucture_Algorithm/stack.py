# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 20:48
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : stack.py
# @Documents:

"""
本代码实现了一个栈对象，并用栈来实现一个括号匹配问题的解决
"""


# 定义栈
class Stack(object):

    # 初始化一个空栈
    def __init__(self):
        self.stack = []

    # 入栈
    def push(self, element):
        # 在列表尾部追加一个数据
        self.stack.append(element)

    # 出栈
    def pop(self):
        # 删除并弹出列表最后的数据
        self.stack.pop()

    # 获取栈顶元素
    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    # 判断是否空栈
    def is_empty(self):
        return len(self.stack) == 0


"""
brace_match只实现匹配仅包含括号的输入
"""


def brace_match(s):
    # 创建一个匹配字典，即右括号只能匹配对应的左括号
    match = {'}': '{', ']': '[', ')': '('}
    # 初始化一个空栈
    stack = Stack()
    # 遍历输入的元素, e=element
    for e in s:
        # 如果元素是左括号，那么入栈
        if e in ['{', '[', '(']:
            stack.push(e)
        # 如果元素是右括号
        else:
            # 来了有括号，但栈是空的，则直接返回不匹配
            if stack.is_empty():
                return False
            # 如果栈不为空, 且当前遍历到的括号能和栈顶元素匹配，如：当前栈顶是'('，遍历到的括号是')'，那么栈顶出栈
            elif stack.get_top() == match[e]:
                stack.pop()
            # 如果栈不为空，且当前遍历到的括号不能和栈顶元素匹配，则直接返回不匹配
            else:
                return False
    # 遍历完之后，判断栈是否为空，如果为空，那么返回匹配成功，如果不能空，返回不匹配
    if stack.is_empty():
        return True
    else:
        return False


print(brace_match('[[]])'))  # False
print(brace_match('[[]](){[]}'))  # True
