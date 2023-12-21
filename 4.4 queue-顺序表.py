#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :4.4 queue-顺序表.py
@Author  :Sunshine
@Date    :21/12/2023 11:56 
'''

# 队列 -- 顺序列表实现


class Queue:
    def __init__(self):
        # 以列表的最后一个元素作为队尾
        self.items = []

    # 判断该是否为空  时间复杂度O(1)
    def isEmpty(self):
        return self.items == []

    # 判断长度  时间复杂度O(1)
    def length(self):
        return len(self.items)

    # 队尾添加元素  时间复杂度O(1)
    def push(self, item):
        self.items.append(item)                       # 从尾部添加, 时间复杂的度 O(1)
        # self.items.insert(0, item)      # 从头部添加, 时间复杂度O(n)

    # 抛出队首  时间复杂度 O(n)
    def pop(self):
        if self.isEmpty():
            raise ValueError('队列是空的')
        return self.items.pop(0)

    # 获取队首的值  时间复杂度O(1)
    def peek(self):
        if self.isEmpty():
            raise ValueError('列表为空')
        return self.items[0]


if __name__ == '__main__':
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    print(queue.length())
    print()
    print(queue.peek())
    print()
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
