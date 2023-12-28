#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.3 InsertSort.py
@Author  :Sunshine
@Date    :28/12/2023 12:36 
'''


def InserSort(nums):
    n = len(nums)                                   # 数组的长度
    for i in range(n-1):                            # 外层循环遍历数组中的每个元素（从第二个元素开始到最后一个元素）
        curNum = nums[i+1]                          # 取出当前未排序区的第一个元素作为待插入元素
        idx = i                                     # 初始化有序区的最后一个元素的索引
        while nums[idx] > curNum and idx >= 0:      # 内层循环在有序区从后往前比较，找到合适的插入位置
            nums[idx+1] = nums[idx]                 # 如果有序区的元素大于待插入元素，则将有序区元素向后移动一位
            idx -= 1                                # 继续向前寻找插入位置
        nums[idx+1] = curNum                        # 将待插入元素放到合适的位置上
        print(f'第{i+1}趟排序', nums)


test = [9, 3, 1, 2, 7, 5]
InserSort(test)
print(test)
