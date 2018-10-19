# -*- coding: utf-8 -*-
__author__ = 'Anliven'

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
print (animals)
print (animals[0]), (animals[1]), (animals[2]), (animals[3]), (animals[4]), (animals[5])  # 从0开始计数
# 遍历列表
for i in animals:
    print (i),
print ('\n')


string_sample = "Apples Oranges Crows Telephone Light Sugar"
stuff = string_sample.split(' ')  # string.split()分割字符串并形成列表，默认是以空格作为分隔符
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) < 10:
    next_one = more_stuff.pop()  # list.pop()移除列表中的一个元素（从0开始计数，默认最后一个元素），并且返回该元素的值
    print ("Adding:%s," % next_one),
    stuff.append(next_one)  # list.append()在列表末尾添加新的对象
    print ("there's %d items now." % len(stuff))

print ("# Current List : "), (stuff)
print ("# After the sorting action : "), (sorted(stuff))  # 内置函数sorted()可以对list或者iterator（迭代器）进行排序
print ("# Some items : "), (stuff[0]), (stuff[1]), (stuff[-1]), (stuff.pop()), (stuff[-1])
# 从0开始计数，[0]表示第一个元素，[-1]表示最后一个元素；


print ("# Join with blank : "), (' '.join(stuff))  # string.join()连接字符串并形成一个新的字符串
print ("# Join with --- : "), ('---'.join(stuff[3:7]))
