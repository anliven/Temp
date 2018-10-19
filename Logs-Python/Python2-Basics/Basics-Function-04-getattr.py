# -*- coding: utf-8 -*-
__author__ = 'Anliven'


class Man(object):
    """
    sample.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def says(what):
        """

        :param what:
        """
        print ("hello, %s" % what)


X = Man("Object exists.", 30)
print (getattr(X, 'name', 'not found.'))  # 如果对象属性name存在，打印self.name的值，否则打印”not find“
print (getattr(Man, 'says_test', 'not find'))  # 如果类方法says_test存在，打印信息，否则打印"not find"

print (hasattr(X, 'age'))  # 如果对象X有age属性则打印True，否则打印False
setattr(Man, 'action', 'run')  # 为man类添加属性action和值
setattr(X, 'height', '6feet')  # 为对象X添加属性height和值，相当于执行 X.height = '6feet'
delattr(X, 'age')  # 删除对象X的属性age，相当于执行 del X.age

print ("Man __dict__ : "), (Man.__dict__)
print ("X __dict__ : "), (X.__dict__)


# getattr()函数
# 可以获取对象引用，返回对象的任意属性或者方法。
# 通常， getattr(object,"attribute") 相当于 object.attribute。
# 如果 object 是一个模块，那么attribute 可以是定义在模块中的函数，类，或全局变量。
#
# setattr()函数
# 添加或者修改指定的属性；setattr(对象，属性，属性的值)
#
# delattr()函数
# 删除指定的对象属性；delattr(对象，属性)
#
# hasattr()函数
# 确定一个对象是否具有某个属性，属性存在返回True，否则返回False；hasattr(对象，属性)
