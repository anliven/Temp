# -*- coding: utf-8 -*-
__author__ = 'Anliven'


class Person(object):  # 声明一个新式类;旧式类的格式类似于Person()；
    """
    sample.
    """

    def __init__(self, name):
        self.name = name
        print ("Person created.")

    def person_name(self):
        """
        sample.
        """
        print ("Person's name : "), (self.name)


class Employee(Person):
    """
    sample.
    """

    def __init__(self, name):  # 重新定义__init__函数，覆盖父类同名函数；
        Person.__init__(self, name)  # 直接类名调用父类的 __init__ 方法；
        print ("Employee created.")

    def employee_name(self):
        """
        sample.
        """
        print ("Employee's name : "), (self.name)


class Developer(Employee, Person):  # 类的多重继承(multiple inheritance)： 定义的类继承了多个类
    """
    sample.
    """

    def __init__(self, name):
        super(Developer, self).__init__(name)  # 将父类的 __init__ 方法运行起来；使用super()不用显式引用基类；
        print ("Developer created.")


An = Developer("An")
An.person_name()
An.employee_name()
print (An.__class__.__mro__)  # mro()方法获得类的继承顺序


# super()机制用来解决多重继承
# super(class, self)事实上调用了super类的初始化函数，产生了一个super对象，也就是说super()实际上是一个类名而非函数；
# super()只能用于新式类，用于经典类时就会报错；
# super()或直接类名调用最好只选择一种形式，不要混合的用；
#
# 新式类：必须有继承的类，如果无继承的，则继承object
# 经典类：没有父类，如果此时调用super就会出现错误“super() argument 1 must be type, not classobj”
#
# 多重继承带来的麻烦往往比能解决的问题多，所以要极力避免多重继承；
