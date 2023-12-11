#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :3.2 单项循环链表.py
@Author  :Sunshine
@Date    :11/12/2023 13:25 
'''


# 节点类
class Node(object):
    """ 单向链表 结点 的存储结构"""

    def __init__(self, data, _next=None):
        # item 存放数据元素  数据域
        self.data = data
        # next 存放下一个节点的标识/地址  指针域
        self.next = _next


class SingleCycleLinkList(object):
    """ 单向循环链表 """

    def __init__(self):
        self.head = None  # 链表的头节点的地址
        self._length = 0  # 链表的长度, 链表的元素个数

    def is_empty(self):
        """ 判断链表是否为空 """
        return self._length == 0

    def length(self):
        """ 返回链表的长度"""
        return self._length

    def nodes_list(self):
        """ 返回链表中的所有节点的值组成的列表 """
        res = []
        if self.is_empty():
            return res
        res.append(self.head.data)
        cur = self.head.next
        while cur != self.head:                 # 循环链表直到头节点
            res.append(cur.data)
            cur = cur.next
        return res

    def add(self, data):
        """  往循环链表的头部添加一个节点, 值为data """
        node = Node(data)                       # 新建一个节点 node
        if self.is_empty():                     # 若链表为空
            self.head = node
            node.next = self.head               # 或者 node 指向自身 形成循环
        else:
            node.next = self.head               # 让新的node指向当前链表中的头结点
            cur = self.head
            while cur.next != self.head:        # 遍历 循环链表 找到尾节点
                cur = cur.next
            cur.next = node                     # 让链表的尾节点的next指向Node
            self.head = node                    # 更新头节点为新节点

        self._length += 1                       # 添加节点之后, 链表的长度加1

    def append(self, data):
        """ 往链表的尾部添加一个节点, 值为data"""
        node = Node(data)                       # 新建一个节点 node, 值为data

        if self.head:                           # 判断 头节点是否为空
            cur = self.head                     # 把当前节点的地址赋值给 cur
            while cur.next != self.head:        # 遍历链表中的所有节点  寻找尾节点
                cur = cur.next
            cur.next = node                     # 让原本的尾节点的指针域指向新建的node

        else:                                   # 若为空， 则直接把头部的指针域指向node
            self.head = node
        node.next = self.head                   # 新的尾节点指向当前的头结点
        self._length += 1                       # 链表长度 +1

    def insert(self, pos, data):
        """ 往链表的指定位置插入一个节点，值为data """
        # 异常情况
        # 若指定位置pos为第一个元素之前, 则执行尾部插入
        if pos <= 0:
            self.add(data)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(data)
        else:
            # 正常情况
            # 第一步 新建一个节点node
            node = Node(data)
            # 第二步 找到链表中索引为pos-1的节点
            pre = self.head  # pre 变量用于存储索引为 pos-1 的节点
            while pos - 1:  # 这个循环用于找到索引为 pos-1 的节点
                # [在 while 循环中，当表达式的结果为非零值或者是 True 时，循环会继续执行。当表达式的结果为零值或者是 False 时，循环会停止执行，程序继续往下执行。]
                pre = pre.next  # 将 pre 指向下一个节点，直到找到索引为 pos-1 的节点
                pos -= 1  # 不断减少 pos 的值，直到找到索引为 pos-1 的节点

            # 第三步 让node的next指向索引为pos的节点
            node.next = pre.next
            # 第四步 让索引为pos-1的节点的next指向node
            pre.next = node
            # 第五步 链表的长度+1
            self._length += 1

    def remove(self, data):
        """ 这段代码实现了在单向链表中删除第一个匹配给定值的节点的功能，如果存在匹配的节点则删除，否则不做任何操作。"""
        if self.is_empty():                             # 判断单项循环链表是否为空， 若为空， 那必然没有值为data的节点
            return -1
        cur = self.head
        flag = True                                     # 该标志的作用是: 让第一次循环能进入
        pre_node = None                                 # 要删除的节点的前驱结点
        while cur != self.head or flag:                 # 遍历整个链表，直到找到需要删除的节点或者到达链表末尾 (当cur为None时，表示已经遍历完整个链表)
            flag = False                                # 让循环继续的条件就必须是 cur!=self.head
            if cur.data == data:                        # 检查当前节点cur的数据是否等于目标值data。
                                                        # 如果前驱结点为空，说明我们要删除的节点是第一个节点
                if not pre_node:                        # 判断是否为链表的第一个节点（即没有前驱节点）。如果 pre_node 为空（None），说明要删除的节点是链表的头节点。
                    last_node = self.head               # 找到尾节点， 让尾节点的next指向新的 head
                    while last_node.next != self.head:
                        last_node = last_node.next
                    last_node.next = self.head.next
                    self.head = cur.next                # 这种情况下，将链表的头节点指向当前节点的下一个节点 cur.next，从而删除了头节点。
                else:                                   # 如果不是头节点，即 pre_node 不为空，
                    pre_node.next = cur.next            # 将前驱节点 pre_node 的 next 指针指向当前节点的下一个节点 cur.next，以跳过当前节点，从而删除了当前节点。
                self._length -= 1
                return 0
            pre_node = cur
            cur = cur.next
        return -1                                       # 如果遍历完整个链表都没有找到值为 data 的节点，那么函数返回 -1，表示未找到对应节点，没有执行删除操作

    def modify(self, pos, data):
        """ 修改链表中指定位置的节点的值 """
        if 0 <= pos < self._length:
            cur = self.head
            while pos:
                cur = cur.head
                pos -= 1
            cur.data = data
        else:
            print('你输入的不符合范围')

    def search(self, data):
        """ 查找链表中是否有节点的值为data """
        if self.is_empty():
            return False
        cur = self.head
        flag = True
        while cur != self.head or flag:
            flag = False
            if cur.data == data:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    l1 = SingleCycleLinkList()                      # 新建一个循环链表类
    print(l1.nodes_list(), l1.length())

    print('**************Test add()**************')
    l1.add(10)
    print(l1.nodes_list())
    l1.add(32)
    print(l1.head.data, l1.length())
    print(l1.head.data, '->', l1.head.next.data, '->', l1.head.next.next.data)
    print(l1.nodes_list())

    print('**************Test append()**************')
    l1.append(41)
    print(l1.head.data, l1.length())
    print(l1.nodes_list())

    print('**************Test insert()**************')
    l1.insert(2, 72)
    print(l1.nodes_list())

    print('**************Test remove()**************')
    l1.add(12)
    l1.add(14)
    l1.add(32)
    print(l1.nodes_list(), l1.length())
    l1.remove(32)
    print(l1.nodes_list(), l1.length())
    l1.remove(10)
    print(l1.nodes_list(), l1.length())

    print('**************Test modify()**************')
    print(l1.nodes_list())
    l1.modify(0, 21)
    print(l1.nodes_list())
    #
    print('**************Test search()**************')
    print(l1.search(21))
    print(l1.search(20))
