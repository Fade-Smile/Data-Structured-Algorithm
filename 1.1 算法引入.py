#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :1.1 算法引入.py
@Author  :Sunshine
@Date    :05/12/2023 02:47 
'''

# 如果 a+b+c=1000，且 a^2+b^2=c^2 (a,b,c 为自然数)，如何求出所有a、b、c可能的组合?

# 第一步 分析需求

# 找到所有满足以上两个条件的 a, b, c 的组合


# 第二步 设计算法

# 尝试o,b,c的所有组合,判断当前的组合是否满足以上两个条件,如果满足,就输出，否则就尝试下一个组合
# 枚举法

# 第三步 代码实现


import time

start = time.time()

for a in range(1001):
    for b in range(1001):
        for c in range(1001):
            if (a + b + c == 1000) and (a**2 + b**2 == c**2):
                print(f'组合{a}, {b}, {c} 满足条件')

end = time.time()
print(end-start)

# 第四步 验证结果
