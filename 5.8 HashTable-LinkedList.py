#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :5.8 HashTable-LinkedList.py
@Author  :Sunshine
@Date    :06/01/2024 14:24 
'''

class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.size = 0
        self.threshold = int(self.capacity * 2 / 3)
        self.table = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity if self.capacity > 0 else 0 if self.capacity == 0 else -1

    def _resize(self):
        self.capacity *= 2
        self.threshold = int(self.capacity * 2 / 3)
        old_table = self.table
        self.table = [None] * self.capacity

        for head in old_table:
            current = head
            while current:
                key = current.key
                value = current.value
                index = self._hash(key)

                if self.table[index] is None:
                    self.table[index] = LinkedListNode(key, value)
                else:
                    last_node = None
                    node = self.table[index]
                    while node:
                        last_node = node
                        node = node.next
                    last_node.next = LinkedListNode(key, value)

                current = current.next

    def put(self, key, value):
        # 计算哈希值，确定存储位置
        index = self._hash(key)

        # 若当前索引处的槽为空，则创建新节点并插入到该槽中
        if self.table[index] is None:
            self.table[index] = LinkedListNode(key, value)
            self.size += 1
        else:
            current = self.table[index]

            # 若槽中已经有链表存在，则遍历该链表
            while current:
                # 如果找到具有相同键和值的节点，说明键值对已存在，立即返回
                if current.key == key and current.value == value:
                    return

                # 如果找到具有相同值（可能不同键）的节点，继续遍历
                if current.value == value:
                    new_node = LinkedListNode(key, value)
                    new_node.next = current.next
                    self.table[index] = new_node
                    return

                current = current.next

            # 如果到达链表末尾仍未找到相同键值对，则创建新节点
            new_node = LinkedListNode(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

        # 如果哈希表大小超过阈值，触发调整大小操作
        if self.size >= self.threshold:
            self._resize()

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

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

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
    print('当前容量为：', hash_table.capacity)

    print()
    hash_table.put("apple", 10)
    hash_table.put("banana", 20)
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
    hash_table.display()

    print()
    hash_table.remove("orange")
    print('当前容量为：', hash_table.capacity)
    print("After removing 'orange':")
    hash_table.display()
