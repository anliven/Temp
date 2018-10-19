# -*- coding: utf-8 -*-
from sys import argv  # 引入sys库的argv功能；“from 模块名 import *”可以导入模块的所有方法

__author__ = 'Anliven'

script, filename = argv
# filename = "Basics-File-sample01.txt"
txt = open(filename)  # open方法打开文件，返回一个文件对象
print ("Here's your file %r." % filename)
print ("The contents of txt file are shown below : ")
print (txt.read())  # 利用文件对象的read方法获取文件内容

# 获取open方法的信息：“python -m pydoc open”
# 运行程序:"python Basics-File-01.py Basics-File-sample01.txt"