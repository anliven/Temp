# -*- coding: utf-8 -*-
__author__ = 'Anliven'

letters = {
    'AAA': 'aaa',
    'BBB': 'bbb'
}
letters['CCC'] = 'ccc'  # 增加新键值对
print (letters['AAA']), (letters['BBB']), (letters['CCC'])  # 通过键名访问对应的值

for x, y in letters.items():  # dict.items()以列表返回可遍历的(键, 值) 元组数组
    print ("%s---%s, " % (x, y)),
print ("\n")

numbers = dict(aaa=111, bbb=222)
numbers['ccc'] = 333  # 增加新键值对
print (numbers['aaa']), (numbers['bbb']), (numbers['ccc'])  # 通过键名访问对应的值
print (numbers[letters['AAA']]), (numbers[letters['BBB']]), (numbers[letters['CCC']])

for x, y in letters.items():
    print ("%s---%s---%s, " % (x, y, numbers[y])),
print ("\n")

x = letters.get('DDD', None)  # 使用dict.get()访问字典的key值不存在时，返回None,可自定义None；
if not x:
    print ("Sorry, no EEE.")
y = numbers.get('ddd', 'Does Not Exist.')  # 自定义None
print ("%s" % y)
