# -*- coding: utf-8 -*-
__author__ = 'Anliven'

try:
    k1 = 123
    try:
        k1 = 321
    finally:  # 无论是否发生异常都将执行最后的代码。
        print ("try-finally is running")
        print (k1 / 0)
except ZeroDivisionError:  # finally块中的所有语句执行后，异常被再次提出，并执行except块代码。
    print ("try-except is running")

# 捕捉异常 - try-finally语句
# try-finally语句无论是否发生异常都将执行最后的代码。
# 注意：except语句和finally语句两者不能同时和try语句搭配使用。
# else语句不能与finally语句同时使用。
