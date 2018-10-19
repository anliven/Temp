# -*- coding: utf-8 -*-
__author__ = 'Anliven'


class JustCounter(object):
    """
    Sample.
    """
    __secretCount = 0

    def __init__(self):
        pass

    def count(self):
        """
        Sample.
        """
        self.__secretCount += 1
        print (self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
# print (counter.__secretCount)   # 不允许实例化的类访问隐藏数据，会报错：no attribute
print (counter._JustCounter__secretCount)  # 使用object._className__attrName方式访问属性

# 隐藏数据
# 在python中只要把类变量名或成员函数前面加两个下划线即可实现数据隐藏的功能。
# 对于类的实例来说，其实现数据隐藏的变量名和成员函数是不能使用的，对于其类的继承类来说，也是隐藏的。
# 可以使用object._className__attrName的方式来访问属性。
# 在隐藏数据的情况下，其继承类可以定义其一模一样的变量名或成员函数名，而不会引起命名冲突。
