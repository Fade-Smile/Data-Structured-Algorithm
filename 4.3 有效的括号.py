#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python数据结构和算法 
@File    :4.3 有效的括号.py
@Author  :Sunshine
@Date    :17/12/2023 13:53 
'''

from Stack_LinkedList import Stack

"""
遍历字符串
遇到左边括号, 就入库
遇到右边括号, 栈是否为空
为空 --> False 
不为空, 弹出栈顶元素
栈顶元素和遇到的右边括号匹配一下, 看是否是相同类型
若是不同类型, 返回False
若相同类型, 则继续往下遍历
如果字符串全部匹配完了
栈为空 --> True
栈不为空 --> False 
"""


# Method 1
def func(string):
    if len(string) % 2:
        return False
    stack = Stack()
    dic = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for char in string:
        # 判断遇到的是左括号还是右括号
        if char in '([{':
            stack.push(dic[char])
        else:
            if stack.is_empty() or stack.pop() != char:
                return False
    return stack.is_empty()


# Method 2
def isValid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}  # 用于匹配右括号和对应的左括号

    for char in s:
        if char in mapping:  # 如果是右括号
            top_element = stack.pop() if stack else '#'  # 弹出栈顶元素或者使用特殊字符标记
            if mapping[char] != top_element:
                return False
        else:  # 如果是左括号
            stack.append(char)

    return not stack  # 检查栈是否为空


if __name__ == '__main__':
    print(func('((()))'))               # 输出 True
    print(func('((())'))                # 输出 False
    print(func('(()))'))                # 输出 False
    print(func('()[]{}'))               # 输出 True
    print(func('(' * 20 + ')' * 19))    # 输出 False
    print('*'*20)
    print(isValid("({[]})"))            # 输出 True
    print(isValid("(]"))                # 输出 False
    print(isValid("([)]"))              # 输出 False
