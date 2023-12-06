#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :1.4 Timeit 模块.py
@Author  :Sunshine
@Date    :06/12/2023 17:57 
'''

'''
class timeit.TimerTimer(stmt, setup, timer, globals)    # 创建一个Timer对象
        stmt: statement,要测试的代码语句
        setup: 执行测试代码需要的环境,比如import语句
        timer:定时器函数有默认值,一般使用默认值即可
        globals:代码的作用域传一些要用到的变量组成的字典

Timer.timeit(number=1000000)
将Timer对象的测试语句执行number次,默认为1000000次返回执行语句的平均耗时
'''
import timeit


def list_append():
    # 像一个空列表中添加一个 0 - 10000 的元素

    lst = []
    for i in range(1001):
        lst.append(i)


def list_insert_tail():
    # 像一个空列表中添加一个 0 - 10000 的元素

    lst = []
    for i in range(1001):
        lst.insert(-1, i)  # 尾部插入元素


def list_inset_head():
    # 像一个空列表中添加一个 0 - 10000 的元素

    lst = []
    for i in range(10000, -1, -1):
        lst.insert(0, i)  # 将范围从 10000 到 0 的整数逆序插入到列表 lst 的开头（索引 0 处），由大到小顺序插入。


def list_extend():
    # 像一个空列表中添加一个 0 - 10000 的元素

    lst = []
    for i in range(1001):
        lst.extend([i])


def list_concat_1():
    # 像一个空列表中添加一个 0 - 10000 的元素

    lst = []
    for i in range(1001):
        lst = lst + [i]


def list_concat_2():
    # 像一个空列表中添加一个 0 - 10000 的元素

    lst = []
    for i in range(1001):
        lst += [i]


def list_comprehension():
    # 像一个空列表中添加一个 0 - 10000 的元素
    lst = [i for i in range(1001)]


def list_range():
    lst = list(range(1001))


# 创建函数列表
func_list = [list_append, list_comprehension, list_concat_1, list_concat_2,
             list_extend, list_inset_head, list_insert_tail, list_range]

# 储存结果的列表
results = []

# 测试每个函数的执行时间
for func in func_list:
    t = timeit.Timer('func()', globals={'func': func})
    execution_time = t.timeit(1000)
    results.append((func.__name__, execution_time))  # 将函数名和执行时间存入结果列表

# 按照执行时间长短对结果进行排序
results.sort(key=lambda x: x[1])

# 输出按照时间长短排序后的结果
for result in results:
    print(f'{result[0]} 运行时间: '.ljust(30), result[1], '秒')

# t = timeit.Timer('lst_append', 'from __main__ import lst_append')
# 'from __main__ import lst_append': 是为了确保 lst_append 函数在 timeit 模块的环境中可用。
# from __main__ import lst_append 语句会将当前模块中的 lst_append 函数引入 timeit 模块中，以便在计时的代码中使用。
# print('append 方法使用的时间为:', t.timeit(1000))
