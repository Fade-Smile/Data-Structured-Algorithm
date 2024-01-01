#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.5 QuickSort.py
@Author  :Sunshine
@Date    :31/12/2023 14:08 
'''

print('________________________________________ 方法一 时间复杂度 O（n^2）_________________________________________________')
def quickSort_1(nums):
    n = len(nums)
    if n <= 1:
        return nums
    pivot = nums[0]             # 基准值
    left = []
    right = []

    for i in range(1, n):
        if nums[i] > pivot:
            right.append(nums[i])
        else:
            left.append(nums[i])
    print(left, pivot, right)
    print('_'*30)
    return quickSort_1(left) + [pivot] + quickSort_1(right)


test = [44, 12, 59, 36, 62, 43, 94, 7, 35, 52, 85]
test = quickSort_1(test)
print(test)

print('____________________________________ 方法二 时间复杂度（n log n）___________________________________________________')
# 挖坑法
def partition(nums, left, right):
    pivot = nums[left]                                      # 区域的第一个元素作为基准值
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


def quickSort_2(nums, left, right):
    if left >= right:
        return
    # 分区 --> 分好区之后的基准值的索引返回
    pivot_idx = partition(nums, left, right)
    print(nums, pivot_idx)
    # 左边的区域, left -> pivot_idx -1
    quickSort_2(nums, left, pivot_idx-1)
    # 右边的区域, pivot_idx+1 -> right
    quickSort_2(nums, pivot_idx+1, right)


test = [44, 12, 59, 36, 62, 43, 94, 7, 35, 52, 85]
quickSort_2(test, 0, len(test)-1)
print(test)


print('____________________________________ 优化思路 减少堆栈的消耗(空间) _______________________________________________')
# 挖坑法
"""
1. 基准值的选取
    1.1 随机选取
    1.2 三数 (从数组中的 left, mid, right 三个数排序， 选取它们三者的中间值【mid】)
    
2. 排序序列长度到一定大小后, 改用插入排序 [插入排序的时间和空间都比较少]

3. 重复元素的处理
    每次分割时， 将于本次基准值相等的元素聚集在一起
    3.1 遇到相等的元素, 放到区域的最左边或最右边
    3.2 分好区之后, 相等的元素与基准值一边的元素进行交换

4. 尾递归: 让栈的高度变少， 即把栈的元素给替换掉了， 以此来减少堆栈的消耗
"""
