#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :4.12 堆模块--heaqq.py
@Author  :Sunshine
@Date    :23/12/2023 14:38 
'''

import heapq

# 创建一个列表
data = [4, 1, 7, 3, 9, 2]

# 使用 heapify 将列表转换为堆
heapq.heapify(data)

print("堆化后的结果:", data)
print(type(data))

# 向堆中推入元素
heapq.heappush(data, 24)
heapq.heappush(data, 16)
heapq.heappush(data, 78)
heapq.heappush(data, 32)
heapq.heappush(data, 92)
heapq.heappush(data, 26)

print("初始堆:", data)

# 从堆中弹出并返回最小元素
print("弹出最小元素:", heapq.heappop(data))
print("剩余堆:", data)

# 将元素推入堆并弹出堆顶元素
print("推入并弹出:", heapq.heappushpop(data, 5))
print("堆更新后:", data)

# 弹出堆顶元素并推入新元素
print("弹出并推入:", heapq.heapreplace(data, 0))
print("堆更新后:", data)

# 获取可迭代对象中最大/最小的 n 个元素
largest_three = heapq.nlargest(3, data)
smallest_three = heapq.nsmallest(3, data)

print("最大的三个元素:", largest_three)
print("最小的三个元素:", smallest_three)
