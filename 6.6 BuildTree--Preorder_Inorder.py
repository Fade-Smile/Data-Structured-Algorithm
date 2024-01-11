#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project :Python数据结构和算法 
@File    :6.6 BuildTree--Preorder_Inorder.py
@Author  :Sunshine
@Date    :11/01/2024 01:33 
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(preorder, inorder):
    """
    根据前序遍历和中序遍历去构建一棵 二叉树
    :param preorder: 前序遍历的结果, list
    :param inorder: 中序遍历的结果， list
    :return:  树的根节点
    """
    # 递归结束条件
    if not preorder or not inorder:
        return None

    # 从前序遍历的结果中 找到 root
    root_val = preorder[0]
    root = TreeNode(root_val)

    # 获取中序遍历中 根值的索引
    root_index_inorder = inorder.index(root_val)

    # 计算左子树的范围
    left_preorder = preorder[1:1 + root_index_inorder]
    left_inorder = inorder[:root_index_inorder]

    # 计算右子树的范围
    right_preorder = preorder[1 + root_index_inorder:]
    right_inorder = inorder[root_index_inorder + 1:]

    # 递归构建左子树和右子树
    root.left = build_tree(left_preorder, left_inorder)
    root.right = build_tree(right_preorder, right_inorder)

    return root


def print_tree_shape_top_down(root):
    if not root:
        return

    queue = [root]

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            current = queue.pop(0)
            if current:
                print(current.val, end=' ')
                queue.append(current.left)
                queue.append(current.right)
            else:
                print('None', end=' ')

        print()


# Example usage:
# preorder = [1, 2, 4, 5, 3, 6]
preorder = [0, 1, 3, 7, 8, 4, 9, 2, 5, 6]
# inorder = [4, 2, 5, 1, 3, 6]
inorder = [7, 3, 8, 1, 9, 4, 0, 5, 2, 6]
root = build_tree(preorder, inorder)

print_tree_shape_top_down(root)
