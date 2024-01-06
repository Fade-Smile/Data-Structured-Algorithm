#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.8 HashTable-LinkedList.py
@Author  :Sunshine
@Date    :06/01/2024 14:24 
'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.size = 0
        self.threshold = int(self.capacity * 2 / 3)  # 2/3 填充率触发扩容
        self.table = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        # 扩容
        self.capacity *= 2
        self.threshold = int(self.capacity * 2 / 3)
        old_table = self.table
        self.table = [None] * self.capacity

        for head in old_table:
            current = head
            while current:
                self.put(current.key, current.value)
                current = current.next

    def put(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    if current.value != value:
                        current.value = value  # 如果键已存在但值不同，则更新值
                    return
                if current.next is None:
                    current.next = Node(key, value)
                    self.size += 1
                    return
                current = current.next

        if self.size >= self.threshold:
            self._resize()

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        index = self._hash(key)
        head = self.table[index]
        prev = None
        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next
                else:
                    self.table[index] = head.next
                self.size -= 1
                return
            prev = head
            head = head.next

    def display(self):
        for i in range(self.capacity):
            current = self.table[i]
            print(f'Index {i}:', end=' ')
            while current:
                print(f'({current.key}, {current.value})', end=' -> ')
                current = current.next
            print("None")


if __name__ == '__main__':
    # 示例用法
    hash_table = HashTable()

    hash_table.display()
    print()
    hash_table.put("apple", 10)
    hash_table.put("banana", 20)
    print('当前容量为：', hash_table.capacity)
    print()
    hash_table.put("orange", 30)
    print('当前容量为：', hash_table.capacity)
    print()
    hash_table.put("watermelon", 30)
    hash_table.put("lemon", 30)

    print("Get 'apple':", hash_table.get("apple"))
    print("Get 'banana':", hash_table.get("banana"))
    print("Get 'orange':", hash_table.get("orange"))
    print("Get 'watermelon':", hash_table.get("watermelon"))
    print("Get 'lemon':", hash_table.get("lemon"))

    print()
    hash_table.remove("orange")
    print("After removing 'orange':")
    hash_table.display()

