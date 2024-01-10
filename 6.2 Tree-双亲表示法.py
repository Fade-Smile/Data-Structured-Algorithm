#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project :Python数据结构和算法 
@File    :6.2 Tree-双亲表示法.py
@Author  :Sunshine
@Date    :10/01/2024 22:57 
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None  # 指向父节点的指针


class ParentTree:
    def __init__(self):
        self.nodes = []  # 存储所有节点的列表

    def add_node(self, data, parent_data=None):
        new_node = TreeNode(data)
        self.nodes.append(new_node)

        if parent_data is not None:
            parent_node = self.find_node(parent_data)
            if parent_node:
                new_node.parent = parent_node

    def find_node(self, data):
        for node in self.nodes:
            if node.data == data:
                return node
        return None


# 示例用法：
tree = ParentTree()

tree.add_node("A")
tree.add_node("B", "A")
tree.add_node("C", "A")
tree.add_node("D", "B")
tree.add_node("E", "B")

# 访问节点的数据和父节点
for node in tree.nodes:
    parent_data = node.parent.data if node.parent else None
    print(f"Node Data: {node.data}, Parent Data: {parent_data}")
