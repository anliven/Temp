# -*- coding: utf-8 -*-
from os.path import exists  # exists方法将文件名作为参数，如果文件存在返回True，否则返回False
__author__ = 'Anliven'

filename = "Basics-File-sample01.txt"
print ("Opening the file : %s" % filename)
target = open(filename, 'w')  # 'w'表示写入(write)模式；'r'读取（read）；'a'追加(append)
target.truncate()  # truncate方法清空文件，小心使用

print ("Enter three lines in the file.")
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
target.write(line1 + "\n" + line2 + "\n")
target.close()

txt = open(filename)
print ("The contents of %s are shown below : " % filename)
print (txt.read())

# 文件操作
# open - 打开文件
# close – 保存并关闭文件
# read – 读取文件内容；open()方法的默认工作方式
# readline – 读取文本文件中的一行
# truncate – 清空文件，小心使用
# write – 将stuff写入文件

to_file = "Basics-File-sample02.txt"
print ("Copying from %s to %s" % (filename, to_file))
inData = open(filename).read()
print ("The input file is %d bytes long" % len(inData))  # len()函数以数字的形式返回传递的字符串的长度
print ("Does the output file exist? %r" % exists(to_file))
out_file = open(to_file, 'w')
out_file.write(inData)
out_file.close()
# 简写：open(raw_input("to_file:"),'w').write(open(raw_input("from_file:")).read())

txt = open(to_file)
print ("The contents of %s are shown below : " % to_file)
print (txt.read())
