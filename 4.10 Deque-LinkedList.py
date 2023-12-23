#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :4.10 Deque-LinkedList.py
@Author  :Sunshine
@Date    :23/12/2023 13:34 
'''

# 双端队列 -- 链表实现
from collections import deque   # 这里的deque 数双端循环队列， python内置


class Node:
    def __init__(self, data, _next=None):
        self.data = data            # 数值域
        self.next = _next           # 指针域


class Deque:
    def __init__(self):
        self.head = None            # 队首
        self.rear = None            # 队尾
        self._length = 0            # 队列长度

    def is_empty(self):
        return self._length == 0

    def length(self):
        return self._length

    # 遍历列表
    def loop_item(self):
        cur = self.head
        while cur:
            print(cur.data, '->', end=' ')
            cur = cur.next

    # 往队尾添加一个元素
    def add_rear(self, item):
        node = Node(item)
        # 情况一: 队列为空
        if self.is_empty():
            self.head = node
            self.rear = node
        # 情况二: 队列不为空
        else:
            self.rear.next = node
            self.rear = node
        self._length += 1

    # 往队首添加一个元素
    def add_front(self, item):
        node = Node(item)
        # 情况一: 队列为空
        if self.is_empty():
            self.head = node
            self.rear = node
        # 情况二: 队列不为空
        else:
            node.next = self.head
            self.head = node
        self._length += 1

    #  弹出队首元素
    def pop_front(self):
        if self.is_empty():
            raise ValueError('双端队列为空')
        value = self.head.data
        self.head = self.head.next
        self._length -= 1
        if self._length == 0:
            self.rear = None
        return  value

    # 弹出队尾元素
    def pop_rear(self):
        if self.is_empty():
            raise ValueError('双端队列为空')
        if self.length() == 1:
            return self.pop_front()
        cur = self.head
        value = self.rear.data
        while cur.next != self.rear:
            cur = cur.next
        self.rear = cur
        cur.next = None
        self._length -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise ValueError("双端队列为空")
        return self.head.data


if __name__ == '__main__':
    d = Deque()
    # print(d.pop_rear())
    # print(d.pop_front())
    # print(d.peek())

    d.add_front(1)
    d.add_front(2)
    print('当前队首元素为: ', d.head.data)
    print('当前队尾元素为: ', d.rear.data)
    d.add_front(3)
    print('当前队首元素为: ', d.head.data)
    print('当前队尾元素为: ', d.rear.data)
    d.add_rear(98)
    print('当前队尾元素为: ', d.rear.data)
    print(d.loop_item())

    print('目前队列长度为: ', d.length())
    f1 = d.pop_front()
    print('队首弹出: ', f1)
    print(d.loop_item())
    r1 = d.pop_rear()
    print('队尾弹出: ', r1)
    print('目前队列长度为: ', d.length())
    print('当前队列的首元素为: ', d.peek())

    print(d.loop_item())
