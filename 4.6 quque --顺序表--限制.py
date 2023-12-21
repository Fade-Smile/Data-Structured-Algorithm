#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :4.6 quque --顺序表--限制.py
@Author  :Sunshine
@Date    :21/12/2023 12:35 
'''


class LimitedQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.size = 0
        self.front = 0
        self.rear = -1

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            print("队列已满，无法添加新元素")
            return

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("队列为空")
            return None

        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("队列为空")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("队列为空")
            return

        current = self.front
        while current != (self.rear + 1) % self.capacity:
            print(self.queue[current], end=" ")
            current = (current + 1) % self.capacity
        print()


# 示例用法
if __name__ == '__main__':
    queue = LimitedQueue(5)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)  # 超出容量，会提示队列已满

    print(queue.display())  # 输出队列内容
    print(queue.dequeue())
    print(queue.dequeue())

    print(queue.display())  # 输出更新后的队列内容
