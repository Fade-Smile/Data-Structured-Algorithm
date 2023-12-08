#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project :Python数据结构和算法
@File    :3.1 单向链表.py
@Author  :Sunshine
@Date    :07/12/2023 14:21
"""


# 节点类
class Node(object):
    """ 单向链表 结点 的存储结构"""

    def __init__(self, data, _next=None):
        # item 存放数据元素
        self.data = data
        # next 存放下一个节点的标识/地址
        self.next = _next


class SingleLinkList(object):
    """ 单向链表 """

    def __init__(self):
        self.head = None  # 链表的头节点的地址
        self._length = 0  # 链表的长度, 表表的元素个数

    def is_empty(self):
        """ 判断链表是否为空 """
        return self.head == None

    def length(self):
        """ 返回链表的长度"""
        return self._length

    def nodes_list(self):
        """ 返回链表中的所有节点的值组成的列表 """
        res = []
        cur = self.head
        while cur:  # 当链表不为空, 遍历链表， 获取它的值
            res.append(cur.data)
            cur = cur.next
        return res

    def add(self, data):
        """  往链表的头部添加一个节点, 值为data """
        # 新建一个节点 node
        node = Node(data)
        # 先让node指向当前链表中的头结点
        node.next = self.head
        # 再让链表的head指向当前node节点
        self.head = node
        # 添加节点之后, 链表的长度加1
        self._length += 1

    def append(self, data):
        """ 往链表的尾部添加一个节点, 值为data"""
        # 新建一个节点 node, 值为data
        node = Node(data)
        # 找到链表的尾节点
        # 从头结点开始, 遍历链表中的所有节点
        # 每次判断当前节点的next是否为空
        # 为空说明当前就是尾节点
        # 不为空 通过当前节点的next去访问下一个节点
        if self.head:
            cur = self.head  # 把当前节点的地址赋值给 cur
            while cur.next:
                cur = cur.next
            # 让当前的尾节点的指针域指向node
            cur.next = node
        else:  # 若为空， 则直接吧只想头部的指针域指向node
            self.head = node

        # 链表长度 +1
        self._length += 1

    def insert(self, pos, data):
        """ 往链表的指定位置插入一个节点，值为data """
        # 异常情况
        # 若指定位置pos为第一个元素之前, 则执行尾部插入
        if pos <= 0:
            self.add(data)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(data)
        else:
            # 正常情况
            # 第一步 新建一个节点node
            node = Node(data)
            count = 0
            # 第二步 找到链表中索引为pos-1的节点
            # # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self.head
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 第三步 让node的next指向索引为pos的节点
            node.next = pre.next
            # 第四步 让索引为pos-1的节点的next指向node
            pre.next = node
            # 第五步 链表的长度+1
            self._length += 1

    def remove(self, data):
        """ 删除链表中第一个值为data的节点"""
        pass

    def modify(self, pos, data):
        """ 修改链表中指定位置的节点的值 """
        pass

    def search(self, data):
        """ 查找链表中是否有节点的值为data """
        pass


if __name__ == '__main__':
    l1 = SingleLinkList()  # 新建一个链表类
    print(l1.head, l1.length())
    l1.add(1)
    print(l1.head.data, l1.length())
    l1.add(3)
    print(l1.head.data, l1.length())
    print(l1.nodes_list())
    l1.append(4)
    print(l1.head.data, l1.length())
    print(l1.nodes_list())
