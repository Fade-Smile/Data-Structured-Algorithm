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
        return self.head == 0

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
        cur = self.head
        pre_node = None  # 要删除的节点的前驱结点
        while cur:  # 遍历整个链表，直到找到需要删除的节点或者到达链表末尾 (当cur为None时，表示已经遍历完整个链表)
            if cur.data == data:  # 检查当前节点cur的数据是否等于目标值data。
                # 如果前驱结点为空，说明我们要删除的节点是第一个节点
                if not pre_node:  # 判断是否为链表的第一个节点（即没有前驱节点）。如果 pre_node 为空（None），说明要删除的节点是链表的头节点。
                    self.head = cur.next   # 这种情况下，将链表的头节点指向当前节点的下一个节点 cur.next，从而删除了头节点。
                else:  # 如果不是头节点，即 pre_node 不为空，
                    pre_node.next = cur.next  # 将前驱节点 pre_node 的 next 指针指向当前节点的下一个节点 cur.next，以跳过当前节点，从而删除了当前节点。
                self._length -= 1
                return 0
            pre_node = cur
            cur = cur.next
        return -1   # 如果遍历完整个链表都没有找到值为 data 的节点，那么函数返回 -1，表示未找到对应节点，没有执行删除操作

    def pop(self, pos):
        """ 指定位置删除节点 """

        if pos < 0 or self._length == 0:  # 检查索引有效性
            raise IndexError("索引超出范围")
        if pos == 0:  # 若要删除头节点
            pop_node = self.head
            self.head = self.head.next   # 更新链表的头节点为当前头节点的下一个节点
            self._length -= 1
            return pop_node.data

        cur = self.head
        pre_node = None
        while pos > 0 and cur:  # 如果要删除的位置不是头节点，使用 cur 和 pre_node 指针来遍历链表，直到找到要删除位置的节点。
            pre_node = cur
            cur = cur.next
            pos -= 1

        if pos == 0 and cur:  # 是否找到要删除的位置 pos，并且 cur 不为空
            pop_node = cur  # 找到目标位置后，将目标节点从链表中取出
            pre_node.next = cur.next    # 并将前一个节点 pre_node 的 next 指针指向目标节点的下一个节点
            self._length -= 1
            return pop_node.data
        else:    # 如果给定的索引超出了链表范围或者无法找到目标节点，则会引发 IndexError 异常，指示索引超出范围。
            raise("索引超出范围")



    def modify(self, pos, data):
        """ 修改链表中指定位置的节点的值 """
        pass

    def search(self, data):
        """ 查找链表中是否有节点的值为data """
        pass


if __name__ == '__main__':
    l1 = SingleLinkList()  # 新建一个链表类
    print(l1.head, l1.length())

    print('**************Test add()**************')
    l1.add(1)
    print(l1.head.data, l1.length())
    l1.add(3)
    print(l1.head.data, l1.length())
    print(l1.nodes_list())

    print('**************Test append()**************')
    l1.append(4)
    print(l1.head.data, l1.length())
    print(l1.nodes_list())

    print('**************Test insert()**************')
    l1.insert(7, 7)
    print(l1.nodes_list())

    print('**************Test remove()**************')
    l1.remove(7)
    print(l1.nodes_list())
    print(l1.length())

    print('**************Test pop()**************')
    print(l1.nodes_list())
    l1.pop(2)
    print(l1.nodes_list())
    print(l1.length())

