# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 20:31
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : maze_solved_by_stack.py
# @Documents:

"""
本代码用栈来解决迷宫问题，即深度优先搜索

如下图所示迷宫maze，1代表墙表示不能走，0则表示可以走
"""

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# 定义栈
class Stack(object):

    # 初始化一个空栈
    def __init__(self):
        self.__stack = []

    # 入栈
    def push(self, element):
        # 在列表尾部追加一个数据
        self.__stack.append(element)

    # 出栈
    def pop(self):
        # 删除并弹出列表最后的数据
        return self.__stack.pop()

    # 获取栈顶元素
    def get_top(self):
        if len(self.__stack) > 0:
            return self.__stack[-1]
        else:
            return None

    # 判断是否空栈
    def is_empty(self):
        return len(self.__stack) == 0


    # 获取当前栈的内容
    def get_content(self):
        return self.__stack


# 上下左右四个方向的表示, dir=direction
# 上: (x-1, y) 下: (x+1, y) 左: (x, y-1) 右: (x, y+1)
# 约定的方向优先级是 : 顺时针方向  上-->右-->下-->左
dirs = [
    lambda x,y: (x-1, y),  # 上
    lambda x,y: (x, y+1),  # 右
    lambda x,y: (x+1, y),  # 下
    lambda x,y: (x, y-1)   # 左
]


# 0 表示可以走，1表示不能走，2表示已经走过
# (x1,y1)代表迷宫路径的开始位置，(x2, y2)代表迷宫路径的结束位置
def maze_path_solved_by_stack(x1, y1, x2, y2):
    # 初始化一个空栈
    stack = Stack()
    # 先把起始位置压入栈
    stack.push((x1, y1))
    # 如果栈为空，说明无路可走
    while(not stack.is_empty()):
        # 获取栈顶元素，也即当前位置
        current_position = stack.get_top()
        # 如果当前位置已经到达结束位置，则打印路径
        if current_position[0] == x2 and current_position[1] == y2:
            print('当前走过的路径列表如下：')
            print(stack.get_content())
            return True
        # 如果还没到结束位置，按照上右下左的顺序遍历相邻节点
        for dir in dirs:
            next_position = dir(current_position[0], current_position[1])
            # 如果当前遍历到的相邻位置可以走，将此相邻位置压入栈，结束本次for循环
            if maze[next_position[0]][next_position[1]] == 0:
                stack.push(next_position)
                # 标记当前遍历到的相邻位置已经走过
                maze[next_position[0]][next_position[1]] = 2
                break

        else:
            # maze[current_position[0]][current_position[1]] = 2
            stack.pop()
    else:
        print('起点不能走到终点')
        return False


maze_path_solved_by_stack(1,1,8,8)
