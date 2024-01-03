#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.7 BucketSort.py
@Author  :Sunshine
@Date    :03/01/2024 22:31 
'''
# 时间复杂度 O(n)
# 缺点: 耗费的空间比较大， 因为不是每个桶都能用得上


def bucketSort(nums, size=5):
    # 1. 确定待排序数组的最大值和最小值，计算桶的个数。
    maxVal = max(nums)  # 最大值
    minVal = min(nums)  # 最小值

    # 2. 初始化桶，创建若干个空桶。
    bucketCount = (maxVal - minVal) // size + 1  # 桶的数量
    buckets = [[] for _ in range(bucketCount)]  # 创建桶

    print("桶的范围：")
    for i in range(bucketCount):
        lower_bound = minVal + i * size
        upper_bound = minVal + (i + 1) * size - 1
        print(f"桶 {i} 的值范围: [{lower_bound} ~ {upper_bound}]")
    print()

    # 3. 遍历待排序数组，将每个元素放入对应的桶中。
    for num in nums:
        idx = (num - minVal) // size  # num应该在哪个桶中， 索引为idx
        n = len(buckets[idx])  # 求出当前桶中的元素个数
        i = 0
        print(f"将 {num} 放入桶 {idx} 中")  # 打印将每个元素放入对应桶的信息

        # 4. 对每个非空桶中的元素进行排序（可选择其他排序算法或递归使用桶排序）。
        # 找出第一个比 num 要大的元素
        while i < n and buckets[idx][i] <= num:
            i += 1
        buckets[idx].insert(i, num)             # 把 num 插入到其应该在的位置, 并确保其有序性
    print('每个桶内的元素:', buckets)

    # 5. 将所有桶中的元素按顺序合并，得到最终的排序结果。
    nums.clear()
    for bucket in buckets:
        nums.extend(bucket)                     # 将每个桶中的元素放到nums中


test = [44, 12, 59, 36, 62, 43, 94, 7, 35, 52, 85]
bucketSort(test)
print('最终结果为: ', test)

print()
test2 = [1, 2, 3, 4, 5, 4, 5, 99]
bucketSort(test2)
print(test2)
