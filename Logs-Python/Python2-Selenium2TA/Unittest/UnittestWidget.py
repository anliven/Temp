# -*- coding: utf-8 -*-
__author__ = 'Anliven'


# 将要被测试的类 Widget， 执行测试的脚本名称为UnitAuto.py
class Widget:
    def __init__(self, size=(40, 40)):  # __init__()方法在类的一个对象被建立时，马上运行，将对象做初始化
        self._size = size

    def getsize(self):
        return self._size  # 调用 getSize()方法来使用__init__()方法中self._size,返回 self._size

    def resize(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("illegal size")
        self._size = (width, height)

    def dispose(self):
        pass

# 单元测试负责对最小的软件设计单元（模块）进行验证
# 单元测试使用软件设计文档中对模块的描述作为指南，对重要的程序分支进行测试以发现模块中的错误
# unittest 框架（又名 PyUnit 框架）为 python 语言的单元测试框架，从Python 2.1 成为一个标准模块

# 在面向对象的编程语言中都会有类的概念，类具有封装性
# 在 C++ 、java 等语言中通过 private（私有） 、protected（保护） 、public（公有）等修饰符来限定访问权限。
# 但在 Python 中没有显式的 private 和 public限定符，只要在方法名前面加上“ __ ”即可声明为 private 的

# 本示例中定义的__init__() 方法是一个私有的方法，不能直接被外部使用。要通过定义的赋值函数getsize()来访问
# 默认参数是 size=(40, 40) 在函数体中定义 self._size = size。通过变量传递，使得self._size=(40, 40)
# 此时，变量self._size 是私有的，不可被类以外的方法和函数调用。 （self 表示类本身）