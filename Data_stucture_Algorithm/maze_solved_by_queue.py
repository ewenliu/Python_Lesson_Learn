# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 16:20
# @Author  : Liu Yiwen
# @Email   : ewen.liu@outlook.com
# @File    : maze_solved_by_queue.py
# @Documents:

"""
本代码用队列来解决迷宫问题，即广度优先搜索

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

from collections import deque


# 上下左右四个方向的表示, dir=direction
# 上: (x-1, y) 下: (x+1, y) 左: (x, y-1) 右: (x, y+1)
# 约定的方向优先级是 : 顺时针方向  上-->右-->下-->左
dirs = [
    lambda x,y: (x-1, y),  # 上
    lambda x,y: (x, y+1),  # 右
    lambda x,y: (x+1, y),  # 下
    lambda x,y: (x, y-1)   # 左
]


# 用来打印路径
def print_r(path):
    real_path = []
    # 取path最后一个值的索引
    i = len(path) - 1
    # 只要还没到起点位置，即-1
    while i>=0:
        # path[i][0:2]获取坐标位置
        real_path.append(path[i][0:2])
        # 获取当前坐标的来源位置
        i = path[i][2]
    real_path.reverse()
    print(real_path)

def maze_path_solved_by_queue(x1, y1, x2, y2):
    queue = deque()
    # path用来记录所有走过的迷宫节点，格式是（x坐标，y坐标，当前节点来源于path第几个节点）
    path = []
    # 入队第一个元素，由于是第一个，所以没有来源节点，故为-1
    queue.appendleft((x1, y1, -1))
    # 只要队里还有东西
    while len(queue) > 0:
        current_position = queue.popleft()
        # 将当前访问的节点存入path
        path.append(current_position)

        # 如果当前访问到的节点等于（x2, y2），表示已经走到了终点，循环结束
        if current_position[0] == x2 and current_position[1] == y2:
            print('可以走到终点且路径如下')
            print_r(path)
            return True

        # 如果当前节点不是终点，那么遍历当前节点的4个方向
        for direction in dirs:
            next_position = direction(current_position[0], current_position[1])
            # 判断下一个位置是否是可以走的，0表示可以走，1表示墙，不能走
            if maze[next_position[0]][next_position[1]] == 0:
                # 入队, len(path)-1)用来指示当前节点是由那个节点来的
                queue.append((next_position[0], next_position[1], len(path)-1))
                # 标记已走过为2避免重复走
                maze[next_position[0]][next_position[1]] = 2

    # 如果while里面没有return，说明没有碰到终点
    return False

maze_path_solved_by_queue(1,1,8,8)
