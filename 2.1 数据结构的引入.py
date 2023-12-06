#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :2.1 数据结构的引入.py
@Author  :Sunshine
@Date    :06/12/2023 20:13 
'''

# 根据英雄名推荐英雄的推荐出装
# 存储英雄，以及他对应的出装

foo = [
    ['英雄名', ['出装1', '出装2', '出装3']],
    ['亚索', ['电刀', '攻速鞋', '无尽']]
]

name = '亚索'

for item in foo:
    if item[0] == name:
        print(item[1])
# 第一种方式 : 列表, 时间复杂度是 Ｏ(n)

foo1 = {
    '亚索': ['电刀', '攻速鞋', '无尽'],
    'EZ': ['魔宗', '三项', 'CD鞋']
}


class Hero:
    def __init__(self):
        self.data = {

        }

    def add(self):
        pass

    def remove(self):
        pass

    def modify(self):
        pass

    def get(self):
        pass


print(foo1['EZ'])
# 第二种方式 : 字典, 时间复杂度 Ｏ(1)