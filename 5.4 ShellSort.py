#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.4 ShellSort.py
@Author  :Sunshine
@Date    :28/12/2023 13:55 
'''
import time


def shellSort_1(nums):
    n = len(nums)                                       # 数组长度
    gap = n//2                                          # 设置一个增量
    while gap >= 1:                                     # 这个循环控制着增量的逐步减小，直到最终为 1 时排序完成。
        for i in range(gap):                            # 这个循环用于分组，将数组分成若干个子序列，以便进行局部排序。
            for j in range(i, n-gap, gap):              # 这个内部循环在每个子序列内进行插入排序。它遍历每个子序列中的元素，将当前元素插入到正确的位置以形成局部有序。
                curNum = nums[j+gap]                    # 获取当前子序列中无序区的第一个元素的值。
                idx = j                                 # 初始化有序区的最后一个元素的索引
                while idx >= 0 and nums[idx] > curNum:  # 这个循环用于将当前元素插入到有序区的合适位置。它向前遍历有序区，并将比当前元素大的元素向后移动，为当前元素腾出位置。
                    nums[idx+gap] = nums[idx]           # 把小组的有序区的元素往后挪
                    idx -= gap                          # 指针往前移， 从此来从后往前遍历小组的有序区
                nums[idx+gap] = curNum                  # 将当前元素插入到有序区的正确位置。
            print(f'当前增量是{gap}, ', nums)
        gap //= 2                                       # 逐渐减小增量，以进行下一轮的分组和排序


# improve version    时间复杂度
def shellSort_2(nums):
    n = len(nums)                                       # 数组长度
    gap = n//2                                          # 设置一个增量
    while gap >= 1:                                     # 这个循环控制着增量的逐步减小，直到最终为 1 时排序完成。
        # 分组
        for i in range(gap, n):
            # i = 5, curNums=43, idx = 0
            # [43, ..., 44, ..., 85]
            # i = 6,  curNum=94, idx=1
            # [..., 12, ..., 94]
            # i = 7, curNums=7, idx=2
            # [..., 7, ... 59, ...]
            curNum = nums[i]                            # 当前要插入的无序区的元素的值
            idx = i - gap                               # 当前元素所在小组的有序区的最后一个元素的索引
            while idx >= 0 and curNum < nums[idx]:
                nums[idx+gap] = nums[idx]
                idx -= gap
            nums[idx+gap] = curNum
            print(f'当前增量是{gap}, ', nums)
        gap //= 2                                       # 逐渐减小增量，以进行下一轮的分组和排序


def shellSort_3(nums):
    n = len(nums)                                       # 数组长度
    # O(nlogn)
    gap = 1                                             # 设置一个增量
    while gap < n//3:
        gap = gap * 3 + 1
    while gap >= 1:                                     # 这个循环控制着增量的逐步减小，直到最终为 1 时排序完成。
        for i in range(gap):                            # 这个循环用于分组，将数组分成若干个子序列，以便进行局部排序。
            for j in range(i, n-gap, gap):              # 这个内部循环在每个子序列内进行插入排序。它遍历每个子序列中的元素，将当前元素插入到正确的位置以形成局部有序。
                curNum = nums[j+gap]                    # 获取当前子序列中无序区的第一个元素的值。
                idx = j                                 # 初始化有序区的最后一个元素的索引
                while idx >= 0 and nums[idx] > curNum:  # 这个循环用于将当前元素插入到有序区的合适位置。它向前遍历有序区，并将比当前元素大的元素向后移动，为当前元素腾出位置。
                    nums[idx+gap] = nums[idx]           # 把小组的有序区的元素往后挪
                    idx -= gap                          # 指针往前移， 从此来从后往前遍历小组的有序区
                nums[idx+gap] = curNum                  # 将当前元素插入到有序区的正确位置。
            print(f'当前增量是{gap}, ', nums)
        gap //= 3                                       # 逐渐减小增量，以进行下一轮的分组和排序


# gap=5 [44，43，85]，[12，94], [59，7]，[36，35], [62,52]
#           43, 12, 7, 35, 52, 44, 94, 59, 36, 62, 85
# gap = 2 [43, 7, 52, 94, 36, 85], [12, 35, 44, 59, 62]
# 7, 36, 43, 52, 85, 94
test1 = [44, 12, 59, 36, 62, 43, 94, 7, 35, 52, 85]
shellSort_1(test1)
print(test1)

time.sleep(3)
print()

test2 = [44, 12, 59, 36, 62, 43, 94, 7, 35, 52, 85]
shellSort_2(test2)
print(test2)

time.sleep(3)
print()

test3 = [44, 12, 59, 36, 62, 43, 94, 7, 35, 52, 85]
shellSort_3(test3)
print(test3)
