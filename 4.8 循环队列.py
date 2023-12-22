#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :4.8 循环队列.py
@Author  :Sunshine
@Date    :22/12/2023 14:45 
'''


class Queue:

    def __init__(self, size):
        self.items = [None] * size                  # 先声明 长度为 Size 的数据区
        self.head = 0                               # 队首的索引
        self._length = 0                            # 队列的长度
        self.size = size                            # 队列的最大长度

    def is_empty(self):
        return self._length == 0

    def length(self):
        return self._length

    def push(self, item):
        if self.length() == self.size:
            raise ValueError('队列已满')
        # 先算出要添加的元素的索引
        idx = (self.head + self.length()) % self.size
        self.items[idx] = item
        self._length += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('队列为空')
        value = self.items[self.head]
        self.head = (self.head + 1) % self.size
        self._length -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise ValueError('队列为空')
        return self.items[self.head]


if __name__ == '__main__':
    queue = Queue(3)
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.pop())  # 1
    queue.push(4)
    print(queue.length())  # 3
    print(queue.peek())  # 2
    print(queue.pop())  # 2
    print(queue.pop())  # 3
    print(queue.pop())  # 4
    print(queue.length())  # 0
    print(queue.items)   # 虽然这里面有数据[4, 2, 3]， 但对于使用者来说 他们是被删掉的， 而且 length 为0， 那么这个队列就是空的   【这个就是 封装】
