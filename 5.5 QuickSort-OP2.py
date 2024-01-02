#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.5 QuickSort-OP2.py
@Author  :Sunshine
@Date    :02/01/2024 13:22 
'''

'''
优化思路 2:
    排序序列长度到一定大小后, 改用插入排序 [插入排序的时间和空间都比较少]
'''

def insertion_sort(nums, left, right):
    for i in range(left + 1, right + 1):
        key = nums[i]
        j = i - 1
        while j >= left and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key


def partition(nums, left, right):
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] > pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot
    return left


def quickSort_5(nums, left, right):
    if left >= right:
        return

    # 使用插入排序进行优化
    if right - left + 1 <= 10:
        insertion_sort(nums, left, right)
        return

    pivot_idx = partition(nums, left, right)
    quickSort_5(nums, left, pivot_idx - 1)
    quickSort_5(nums, pivot_idx + 1, right)


test = [44, 12, 59, 36, 62, 43, 94, 7, 35, 52, 85]
quickSort_5(test, 0, len(test) - 1)
print(test)
