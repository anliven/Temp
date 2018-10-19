# -*- coding: utf-8 -*-
__author__ = 'Anliven'


class ShortInputException(Exception):  # 定义一个子类ShortInputException，是Exception类的派生类。
    """A user-defined exception class."""

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    s = raw_input('Enter something --> ')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)  # raise语句来主动的触发
except EOFError:
    print ('\nWhy did you do an EOF on me?')  # 伴随异常触发的异常对象
except ShortInputException as x:
    print ('ShortInputException: The input was of length %d, was expecting at least %d' % (x.length, x.atleast))
else:
    print ('No exception was raised.')

# 触发异常 - raise语句主动触发异常
# 可以使用raise语句来主动的触发Python程序的异常。
# 可以引发的异常应该是典型的继承自Error或Exception类，通过直接或间接的方式。
# 为了能够捕获异常，"except"语句必须用相同的异常类来捕获抛出的类对象或者字符串。
