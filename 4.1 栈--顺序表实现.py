#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :4.1 栈--顺序表实现.py
@Author  :Sunshine
@Date    :17/12/2023 13:09 
'''

# 栈 -- 用顺序表实现
class Stack():
    def __init__(self):
        # 把列表的第一个元素作为栈顶
        # 把列表的最后一个元素作为栈顶
        self.__data =[]

    # 判断是否为空
    def is_empty(self):
        return self.__data == []

    # 添加一个元素到栈中
    def push(self, item):
        # append, insert
        self.__data.append(item)                   # 时间复杂度 O(1)
        # self.__data.insert(0, item)              # 时间复杂度 O(n)

    # 弹出栈中的最后一个元素
    def pop(self):
        # 判断栈是否为空
        if self.is_empty():
            raise ValueError('栈为空')
        return self.__data.pop()

    # 返回栈顶的元素
    def peek(self):
        # 判断栈是否为空
        if self.is_empty():
            raise ValueError('栈为空')
        return self.__data[-1]

    # 返回栈的长度/大小
    def size(self):
        return len(self.__data)


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






