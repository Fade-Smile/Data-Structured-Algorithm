#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.7 BusketSort--LinkedList.py
@Author  :Sunshine
@Date    :03/01/2024 23:40 
'''


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def bucketSort(nums, size=5):
    maxVal = max(nums)
    minVal = min(nums)
    bucketCount = (maxVal - minVal) // size + 1
    buckets = [Node() for _ in range(bucketCount)]  # 每个桶的头节点，初始化为一个空节点

    print("桶的范围：")
    for i in range(bucketCount):
        lower_bound = minVal + i * size
        upper_bound = minVal + (i + 1) * size - 1
        print(f"桶 {i} 的值范围: [{lower_bound} ~ {upper_bound}]")
    print()

    # 遍历待排序数组，将每个元素放入对应的桶中
    for num in nums:
        idx = (num - minVal) // size  # num应该在哪个桶中， 索引为idx
        print(f"将 {num} 放入桶 {idx} 中")  # 打印将每个元素放入对应桶的信息

        # 在当前桶的链表中找到合适的位置，将新元素 num 插入到链表中，保持链表的有序性。
        current = buckets[idx]                                      # 将 current 设为当前桶的头节点，开始对该桶进行处理。
        # current.next 检查当前节点是否有下一个节点，同时 current.next.value <= num 检查下一个节点的值是否小于等于待插入的值 num。
        while current.next and current.next.value <= num:
            current = current.next

        new_node = Node(num)
        new_node.next = current.next
        current.next = new_node

    print('每个桶内的元素:')
    for i, bucket in enumerate(buckets):
        print(f"桶 {i}:", end=" ")
        current = bucket.next
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

    # 合并桶中的元素得到排序结果
    nums.clear()
    for bucket in buckets:
        current = bucket.next
        while current:
            nums.append(current.value)
            current = current.next


# 调用示例
nums = [29, 25, 3, 49, 9, 37, 21, 43]
bucketSort(nums)
print(nums)
