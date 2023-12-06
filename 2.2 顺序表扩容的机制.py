#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :2.2 顺序表扩容的机制.py
@Author  :Sunshine
@Date    :06/12/2023 22:20 
'''

lst = []
''' 
列表对象
表头 容量 元素个数
数据区
lst.allocated 容量
lst.size元素个数
lst, items = 数据区
'''
lst.append(1)

PY_SSIZE_T_MAX = float('inf')  # 最大值
obj_size = 1


class List:
    allocated = 0
    size = 0
    items = []

    def list_resize(self, new_size):
        '''
        这是一个列表的扩容或缩容的流程

        self: 列表对象本身
        :param new_size: 修改之后的元素个数
        :return:
        '''

        allocated = self.allocated  # 获取当前对象的容量
        # allocated >> 1 ==> allocated //2  (以二进制的方式位移)
        if allocated >= new_size >= (allocated >> 1):  # 判断当前对象的容量是否在这个范围内
            self.size = new_size  # 如果在， 只需要修改其元素个数即可
            return 0
        # 如果不在就需要扩容或者缩容

        # 计算需要的内存容量是多少
        new_allocated = new_size + (new_size >> 3) + (3 if new_size < 9 else 6)  # 内存容量最少为3
        # 计算一个新的值new_allocated，该值等于 new_size 加上 new_size 右移3位的结果，
        #   [这相当于将 new_size 除以 2 的 3 次方（即将 new_size 除以 8 并取整数部分）。]
        # 再加上一个条件表达式的结果（根据 new_size是否小于9而定，小于9时结果为3，否则为6）。

        if new_allocated > PY_SSIZE_T_MAX:  # 判断是否超过要求的最大值, 若超过就报错
            return -1

        if new_size == 0:   # 若没有超过， 继续判断 修改之后列表中的元素个数是多少。 若为0， 那就说明 列表为空 (属于不符合要求)
            new_allocated = 0  # 当 new_size 的值为零时，这意味着列表将不包含任何元素， 所需的内存空间也可以为零。

        # 计算new_allocated之后， 计算容量需要的字节数
        # (obj_size : 对象占用的字节数是多少, 例如
        #           int 类型在32位系统上，int 类型占用4个字节（32位）。
        #                   在64位系统上，int 类型通常占用8个字节（64位）。
        num_allocated_bytes = new_allocated * obj_size

        # 根据 new_allocated 列表应该分配的新容量 和 obj_size 是每个列表项所占用的字节数 来申请新的内存空间的地址
        items = addr(self.items, num_allocated_bytes)
        if items == None:  # 判断 内存空间是否申请成功
            return -1
        # 若成功就更新一下顺序表的表头： 容量， 元素个数， 以及数据区的地址
        # 让列表对象指向新的内存空间地址
        self.items = items
        self.size = new_size
        self.allocated = new_allocated
        return 0
