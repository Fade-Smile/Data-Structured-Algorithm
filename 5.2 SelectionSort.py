#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.2 SelectionSort.py
@Author  :Sunshine
@Date    :28/12/2023 12:05 
'''


def selectionSort(nums):
    n = len(nums)  # 数组的长度
    print(nums)
    for i in range(n-1):
        # 找无序取最小的元素
        min_idx = i     # 无序区中最小元素的索引
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        # 执行完上面的循环后
        # min_idx 就是无序区中的最小元素的索引
        # 把最小元素和有序区的后一个元素交换位置
        nums[i],  nums[min_idx] = nums[min_idx], nums[i]
        print(f'第{i+1}排序:', nums)


test = [9, 3, 1, 2, 4, 7]
selectionSort(test)
print(test)
