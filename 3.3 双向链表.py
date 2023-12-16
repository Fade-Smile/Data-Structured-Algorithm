#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :3.3 双向链表.py
@Author  :Sunshine
@Date    :11/12/2023 22:25 
'''


# 节点类
class Node(object):
    def __init__(self, data, _prev=None, _next=None):
        self.data = data                # 数据域
        self.prev = _prev               # 指针域 指向的是当前节点的前一个节点
        self.next = _next               # 指针域 指向的是当前节点的下一个节点


class DoubleLinkList(object):
    def __init__(self):
        self.head = None                # 链表的头节点
        self._length = 0                # 链表的长度

    # 判断链表是否为空
    def is_empty(self):
        return self._length == 0

    # 返回链表的长度
    def length(self):
        return self._length

    # 返回链表中的所有节点的值组成的列表
    def node_list(self):
        res = []
        cur = self.head
        while cur:
            res.append(cur.data)
            cur = cur.next
        return res

    # 住链表的头部添加一个节点,值为data
    def add(self, data):
        node = Node(data)
        if self.is_empty():                 # 若是空链表
            self.head = node                # 把头结点的指针指向新建的Node
        else:
            self.head.prev = node           # 让链表中原本的头结点的prev指针域指向新建的Node
            node.next = self.head
            self.head = node
        self._length += 1

    # 往链表的尾部添加一个节点, 值为data
    def append(self, data):
        node = Node(data)

        if self.head:
            cur = self.head             # 把当前节点的地址赋值给 cur
            while cur.next:             # 从头结点开始, 遍历链表中的所有节点
                cur = cur.next
            node.prev = cur             # 让node的prev指针域去指向原本的尾结点
            cur.next = node             # 让原本的尾结点的next去指向新建的结点
        else:                           # 若为空， 则直接把头部的next指向新建的node
            self.head = node

        self._length += 1

    # 往链表的指定位置 pos 插入一个节点，值为data
    def insert(self, pos, data):
        # 异常情况
        if pos <= 0:
            self.add(data)
        elif pos > (self.length() - 1):
            self.append(data)
        else:
            # 正常情况
            node = Node(data)
            pre = self.head
            while pos - 1:
                pre = pre.next
                pos -= 1
            node.prev = pre             # 让node的prev指向索引为pos-1的节点
            pre.next.prev = node        # 让索引为pos的节点指向新建的节点
            node.next = pre.next        # 让node的next指向索引为pos的节点
            pre.next = node             # 让索引为pos-1的节点的next指向新建的节点
            self._length += 1

    # 这段代码实现了在双向链表中删除第一个匹配给定值的节点的功能，如果存在匹配的节点则删除，否则不做任何操作。
    def remove(self, data):
        cur = self.head                             # 将cur指针设为链表的头节点，用于遍历链表
        while cur:                                  # 使用循环遍历整个链表，直到cur变成None（即遍历完整个链表）
            if cur.data == data:                    # 找到节点，其中cur.data是当前节点的数据
                if cur == self.head:                # 如果要删除的是头节点
                    self.head = cur.next            # 将头节点指向下一个节点
                else:                               # 如果要删除的节点不是头节点，则执行以下操作：
                    cur.prev.next = cur.next        # 将当前节点前一个节点的next指向当前节点的下一个节点
                if cur.next:                        # 检查当前节点的下一个节点是否存在
                    cur.next.prev = cur.prev        # 将当前节点后一个节点的prev指向当前节点的前一个节点
                self._length -= 1                   # 更新链表长度
                return 0                            # 返回0表示成功删除节点
            cur = cur.next                          # 继续遍历链表
        return -1                                   # 返回-1表示未找到要删除的数据节点

    # 修改链表中指定位置的节点的值
    def modify(self, pos, data):
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
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False

if __name__ == '__main__':
    l1 = DoubleLinkList()
    print(l1.node_list())

    print('****************** add() ******************')
    l1.add(1)
    print(l1.node_list())
    l1.add(2)
    print(l1.node_list())

    print('**************Test append()**************')
    l1.append(4)
    print(l1.head.data, l1.length())
    print(l1.node_list())

    print('**************Test insert()**************')
    l1.insert(7, 7)
    l1.insert(-1, 4)
    l1.insert(1, 17)
    print(l1.node_list())

    print('**************Test remove()**************')
    print(l1.remove(17))
    print(l1.remove(5))
    print(l1.node_list())

    print('**************Test modify()**************')
    print(l1.node_list())
    l1.modify(0, 21)
    print(l1.node_list())

    print('**************Test search()**************')
    print(l1.search(21))
    print(l1.search(20))
    