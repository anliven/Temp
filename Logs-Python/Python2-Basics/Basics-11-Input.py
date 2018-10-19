# -*- coding: utf-8 -*-
__author__ = 'Anliven'

print ("How old are you?"),
age = input()
height = raw_input("How tall are you? ")  # Python3不再支持raw_input()
weight = raw_input("How much do you weigh? ")
print ("So, you're %r old, %r tpall and %r heavy." % (age, height, weight))

# 内建函数raw_input()与input()读取控制台的输入，与用户实现交互，推荐使用raw_input()
# raw_input() 将输入当作字符串，可以不用加引号，返回字符串类型
# input()  输入为纯数字时，返回数值类型；输入字符串表达式时，需要使用引号''或者双引号""，会计算字符串中的数字表达式
# type()  可以查看返回值类型
