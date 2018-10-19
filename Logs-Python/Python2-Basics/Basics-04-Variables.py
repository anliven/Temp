# -*- coding: utf-8 -*-
__author__ = 'Anliven'

cars = 100  # "=(single-equal)" 的作用是将右边的值赋予左边的变量
drivers = 30
cars_not_driven = cars - drivers  # 下划线(underscore) 字符通常被用来隔开单词
print (cars), ("cars available."), (drivers), ("drivers available."), (cars_not_driven), ("empty cars.")
print ("Hey %s there." % "you")  # "you"是字符串，不是变量

my_name = 'Anliven'
my_age = 35
my_height = 175
my_weight = 72
print ("Let's talk about %s." % my_name)  # "%s"格式化字符串(formatstring)
print ("He's %d inches tall and %d kilos heavy." % (my_height, my_weight))  # 两个及以上的值则需要用小括号括起来
print ("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))
