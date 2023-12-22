#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :4.6 queue-顺序表--size.py
@Author  :Sunshine
@Date    :22/12/2023 14:18
'''

# 队列 -- 顺序列表实现


class Queue:
    def __init__(self, size):
        # 以列表的最后一个元素作为队尾
        self.items = []
        self.size = size # 队列的最大长度

    # 判断该是否为空  时间复杂度O(1)
    def isEmpty(self):
        return self.items == []

    # 判断长度  时间复杂度O(1)
    def length(self):
        return len(self.items)

    # 队尾添加元素  时间复杂度O(1)
    def push(self, item):
        # 判断队列是否已满
        if self.length() == self.size:
            raise ValueError('队列已满')
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
    queue = Queue(3)
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.pop())  # 1
    print()
    queue.push(4)
    print(queue.length())  # 3
    print()
    print(queue.peek())  # 2
    print()
    print(queue.pop())  # 2
    print(queue.pop())  # 3
    print(queue.pop())  # 4
