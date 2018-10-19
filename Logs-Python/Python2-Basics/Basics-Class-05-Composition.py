# -*- coding: utf-8 -*-
__author__ = 'Anliven'


class Other(object):
    """
    sample.
    """

    @staticmethod
    def aaa():
        """
        sample.
        """
        print ("OTHER---aaa().")

    @staticmethod
    def bbb():
        """
        sample.
        """
        print ("OTHER---bbb().")

    @staticmethod
    def ccc():
        """
        sample.
        """
        print ("OTHER---ccc().")


class Child(object):
    """
    sample.
    """

    def __init__(self):
        self.other = Other()  # 直接使用Other类实例化对象

    def bbb(self):
        """
        sample.
        """
        self.other.bbb()  # 直接调用Other类的bbb方法

    @staticmethod
    def aaa():
        """
        sample.
        """
        print ("CHILD, aaa().")

    def ccc(self):
        """
        sample.
        """
        print ("Child, Before Other ccc()")
        self.other.ccc()  # 直接调用Other类的ccc方法
        print ("Child, After Other ccc()")


son = Child()
son.bbb()
son.aaa()
son.ccc()

# 合成(Composition):直接使用别的类和模块，实现与继承相同功能的方法;
# 如果有一些代码会在不同位置和场合应用到，利用合成能够解决这样的代码重用问题;
