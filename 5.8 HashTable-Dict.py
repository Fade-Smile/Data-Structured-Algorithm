#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.8 HashTable-Dict.py
@Author  :Sunshine
@Date    :06/01/2024 13:38 
'''

class HashTable:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.size = 0
        self.threshold = int(self.capacity * 2 / 3) # 2/3 填充率触发扩容
        self.table = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def _rehash(self, key):
        # 重新计算哈希， 用于扩容是重新放置元素
        return hash(key) % (self.capacity * 2)

    def _resize(self):
        # 扩容
        self.capacity *= 2
        self.threshold = int(self.capacity * 2/3)
        old_table = self.table
        self.table = [None] * self.capacity

        for item in old_table:
            if item is not None:
                self._rehash_and_insert(item[0], item[1])

    def _rehash_and_insert(self, key, value):
        # 用于扩容时重新放置元素
        index = self._rehash(key)
        new_capacity = len(self.table)    # 获取扩容后的新容量
        while self.table[index % new_capacity] is not None:
            index = index + 1
        self.table[index % new_capacity] = (key, value)

    def put(self, key, value):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key: # 如果键已存在， 则更新值
                self.table[index] = (key, value)
                return

            index = (index + 1) % self.capacity     # 开放定址法处理冲突
        self.table[index] = (key, value)
        self.size += 1

        if self.size >= self.threshold:         # 检测填充因子是否达到阈值
            self._resize()

    def get(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity
        return None

    def remove(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.size -= 1
                return
            index = (index + 1) % self.capacity

    def display(self):
        for i in range(self.capacity):
            if self.table[i] is not None:
                print(f'Index {i}: self.table{i}')
            else:
                print(f'Index {i}: None')


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
