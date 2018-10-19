# -*- coding: utf-8 -*-
__author__ = 'Anliven'


class Parent(object):
    """
    sample.
    """

    def __init__(self):  # 类被创建时自动调__init__函数；
        self.name = "This is father."  # 初始化值；
        print(self.name)

    def aaa(self):
        """
        sample.
        """
        print ("Calling parent method---aaa().")

    @staticmethod
    def bbb():
        """
        sample.
        """
        print ("Calling parent method---bbb().")


class Child(Parent):
    """
    sample.
    """

    def __init__(self, age):  # 重新定义__init__函数，覆盖父类的同名函数；
        Parent.__init__(self)  # 通过类名直接调用父类__init__方法，必须提供self参数；
        self.age = age  # 增加了一个属性；
        print("Child Age : %s. " % self.age)

    def aaa(self):  # 显式覆写：在子类中覆写父类的方法，从而实现新功能；
        """
        sample.
        """
        print ("Child, aaa().")


class ChildNew(Parent):  # 隐式继承：在父类里定义了一个函数，但没有在子类中定义;
    """
    sample.
    """
    pass  # 创建空的代码区块;


dad = Parent()
dad.bbb()
dad.aaa()

son = Child("35")
son.bbb()  # 调用--隐式继承（Implicit Inheritance）
son.aaa()  # 调用--显式覆写（Explicit Override）

sonNew = ChildNew()
sonNew.bbb()

print (issubclass(Child, Parent))  # 判断类Child是否是类Parent的子类
print (isinstance(Parent, Child))  # 判断类Parent是否是类Child的子类
print (isinstance(son, Child))  # 判断son是不是类Child的实例对象
print (isinstance(son, Parent))  # 判断son是不是类Parent的实例对象

# 面向对象把一类数据和处理这类数据的方法封装在一个类中，让程序的结构更清晰，不同的功能之间相互独立；
# 面向对象的继承：可以把相关的数据和方法封装在一起，并且可以把不同类中的相同功能整合起来；
#
# 继承(Inheritance)：一个类的大部分或全部功能都是从一个父类中获得；
# 隐式继承（Implicit Inheritance）： 在父类里定义了一个函数，但没有在子类中定义；
# 显式覆写（Explicit Override）： 也被称作重载（Override），就是在子类中覆写父类的方法，从而实现新功能；
#
# 1：在继承中父类的构造（__init__()方法）不会被自动调用，需要在其子类的构造中亲自专门调用
# 2：通过类名调用父类的方法时，需要带上self参数
# 3：Python总是首先查找对应类型的方法，如果不能在子类中找到对应的方法，才开始到父类中逐个查找
#
# 使用issubclass()或者isinstance()方法来检测类之间或者类与实例对象之间的关系。
#   issubclass(sub,sup) --- 布尔函数，判断一个类是否是另一个类的子类或者子孙类，如果是则返回True。
#   isinstance(obj, Class) --- 布尔函数，如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回True。
