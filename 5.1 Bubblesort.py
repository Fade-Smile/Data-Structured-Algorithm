#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.1 Bubblesort.py
@Author  :Sunshine
@Date    :28/12/2023 11:28 
'''


def bubblesort(nums):
    n = len(nums)  # 获取数组的长度
    for i in range(n - 1):
        flag = False  # 表示本轮是否有进行变量交换
        for idx in range(0, n - 1 - i):
            if nums[idx] > nums[idx + 1]:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
                flag = True
            print(f'第{i+1}趟排序:', nums)
        # 如果flag 为False，那说明本轮排序没有进行任何变量交换
        # 数组已经是有序的了
        if not flag:
            break


# 时间复杂度 O(n^2)
# 添加 flag 后  时间复杂度变为O(n)

test = [19, 16, 27, 32, 12, 0, 13]
test1 = [1, 2, 3, 4, 5, 6]
bubblesort(test)
bubblesort(test1)
print(test)
print(test1)
