#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :2.2.1 检测顺序表扩容的增长模式.py
@Author  :Sunshine
@Date    :06/12/2023 23:04 
'''

import sys

lst = []
# print(sys.getsizeof(lst))  # 返回一个对象占用的内存， 以字节为单位  # 输出： 56
# 在Python中，空的列表([])会占用一定的内存空间，因为在创建一个列表时，
# Python需要分配一些内存来存储列表对象的元信息。这些元信息包括列表的长度、容量、引用计数等等。

init_allocated = sys.getsizeof(lst)  # 初始容量
for i in range(1, 100):
    lst.append(i)
    now_allocated = sys.getsizeof(lst) - init_allocated
    print(f'当前的元素是:{i}, 当前的占用内存: {now_allocated} 字节, 当前的容量是: {now_allocated // 8}')

    # The growth pattern is: 0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...

