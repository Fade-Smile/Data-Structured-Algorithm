#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :4.11 数据结构 -- 堆.py
@Author  :Sunshine
@Date    :23/12/2023 14:33 
'''


class MinHeap:
    def __init__(self):
        self.heap = []

    # 获取父节点索引
    def parent(self, i):
        return (i - 1) // 2

    # 获取左子节点索引
    def left_child(self, i):
        return 2 * i + 1

    # 获取右子节点索引
    def right_child(self, i):
        return 2 * i + 2

    # 交换两个节点的值
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # 向上调整，维护堆性质
    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    # 向下调整，维护堆性质
    def heapify_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        # 比较当前节点和左右子节点，找出最小值的索引
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        # 若当前节点不是最小值，则进行交换，并继续向下调整
        if i != min_index:
            self.swap(i, min_index)
            self.heapify_down(min_index)

    # 插入元素到堆中
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    # 从堆中移除最小值
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root


if __name__ == '__main__':

    # 创建最小堆实例
    min_heap = MinHeap()

    # 插入元素到堆中
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(8)
    min_heap.insert(1)

    # 输出最小堆中的最小值并移除
    print(min_heap.extract_min())  # 输出：1
