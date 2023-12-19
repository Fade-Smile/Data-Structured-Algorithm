#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :4.2 栈--链表实现.py
@Author  :Sunshine
@Date    :17/12/2023 13:34 
'''


# 栈 -- 用链表实现

class Node:
    def __init__(self, data, _next=None):
        self.data = data                # 数字域
        self.next = _next               # 指针域


class Stack:
    def __init__(self):
        # 以链表的第一个元素/结点作为栈顶
        self.__top = None                 # 栈顶元素
        self._size = 0                  # 栈的元素个数

    # 判断是否为空
    def is_empty(self):
        return self._size == 0

    # 添加一个元素到栈中
    def push(self, item):
        # 让self.top指向新的节点
        # 让新的节点的next指向原本的栈顶
        self.__top = Node(item, self.__top)
        self._size += 1

    # 弹出栈中的最后一个元素
    def pop(self):
        # 判断栈是否为空
        if self.is_empty():
            raise ValueError('栈为空')
        value = self.__top.data
        self.__top = self.__top.next
        self._size -= 1
        return value

    # 返回栈顶的元素
    def peek(self):
        # 判断栈是否为空
        if self.is_empty():
            raise ValueError('栈为空')
        return self.__top.data

    # 返回栈的长度/大小
    def size(self):
        return self._size


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
