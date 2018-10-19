# -*- coding: utf-8 -*-
__author__ = 'Anliven'

list_sample = [1, 'aaa', 2, 'bbb', 3, 'ccc']
for i in list_sample:
    print ("Got:%r," % i),
print ('\n')

elements = []
for i in range(0, 3):  # range()函数
    print ("Adding %d to the list." % i)
    elements.append(i)  # append()在列表尾部追加元素

print ("elements : "), (elements)
for i in elements:
    print ("%d" % i),
