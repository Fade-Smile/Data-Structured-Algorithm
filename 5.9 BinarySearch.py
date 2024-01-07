#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.9 BinarySearch.py
@Author  :Sunshine
@Date    :07/01/2024 13:39 
'''


def binary_search(nums, target, left, right):
    """
    二分查找 -- 递归
    :param nums: 待查找的数组, 要求是升序的
    :param target: 要找的数字
    :param left: 区间的左边索引
    :param right: 区间的右边索引
    :return:  target在nums 中就返回True，否则返回False

    根据主定理（Master Theorem），该递归式的时间复杂度是 O(log n)，因为在每次递归调用中，问题的规模减半，只需要 O(1) 的时间进行比较和更新索引。
    """
    # 递归的结束条件, left > right
    print(nums[left: right+1])
    if left > right:
        return False

    # 找中间值
    mid = (left + right) // 2
    print('中间值:', nums[mid])
    # 判断中间值是否等于目标值
    if nums[mid] == target:
        return True

    # 如果中间值小于目标值， 说明目标值只可能在中间值的右边区间
    if nums[mid] < target:
        # 左边区间的范围往右边缩
        return binary_search(nums, target, mid + 1, right)
    # 如果中间值大于目标值，说明目标值只可能在中间值的左边区间
    return binary_search(nums, target, left, mid - 1)


if __name__ == '__main__':
    test = [1, 3, 4, 6, 8, 9, 15, 19, 44, 44]
    print(binary_search(test, 15, 0, len(test)-1))
    print()
    print(binary_search(test, 14, 0, len(test) - 1))



