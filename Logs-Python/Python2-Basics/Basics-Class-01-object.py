# -*- coding: utf-8 -*-
__author__ = 'Anliven'


class Employee(object):  # class关键字创建类，class之后为类的名称并以冒号结尾
    """Common base class for all employees"""  # 类的文档字符串（帮助信息），通过ClassName.__doc__查看
    empCount = 0  # 定义类变量，它的值在这个类的所有实例之间共享，可通过“类名.变量名”访问

    def __init__(self, name, salary):  # 创建类的实例时调用__init__()方法，被称为类的构造函数或初始化方法
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @staticmethod  # 静态方法
    def display_count():
        """
        sample.

        """
        print ("Total Employee %d" % Employee.empCount)

    def display_employee(self):
        """
        sample.

        """
        print ("Name: %s, Salary: %d." % (self.name, self.salary))


# 创建实例对象
emp1 = Employee("AAA", 30000)  # 创建一个类的实例对象，使用类的名称并通过__init__方法接受参数
emp2 = Employee("BBB", 50000)

# 访问实例的属性
emp1.display_employee()  # 使用“实例名.属性名”方式访问对象的属性
emp2.display_employee()
print ("Total Employee : %d." % Employee.empCount)  # 使用类的名称访问类变量

# 设置实例的属性
emp1.age = 7  # 添加一个age属性
print ("emp1.age new : "), (emp1.age)
emp1.age = 8  # 修改age属性
print ("emp1.age change : "), (emp1.age)
del emp1.age  # 删除age属性

# 使用函数方式来访问属性：
setattr(emp2, 'age', 9)  # setattr(obj,name,value) : 设置一个属性；如果属性不存在，会创建一个新属性
print ("emp2.age new : "), (emp2.age)
print (getattr(emp2, 'age'))  # getattr(obj, name[, default]) : 访问对象的属性
print (hasattr(emp2, 'age'))  # hasattr(obj,name) : 检查是否存在一个属性，如果存在age属性返回True
delattr(emp2, 'age')  # delattr(obj, name) : 删除属性

# 一些内置类属性
print ("Employee.__name__:"), (Employee.__name__)  # __name__: 类名
print ("Employee.__doc__:"), (Employee.__doc__)  # __doc__: 类的文档字符串
print ("Employee.__module__:"), (Employee.__module__)  # __module__: 类定义所在的模块
print ("Employee.__dict__:"), (Employee.__dict__)  # __dict__: 类的属性


# 面向对象(Object Oriented)
# 面向对象把一类数据和处理这类数据的方法封装在一个类中，让程序的结构更清晰，不同的功能之间相互独立。
# 类和对象是面向对象编程的主要两个方面。
#
# 类(Class): --- 用来描述具有相同的属性和方法的对象的集合。定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 类变量： --- 类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 数据成员： --- 类变量或者实例变量用于处理类及其实例对象的相关的数据。
# 方法重载： --- 如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程也称为方法的覆盖（override）。
# 实例变量： --- 定义在方法中的变量，只作用于当前实例的类。
# 继承： --- 一个派生类（derived class）继承基类（base class）的字段和方法。
# 实例化： --- 创建一个类的实例，类的具体对象。
# 方法： --- 类中定义的函数。
# 对象： --- 通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
#
# 模块(module)是包含函数和变量的Python文件；import这个文件后，可以使用 ‘.’ 操作符访问到模块中的函数和变量；
# 类(class)是在Python文件中包含函数和数据的一种代码结构；
# 将一个类实例化(instance)以后，就得到一个对象(object)；


# 类（class）是一种抽象的类型，而对象（object）是这种类型的实例。
# 类可以有属于它的函数，这种函数被称为类的“方法”。
# 类方法和之前定义的函数区别在于，第一个参数必须为self。
# 类/对象可以有属于它的变量，这种变量被称作“域”。域根据所属不同，分别被称作“类变量”和“实例变量”。
# 域和方法被合称为类的属性。


# 类方法与普通的函数区别在于，第一个参数必须为self，这个self是指对象本身。
# 通过“对象.方法名()”格式调用类的方法，不需要为self这个参数赋值，Python会提供这个值。
# self在类方法中的值，就是调用的这个对象本身。


class Song(object):
    """
    sample.
    """

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def singing(self):  # 增加一个类的方法，第一个参数必须为self，是指对象本身
        """
        sample.
        """
        for line in self.lyrics:
            print (line)

    @staticmethod
    def some_function():
        """
        sample.
        """
        print ("Got called.")


happy_birthday = Song(["Happy birthday to you!", "Happy birthday to you!", "Happy birthday to my Angel！"])
happy_birthday.singing()
happy_birthday.some_function()

# 创建 __init__ 或者类函数时，书写self变量，说明是实例的属性
# 实例化对象的过程
# 1- Python环境获取类的定义信息，创建一个空对象（包含类中def定义的所有函数）；
# 2- 如果类中包含魔法函数（__init__），Python环境会调用这个函数对空对象实现初始化；
# 3- 最后Python将这个新建的空对象赋给一个变量，以供后面使用；
