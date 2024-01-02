#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.5 QuickSort-OP4.py
@Author  :Sunshine
@Date    :02/01/2024 13:48 
'''

'''
4. 尾递归: 让栈的高度变少， 即把栈的元素给替换掉了， 以此来减少堆栈的消耗
'''


def partition(nums, left, right):
    pivot = nums[left]                                      # 区域的第一个元素作为基准值
    print('Pivot No: ', pivot)

    while left < right:
        # 挖坑 填坑
        while left < right and nums[right] > pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot                                      # 基准值的正确位置
    return left


def quickSort_tail(nums, left, right):
    while left < right:
        pivot_idx = partition(nums, left, right)
        print(nums, pivot_idx)

        # 对较小区间进行递归排序
        if pivot_idx - left < right - pivot_idx:
            quickSort_tail(nums, left, pivot_idx - 1)
            left = pivot_idx + 1
        else:
            quickSort_tail(nums, pivot_idx + 1, right)
            right = pivot_idx - 1


# 尾递归优化后的调用方式
test = [44, 12, 59, 36, 62, 43, 94, 7, 35, 52, 85]
quickSort_tail(test, 0, len(test) - 1)
print(test)
