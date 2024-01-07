#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.9 BinarySearch-While-Loop.py
@Author  :Sunshine
@Date    :07/01/2024 14:02 
'''
# 时间复杂度为 O(log n)


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        # 如果找到目标值，则返回索引
        if arr[mid] == target:
            return True

        # 如果目标值比中间元素小，则在左半部分继续查找
        elif arr[mid] > target:
            high = mid - 1

        # 如果目标值比中间元素大，则在右半部分继续查找
        else:
            low = mid + 1

    # 目标值不存在于数组中
    return False


# 示例
test = [1, 3, 4, 6, 8, 9, 15, 19, 44, 44]
print(binary_search(test, 15))
print(binary_search(test, 14))
