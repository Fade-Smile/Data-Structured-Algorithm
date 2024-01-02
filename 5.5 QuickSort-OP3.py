#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.5 QuickSort-OP3.py
@Author  :Sunshine
@Date    :02/01/2024 13:29 
'''

'''
优化思路 3:
    3. 重复元素的处理
        每次分割时， 将于本次基准值相等的元素聚集在一起
        3.1 遇到相等的元素, 放到区域的最左边或最右边
        3.2 分好区之后, 相等的元素与基准值一边的元素进行交换
        
这个改进后的代码实现了一种优化的快速排序算法。在分割数组时，它将与基准值相等的元素聚集在一起，并且在最后将基准值放到正确的位置。
通过这种处理方式，可以避免重复元素对快速排序算法性能的不利影响，并进一步提高算法的效率。
'''


def partition(nums, left, right):
    pivot = nums[left]  # 区域的第一个元素作为基准值
    less_equal = left  # 小于等于基准值的区域边界
    print('Pivot No: ', pivot)
    for i in range(left + 1, right + 1):
        if nums[i] <= pivot:
            less_equal += 1
            nums[less_equal], nums[i] = nums[i], nums[less_equal]

    nums[left], nums[less_equal] = nums[less_equal], nums[left]  # 将基准值放到正确的位置
    return less_equal  # 返回基准值的正确位置


def quickSort_6(nums, left, right):
    if left >= right:
        return

    pivot_idx = partition(nums, left, right)
    print(nums, pivot_idx)
    # 对左右两个分区进行递归排序
    quickSort_6(nums, left, pivot_idx - 1)
    quickSort_6(nums, pivot_idx + 1, right)


test = [44, 12, 42, 36, 62, 42, 94, 7, 35, 44, 52, 85, 7, 62, 94]
quickSort_6(test, 0, len(test) - 1)
print(test)
