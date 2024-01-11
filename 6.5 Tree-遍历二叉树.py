#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project :Python数据结构和算法 
@File    :6.5 Tree-遍历二叉树.py
@Author  :Sunshine
@Date    :11/01/2024 00:40 
"""

class Node:
    def __init__(self, val):
        self.val = val          # 数据域
        self.left = None        # 左指针域
        self.right = None       # 右指针域


class Tree:
    def __init__(self):
        self.root = None        # 树的根节点

    def add(self, val):
        # 将具有给定值的节点添加到树中，同时保持树的完整性。它使用广度优先遍历（级别顺序遍历）来查找添加节点的适当位置。
        # val: 要添加的节点的值
        # 往树种添加一个节点， 并保证添加之后这棵树依旧是一棵完整的 二叉树

        node = Node(val)

        # 判断树是否为空， 如果为空， 直接将 node 设置为根节点
        if not self.root:
            self.root = node
            return

        # 从上往下， 从左往右的去遍历整棵树， 然后找到第一个空位
        # 把节点添加进去
        queue = [self.root]     # 存每一层的节点
        while True:
            # 第一次循环 queue = [root]
            # 第二次循环 queue = [root.left, root.right]
            # 第三次循环 queue = [root.right, root.left.left, root.left.right]
            # 第四次循环 queue = [root.left.left, root.left.right, root.right.left, root.right.right]
            cur_node = queue.pop(0)
            # 先找左边， 看有没有空位
            if not cur_node.left:
                cur_node.left = node
                return
            elif not cur_node.right:
                cur_node.right = node
                return
            # 如果都没有空位， 那就把左边节点与右边节点 都加到之后要判断的节点中
            queue.extend((cur_node.left, cur_node.right))

    def show(self):
        # 展示树
        if not self.root:
            return

        queue = [self.root]  # 存每一层的节点
        i = 1
        while queue:
            size = len(queue)               # 获取当前层的元素个数
            print(f'第{i}层', end='\t')
            for _ in range(size):
                node = queue.pop(0)         # 抛出队列中的第一个元素
                print(node.val, end=' ')    # 对当前元素进行操作
                # 节点的左孩子与右孩子添加到队列里
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()
            i += 1

    def pre_order(self):
        # 先序遍历 前序遍历  根节点 左子树 右子树
        print('先序遍历: ')
        def helper(root):
            if not root:
                return
            print(root.val, end='->')         # 输出根节点
            helper(root.left)       # 先序遍历左子树
            helper(root.right)      # 先序遍历右子树
        helper(self.root)
        print()

    def in_order(self):
        # 中序遍历  左子树 根节点 右子树
        print('中序遍历: ')
        def helper(root):
            if not root:
                return
            helper(root.left)                               # 中序遍历左子树
            print(root.val, end='->')         # 输出根节点
            helper(root.right)                              # 中序遍历右子树
        helper(self.root)
        print()

    def post_order(self):
        # 中序遍历  左子树 根节点 右子树
        print('后序遍历: ')
        def helper(root):
            if not root:
                return
            helper(root.left)                               # 后序遍历左子树
            helper(root.right)                              # 后遍历右子树
            print(root.val, end='->')         # 输出根节点

        helper(self.root)
        print()


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.pre_order()
    tree.in_order()
    tree.post_order()
