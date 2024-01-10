#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project :Python数据结构和算法 
@File    :6.4 Tree-孩子兄弟表示法.py
@Author  :Sunshine
@Date    :10/01/2024 23:09 
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.first_child = None  # 指向第一个孩子节点的指针
        self.next_sibling = None  # 指向下一个兄弟节点的指针


class ChildSiblingTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def add_child(self, parent_data, child_data):
        parent_node = self.find_node(parent_data)
        if parent_node:
            if not parent_node.first_child:
                parent_node.first_child = TreeNode(child_data)
            else:
                sibling = parent_node.first_child
                while sibling.next_sibling:
                    sibling = sibling.next_sibling
                sibling.next_sibling = TreeNode(child_data)

    def find_node(self, data, node=None):
        if node is None:
            node = self.root

        if node.data == data:
            return node

        if node.first_child:
            result = self.find_node(data, node.first_child)
            if result:
                return result

        if node.next_sibling:
            result = self.find_node(data, node.next_sibling)
            if result:
                return result

        return None

    def print_tree(self, node=None, depth=0):
        if node is None:
            node = self.root

        print("  " * depth + f"Node Data: {node.data}")

        if node.first_child:
            print("  " * (depth + 1) + "Children:")
            self.print_tree(node.first_child, depth + 1)

        if node.next_sibling:
            print("  " * (depth + 1) + "Sibling:")
            self.print_tree(node.next_sibling, depth + 1)


# 示例用法：
tree = ChildSiblingTree("A")

tree.add_child("A", "B")
tree.add_child("A", "C")
tree.add_child("B", "D")
tree.add_child("B", "E")

tree.print_tree()
