# -*- coding: utf-8 -*-
__author__ = 'Anliven'

import random  # 模块名称使用不带下划线的小写字母


class BaseFruit(object):  # 对于基类而言，可使用一个 Base 或者 Abstract 前缀
    """Sample."""
    AVG_PRICE = 5  # 大写加下划线，仅用来标明是不会发生改变的全局变量
    __a = 22  # 双下划线开头的变量，表示名字改编

    def __init__(self):  # 双下划线开头双下划线结尾的函数，Python的魔术方法（内置方法/特殊方法）
        self.__color = "red"
        self.__code = 11


class Apple(BaseFruit):  # 类名应该简明精确；驼峰格式命名，即所有单词首字母大写其余字母小写
    """Sample."""
    __number = 10
    _weight = "200g"  # 单下划线开头并且结尾没有下划线，仅用于警告外部类不要去访问它，但实际上还是可以访问

    @staticmethod
    def _apple_price():  # 单下划线开头并且结尾没有下划线，仅用于警告外部类不要去访问这个函数，，但实际上还是可以访问
        return random.randint(5, 10)


if __name__ == "__main__":
    print (Apple.__dict__)  # 类的属性

    one = Apple()
    print (one.__dict__)  # 对象one的实例属性
    print (dir(one))  # 对象one所有有效属性
    print (one._apple_price())  # 仍然可以访问，说明仅用于警告而不是强制限定
    print (one._weight)  # 仍然可以访问，说明仅用于警告而不是强制限定

    AVG_PRICE = 3
    print (AVG_PRICE)  # 仍然可以改变值，说明仅用于警告而不是强制限定

# 单下划线开头
# 在一个模块（例如a_module）中以单下划线开头的变量和函数相当于“私有变量”和“私有函数”，不希望外部的类访问它们
# 使用 from a_module import * 导入时，这部分变量和函数不会被导入
# 但如果使用 import a_module 导入模块，仍然可以用 a_module._some_var 这样的形式访问到这样的对象
#
# 单下划线结尾
# 在解析时并没有特别的含义，但通常用于和 Python 关键词区分开来
# 例如： 定义一个变量叫做class，但class是Python的关键词，此时可以以单下划线结尾写作class_
#
# 双下划线开头，结尾没有下划线
# 在Python的类成员中使用，表示名字改编 (Name Mangling)，可用于避免该类成员的名称与子类中的名称冲突
# 例如：Test类里有一成员__x，那么 dir(Test) 时会看到 _Test__x 而不是 __x
#
# 双下划线开头，双下划线结尾
# 变量---标明是内置变量
# 函数---Python的魔术方法，例如：类成员的 __init__、__del__、__add__、__getitem__ 等，以及全局的 __file__、__name__ 等
# Python 官方推荐永远不要将这样的命名方式应用于自己的变量或函数，而是按照文档说明来使用


# Python的代码风格
# Python的代码风格由PEP8描述
# 在遵守这个文档的条件下，不同程序员编写的Python代码可以保持最大程度的相似风格，易于阅读和程序员之间交流
# 可以安装一个PEP8用于验证你的代码风格是否符合PEP8规范
