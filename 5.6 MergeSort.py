#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.6 MergeSort.py
@Author  :Sunshine
@Date    :02/01/2024 14:09 
'''
'''
这段代码是归并排序算法的实现，时间复杂度可以通过分析归并排序的两个主要步骤来确定：分和合。

分步骤（Splitting）：

在每一层递归中，数组都被划分为两个大致相等的子数组。
这个过程会持续进行直到无法再分割为止（即子数组长度为1）。
这样的划分需要进行 O(log n) 次，其中 n 是输入数组的长度。因为每次都将数组分成两半，所以时间复杂度为 O(log n)。
合并步骤（Merging）：

在每个合并步骤中，需要遍历合并两个子数组，时间复杂度为 O(n)，其中 n 是被合并的元素总数。
在最坏情况下，需要合并 O(n) 个元素。
由于合并步骤发生在每一层的每个子问题上，所以总体时间复杂度为 O(n * log n)。
综上所述，归并排序的时间复杂度为 O(n * log n)，其中 n 是输入数组的长度。值得注意的是，归并排序在所有情况下的时间复杂度都是 O(n * log n)，这使得它在处理大规模数据时非常高效。
'''
# 稳定性


# 归并函数
def merge(left, right):
    # 最终返回一个合并好的有序的数组
    # 定义两个变量， 分别代表当前 left 和 right 的未添加进有序数组的第一个元素
    left_idx, right_idx = 0, 0
    res = []
    while left_idx < len(left) and right_idx < len(right):
        # 左边数组的元素小于右边数组
        if left[left_idx] <= right[right_idx]:
            # 把左边元素添加到有序数组中
            res.append(left[left_idx])
            # 索引往后移
            left_idx += 1
        else:
            # 把右边元素添加到有序区中
            res.append(right[right_idx])
            # 索引往后移
            right_idx += 1

    res += right[right_idx:]                    # 把剩余的未添加的元素全部添加到有序数组后面
    res += left[left_idx:]                      # 为什么可以直接添加? 因为 left, right 本身就是一个有序数组
    # 如果说left_idx走完了,right还剩一些元素,说明right剩下的元素全部都比有序数组的最后一个元素要大
    print('合: ', res)
    return res


def mergeSort(nums):
    # 分
    # 结束条件: 数组不能再分了
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2                    # 获取数组的中间位置
    print('分: ', nums[:mid], nums[mid:])
    left = mergeSort(nums[:mid])            # 左边的数组
    right = mergeSort(nums[mid:])           # 右边的数组

    # 合
    return merge(left, right)


test = [44, 12, 59, 36, 62, 43, 94, 7, 35, 52, 85]
test = mergeSort(test)
print('总: ', test)
