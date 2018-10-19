# -*- coding: utf-8 -*-
__author__ = 'Anliven'

try:
    a = 10
    b = 0
    print (a / b)  # 因分母可以为零，会产生“ZeroDivisionError: integer division or modulo by zero”的异常错误
except ZeroDivisionError as e:  # 提供用来表示错误/异常对象的变量e
    print (e)  #


def temp_convert(var):
    """
    :param var:
    """
    try:
        print (int(var))
    except ValueError as Argument:  # 提供用来表示错误/异常对象的变量Argument
        print ("The argument does not contain numbers.")
        print ("The argument does not contain numbers. %s" % Argument)  # 对比理解Argument的作用


temp_convert("xyz")

# 异常的参数
# 一个异常可以带上参数来输出异常信息，通过except语句来捕获异常的参数
# 这个参数是用来表示错误/异常对象的变量，可以接收一个或者多个异常值，通常包含错误字符串，错误数字，错误位置等
