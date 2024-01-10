#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project :Python数据结构和算法 
@File    :6.3 Tree-孩子表示法.py
@Author  :Sunshine
@Date    :10/01/2024 23:01 
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []  # 存储子节点的列表


class ChildTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def add_child(self, parent_data, child_data):
        parent_node = self.find_node(parent_data)
        if parent_node:
            child_node = TreeNode(child_data)
            parent_node.children.append(child_node)

    def find_node(self, data, node=None):
        if node is None:
            node = self.root

        if node.data == data:
            return node

        for child in node.children:
            result = self.find_node(data, child)
            if result:
                return result

        return None

    def print_tree(self, node=None, depth=0):
        if node is None:
            node = self.root

        print("  " * depth + f"Node Data: {node.data}")

        if node.children:
            print("  " * (depth + 1) + "Children:")
            for child in node.children:
                print("  " * (depth + 2) + f"{child.data}")

            print("  " * (depth + 1) + "Sibling Relationships:")
            for i in range(len(node.children) - 1):
                print("  " * (depth + 2) + f"{node.children[i].data} is a sibling of {node.children[i + 1].data}")

        for child in node.children:
            self.print_tree(child, depth + 1)


# 示例用法：
tree = ChildTree("A")

tree.add_child("A", "B")
tree.add_child("A", "C")
tree.add_child("B", "D")
tree.add_child("B", "E")

tree.print_tree()
