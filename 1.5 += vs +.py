#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :1.5 += vs +.py
@Author  :Sunshine
@Date    :06/12/2023 19:09 
'''

lst = []
print(id(lst))

lst += [1]    # 等同于 lst.extend([1])
print(id(lst))

lst = lst + [1]
print(id(lst))

'''

1. += 操作符
  - lst += [1]：这个操作是就地修改列表 lst，将 [1] 添加到列表的末尾，相当于 `lst.extend([1])`。
  - print(id(lst))：输出的 id 是列表 lst 的内存地址。

2. + 操作符
  - lst = lst + [1]：这个操作创建了一个新的列表，包含原始列表 lst 的内容和 [1]，并将这个新列表赋值给变量 lst。
  - print(id(lst))：输出的 id 是新创建的列表 lst 的内存地址，而不是原始列表 lst 的地址。

所以，+= 操作符会就地修改原始列表，而 + 操作符则创建一个新的列表并重新赋值给变量。这就是两者的区别。
'''