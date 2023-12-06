#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :1.3 时间复杂度-2.py
@Author  :Sunshine
@Date    :05/12/2023 13:39 
'''

# 用户输入长度为6的数组,数组由1-6六个数字组成顺序随机
# 请返回数字6出现的位置
# 最坏情况 【1, 2, 3, 4, 5, 6】  Ｏ(n)
# 最好情况 【6, 5, 4, 3, 2, 1】  Ｏ(1)
# 平均时间复杂度 (1+2+3+4+5+6)/6 = 21/6 = 7/2   Ｏ(n)

import random

lst = numbers = list(range(1, 7))
random.shuffle(lst)

for i, num in enumerate(lst):
    if num == 6:
        print(f"数字6在数组中的索引为: {i}")
        break
