#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :4.9 Deque-顺序表.py
@Author  :Sunshine
@Date    :23/12/2023 13:23 
'''


# 双端队列 -- 顺序表实现
class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return  self.items == []

    def length(self):
        return len(self.items)

    def add_rear(self, item):
        self.items.append(item)

    def add_front(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    # 返回队首的元素
    def peek(self):
        return self.items[0]


if __name__ == '__main__':
    d = Deque()
    d.add_rear(1)       # 1
    d.add_rear(2)       # 1, 2
    d.add_rear(3)       # 1, 2, 3
    d.add_front(99)     # 99, 1, 2, 3
    d.add_front(98)     # 98, 99, 1, 2, 3
    d.add_front(97)     # 97, 98, 99, 1, 2, 3
    print(d.items)
    f1 = d.remove_front()
    print(f1)           # 97
    r1 = d.remove_rear()
    print(r1)           # 3
    print(d.peek())     # 98
