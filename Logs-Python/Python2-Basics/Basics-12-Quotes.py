# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# 单引号（single quotation），双引号（double quotation），多引号（triple quotes）区别
print ('hello,world'), ("hello,world"), ('''hello,world'''), ("""hello,world""")

print ('Let\'s go!')  # 转义字符“\”
print ("Let's go!")  # 用 " 来表示字符串,python就把字符串中的单引号 ' , 当成普通的字符处理.

print ("hello,\
world")  # 使用连行符“\”
print ('''hello,
world''')  # 使用3个单引号或双引号写成多行
