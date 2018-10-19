# -*- coding: utf-8 -*-
__author__ = 'Anliven'


class Man(object):
    """this is a test"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def says(what):
        """

        :param what:
        """
        print ("hello, %s" % what)


if __name__ == '__main__':
    X = Man("test", 30)
    print (X.__dict__)
    print (dir(X))

    print (Man.__dict__)
    print (dir(Man))

    print (dir())  # dir()不带参数时，则显示调用者的局部变量


# 内置函数（built-in functions）
#
# python的内置函数可以直接调用,无需import。
# 查看所有内置函数：dir(__builtins__)
# 注意：名称的开始和结尾都是双下划线


# 特殊的内置函数
#
# __init__
# 当一个类实例被创建时， __init__() 方法会自动执行该对象的初始化工作。
# 在创建一个类的新实例的时候，把参数包括在圆括号内跟在类名后面，从而传递给__init__方法。
# 通过创建自己的 __init__() 方法， 可以覆盖默认的 __init__()方法（默认的方法什么也不做）。
#
# __name__和__main__
# 用于判断当前模块是不是程序入口，如果当前程序正在使用，__name__的值为__main__。
# 在编写程序时，通常需要给每个模块添加条件语句，用于单独测试该模块的功能。
#
# if __name__ == '__main__'
# 运行当前脚本，就会执行if __name__=="__main__"下的函数，如果模块被其他程序import的，那么就不会执行。
# 主要是测试用，测试这个模块有没有实现预期的功能。
#
# __doc__
# 每个对象都会有一个__doc__属性，用于描述该对象的作用。


# __dict__与dir()的区别
#
# __dict__属性仅仅是一个对象的局部属性集合，不包含该对象所有有效属性。
# __dict__ 返回的是一个字典，键（key）是属性名，键值（value）是相应的属性对象的数据值。
# dir()函数会自动寻找一个对象的所有完整的有效属性，包括搜索__dict__中列出的属性。
# dir() 返回的仅是对象的属性的一个名字类表。
