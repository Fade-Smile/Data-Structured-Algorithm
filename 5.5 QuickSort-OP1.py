#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.5 QuickSort-OP1.py
@Author  :Sunshine
@Date    :02/01/2024 11:26 
'''
import random
''' 
    快速排序的最坏情况发生在每次选择的基准值都是当前子数组的最大或最小值，这样就会导致每次划分的两个子序列一个为空，
    另一个包含原序列中的 n-1 个元素。这样的情况下，快速排序的时间复杂度退化为 O(n^2)。
    
    优化思路 1: 
        1. 基准值的选取
            1.1 随机选取
            1.2 三数 (从数组中的 left, mid, right 三个数排序， 选取它们三者的中间值【mid】)
'''
print('----------------------解决方法: 1 随机选取------------------------------')


def partition(nums, left, right):
    # 随机选择基准值的索引并交换到区间最左边
    pivot_index = random.randint(left, right)
    nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
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


def quickSort_3(nums, left, right):
    if left >= right:
        return
    pivot_idx = partition(nums, left, right)
    print(nums, pivot_idx)
    quickSort_3(nums, left, pivot_idx - 1)
    quickSort_3(nums, pivot_idx + 1, right)


# 调用方式
test = [44, 12, 59, 36, 62, 43, 94, 7, 35, 52, 85]
quickSort_3(test, 0, len(test) - 1)
print(test)

print('-------------- 1.2 三数 (从数组中的 left, mid, right 三个数排序， 选取它们三者的中间值【mid】) --------------------------')


def median_of_three(nums, left, right):
    mid = (left + right) // 2

    # 确保 nums[left] <= nums[mid] <= nums[right]
    if nums[left] > nums[mid]:
        nums[left], nums[mid] = nums[mid], nums[left]
    if nums[mid] > nums[right]:
        nums[mid], nums[right] = nums[right], nums[mid]
    if nums[left] > nums[mid]:
        nums[left], nums[mid] = nums[mid], nums[left]

    return mid


def partition(nums, left, right):
    # 随机选择基准值的索引并交换到区间最左边
    pivot_index = random.randint(left, right)
    nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
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


def quickSort_4(nums, left, right):
    if left >= right:
        return
    pivot_idx = partition(nums, left, right)
    print(nums, pivot_idx)
    quickSort_3(nums, left, pivot_idx - 1)
    quickSort_3(nums, pivot_idx + 1, right)


# 调用方式
test = [44, 12, 59, 36, 62, 43, 94, 7, 35, 52, 85]
quickSort_4(test, 0, len(test) - 1)
print(test)
