# -*- coding: utf-8 -*-
__author__ = 'Anliven'


def fun(un='xxx@yeah.net', pw='xxx'):
    print "success reader username and password!"
    return un, pw

# 函数可以预先给参数化赋值借助这个特性，可以通过调用函数的方式对用户名密码进行参数化
# 赋值内容如果是字符串需要加引号，如果是数字可以不需要引号


def zidian():
    data = {'xxxy@yeah.net': 'xxx', 'test': 123456}
    print "This operation succeeds, you will get the information!"
    return data

# 读取用户名和密码两个值，那么可以借助 python 字典的方式来完成这个需求
# 创建字典用大括号，数据由 key/value 键值对组成
# 字典的可以方便的存放 k,v 键值对，一个键对应一个值；注意，如果密码中有非数字，需要加引号
# keys()方法返回字典中的键列表。
# values()返回字典中的值列表，
# items()返回（key，value）元组。
