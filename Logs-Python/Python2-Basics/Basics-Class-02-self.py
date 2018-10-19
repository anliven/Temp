# -*- coding: utf-8 -*-
__author__ = 'Anliven'


class TheMultiplier(object):
    """
    sample.
    """

    def __init__(self, base):  # __init__函数是一个特殊的初始方法，可以预设重要的变量；self是Python创建的空对象；
        self.base = base  # 初始化值

    def do_it(self, m):
        """
        :param m:
        :return:
        """
        return m * self.base


x = TheMultiplier(20)
print ("Multiplier: "), (x.do_it(30))


# 理解self
# 定义类的方法时，必须有self参数（即使类的方法不需要任何参数）；但调用类的方法时却不必为self参数赋值；
# self参数所指的是对象本身

# 不必为self赋值的原因
# 举例说明：
# 1. 创建了一个类 MyClass，实例化 MyClass 得到了 MyObject 这个对象，然后调用这个对象的方法 MyObject.method(a,b)
# 2. 在这个过程中， Python会自动转为MyClass.method(MyObject,a,b)， 这就是Python的 self 的原理。
# 即使类的方法不需要任何参数，但还是得给这个方法定义一个 self 参数，虽然在实例化调用的时候不用理会这个参数。

# self 是编程规范约定的在对象的方法中用来指代实例的变量名称
# 应该出现在方法定义的第一个位置参数处，并可以在方法内部用来通过它访问实例。
# 简单的说，self就是类实例自身的引用。
# self只有在类的方法中才会有，独立的函数或方法是不必带有self的。
# 在定义类方法时(即定义类中的函数)，第一个参数必须是self。

# 相对于普通的函数，类的方法只有一个特别的区别：必须有一个额外的第一个参数名称。
# 这个特别的参数指对象本身，按照惯例它的名称是self。
# 但是在调用这个方法的时候不必为这个参数赋值，Python会提供这个值。

# self指的是类实例对象本身(注意：不是类本身)。
# 为什么不是指向类本身呢？如果self指向类本身，那么当有多个实例对象时，将无法明确self指向哪一个。


###  对象使用self注意事项
# 1.  在定义类方法时(即定义类中的函数)，第一个参数必须是self
# 2.  在方法内调用类属性(变量以及其它方法)：所有属于一个类的对象都会共享这些属性；通过self调用类属性（即使用self调用变量及其他方法）
# 3.  在类中调用父类的方法时，方法中的第一个参数必须是self。
# 4.  从类外部调用类方法时，不必对self参数指定任何值


##### Python如何给self赋值以及为何不需要给它赋值。
# 举一个例子：
# 假如一个类称为MyClass，类的方法method(arg1, arg2)和这个类的一个实例MyObject。
# 当调用这个对象的方法MyObject.method(arg1, arg2)的时候，这时Python自动转为MyClass.method(MyObject, arg1, arg2)。


# ----------------------------------------------------------------------------------------------------------------------
##### 一个实际的例子


class Person:

    def __init__(self, name):  # 构造器__init__（）在类的实例被创建后自动执行，用于初始化一个类的实例。一个类也可以没有__init__的。
        self.name = name    # self指的是类对象实例本身的引用(注意：不是类本身)。在这里，就是指调用Person类创建的实例p。
                            # 而self.name相当于创建了一个数据属性（实例的变量）。变量名是name，值是传进来的那个'tianya'.

    def SayHello(self):
        print 'My name is:', self.name

p = Person('tianya')  # 创建类Person的实例P。实际上，这里应该为：p = Person(self,'tianya'),只不过Python自动加上了self。
p.SayHello()
print p.name  # 如果执行print p.name 则会显示：’tianya‘.

# 上面例子中，当Person类的实例p被创建后，__init__会立刻被调用来初始化实例p，会执行p.name=name， self.name实际上就会被p.name所代替。
# 所以当执行p＝Person('tianya')时，“tianya”会被当作参数传到__init__中，执行p.name='tianya'。


