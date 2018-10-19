# -*- coding: utf-8 -*-
__author__ = 'Anliven'


class NetworkWrongError(RuntimeError):  # 创建了一个RuntimeError的子类，用于在异常触发时输出更多的信息
    """
    Sample.
    """

    def __init__(self, arg):
        self.arg = arg


try:  # 在try语句块中，用户自定义的异常后执行except块语句
    raise NetworkWrongError("Bad hostname")  # 触发异常
except NetworkWrongError as e:  # 这里的变量e是NetworkWrongError类的实例
    print (e.arg)

# 用户自定义异常
# 通过创建一个新的异常类，程序可以命名它们自己的异常
# 自定义异常应该是典型的继承自Exception类，通过直接或间接的方式
