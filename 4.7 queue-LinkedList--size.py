#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :4.7 queue-LinkedList -- size.py
@Author  :Sunshine
@Date    :22/12/2023 14:12
'''


# 队列 -- 链表实现 (size 属性)

class Node:
    def __init__(self, data, _next=None):
        self.data = data  # 数字域
        self.next = _next  # 指针域


class Queue:
    def __init__(self, size):
        self.head = None  # 队列的队头
        self.rear = None  # 队列的队尾
        self._length = 0  # 队列的长度
        self.size = size  # 队列的最大长度

    # 判断该是否为空  时间复杂度O(1)
    def isEmpty(self):
        return self._length == 0

    # 判断长度    时间复杂度O(1)
    def length(self):
        return self._length

    # 队尾添加元素   时间复杂度O(1)
    def push(self, item):
        # 判断队列是否已满
        if self.length() == self.size:
            raise ValueError('队列已满')
        node = Node(item)
        # 如果队列为空
        if self.isEmpty():
            self.head = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self._length += 1

    # 抛出队首  时间复杂度O(1)
    def pop(self):
        if self.isEmpty():
            raise ValueError('队列是空的')
        value = self.head.data
        self.head = self.head.next
        self._length -= 1
        return value

    # 获取队首的值  时间复杂度O(1)
    def peek(self):
        if self.isEmpty():
            raise ValueError('列表为空')
        return self.head.data


if __name__ == '__main__':
    queue = Queue(3)
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.pop()) # 1
    print()
    queue.push(4)
    print(queue.length()) # 3
    print()
    print(queue.peek()) # 2
    print()
    print(queue.pop()) # 2
    print(queue.pop()) # 3
    print(queue.pop()) # 4
    # print(queue.pop()) # 空

