# -*- coding: utf-8 -*-
__author__ = 'Anliven'

import random


class Fruit(object):
    """this is a Fruit test."""
    price = 0  # 定义类的变量
    __total = 32  # 定义类的变量（以双下划线开头并且不以下划线结尾），dir()时显示“_Fruit__total” 而不是__total

    def __init__(self):
        self.__color = "red"  # 在构造器__init__()用self.操作的“__color”是实例属性，不是类属性
        self.__weight = "200g"  # “self.xxx”格式第一次赋值的作用：定义了一个名为xxx的实例属性

    @staticmethod
    def guess():
        """
        sample.
        """
        li = ['apple', 'orange', 'banana']
        print (random.choice(li))


class Apple(Fruit):  # Apple类继承Fruit类
    """this is a Apple test."""
    ApplePrice = 12
    __AppleTotal = 10


if __name__ == "__main__":
    print ("Apple.__bases__ : "), (Apple.__bases__)  # 类的基类
    print ("Apple.__name__ : "), (Apple.__name__)  # 类的名字
    print ("Apple.__doc__ : "), (Apple.__doc__)  # 类的文档字符串
    print ("Apple.__dict__ : "), (Apple.__dict__)  # 类的属性
    print ("Apple dir() : "), (dir(Apple))  # 类的所有属性
    Apple.guess()
    print (Apple.price), (Apple.ApplePrice)  # 通过类名访问类的数据属性

    one = Apple()  # 实例化对象one
    print ("one.__class__ : "), (one.__class__)  # 实例所属的类
    print ("one.__class__.ApplePrice : "), (one.__class__.ApplePrice)  # 实例所属类的属性的值
    print ("one.__doc__ : "), (one.__doc__)  # 实例的文档字符串
    print ("one.__dict__ : "), (one.__dict__)  # 实例的属性
    print ("one dir() : "), (dir(one))  # 实例的所有属性，包含所属类以及所属类的父类的属性
    one.guess()
    print (one.price), (one.ApplePrice)  # 通过实例访问类的数据属性

    Apple.ApplePrice = 17  # 通过类名修改类变量，作用于该类和所有实例
    print ("className.var: "), (Apple.ApplePrice), (one.ApplePrice)
    one.ApplePrice = 15  # 通过实例修改类变量，仅仅作用于该实例
    print ("objectName.var: "), (Apple.ApplePrice), (one.ApplePrice)
    Apple.ApplePrice = 19  # 通过类名再次修改类变量
    print ("className.var again: "), (Apple.ApplePrice), (one.ApplePrice)  # 注意此时one.ApplePrice的值

# 类属性(attribute)
#
# 类的变量(也称为静态变量或静态数据)，属于整个class所共享，可以通过类名访问className.var,也可以通过实例访问objectName.var。
# 类的方法是属于这个类的函数，应用在类的实例。
#
# 特殊的类属性
# C.__name__ 	        类C的名字（字符串）
# C.__doc__ 	        类C的文档字符串 ----- 文档字符串不能被派生类继承，派生类可以书写自己的文档字符串
# C.__bases__ 	        在Python中,每个类有一个__bases__属性,列出其基类
# C.__dict__ 	        类C的属性 ----- 包含一个字典，由类的数据属性组成
# C.__module__ 	        类C定义所在的模块


# 实例属性
# 实例属性必须在构造器__init__(self) 方法中定义，但可以在实例创建后任意时间进行设置。
# 实例变量仅属于特定对象实例，只可以通过实例名访问objectName.var。
#
# 特殊的实例属性
# X.__class__ 	    实例X的类
# X.__dict__ 	    实例X的属性，就是构造器__init__(self) 方法中定义的属性


# 获取类属性或实例属性
# 内建函数dir()可以显示类和实例的所有属性，返回的仅是对象的属性的一个名字类表。
# 类和实例的字典属性__dict__返回的是一个字典，键（key）是属性名，键值（value）是相应属性对象的数据值。
#
# 一个普通对象使用一个dict来保存自己的属性，可以动态地向其中添加或删除属性。
# 许多内建类型都没有__dict__属性，例如list string等没有__dict__属性
# Python的实例以及对应的类都拥有自己的__dict__。
