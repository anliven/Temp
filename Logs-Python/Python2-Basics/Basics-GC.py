# -*- coding: utf-8 -*-
__author__ = 'Anliven'


class Point(object):
    """
    sample.
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print ("%s destroyed." % class_name)


pt1 = Point()
pt2 = pt1
pt3 = pt1
print ("id(pt1) : %s. " % id(pt1)), ("id(pt2) : %s. " % id(pt2)), ("id(pt3) : %s. " % id(pt3))
print ("type(pt1) : %s. " % type(pt1)), ("type(pt2) : %s. " % type(pt2)), ("type(pt3) : %s. " % type(pt3))
print ("pt2 == pt3: %s " % (pt2 == pt3))  # 关系运算符 "==" 比较值是否相等
print ("pt2 is pt3 : %s " % (pt2 is pt3))  # is关键字比较是否为同一个对象（同一块内存地址）
del pt1
print ("id(pt2) : %s. " % id(pt2)), ("id(pt3) : %s. " % id(pt3))

c = [3]
d = [3]
print ("id(c) : %s. " % id(c)), ("id(d) : %s. " % id(d))
print ("type(c) : %s. " % type(c)), ("type(d) : %s. " % type(d))
print ("c == d : %s " % (c == d))
print ("c is d : %s " % (c is d))

str1 = "hello python"
str2 = "hello python"
print ("id(str1)) : %s. " % id(str1)), ("id(str2) : %s. " % id(str2))
print ("type(str1)) : %s. " % type(str1)), ("type(str2) : %s. " % type(str2))
print ("str1 == str2 : %s " % (str1 == str2))
print ("str1 is str2 : %s " % (str1 is str2))

# GC(Garbage collection, 对象销毁/垃圾回收)
# Python的GC模块主要运用了“引用计数”（reference counting）来跟踪和回收垃圾。
# 在引用计数的基础上，还可以通过“标记-清除”（mark and sweep）解决容器对象可能产生的循环引用的问题。
# 通过“分代回收”（generation collection）以空间换取时间来进一步提高垃圾回收的效率。

# 引用计数器
# 当一个对象的引用被创建或者复制时，对象的引用计数加1；
# 当一个对象的引用被销毁时，对象的引用计数减1；
# 当对象的引用计数减少为0时，就意味着对象已经没有被任何人使用了，可以将其所占用的内存释放了。
#
# 使用"引用计数"来追踪内存中的对象，记录着所有使用中的对象各有多少引用。
# 当对象被创建时，就创建了一个引用计数，当这个对象不再需要时（引用计数变为0）被垃圾回收。
#
# 引用计数增加的情况：
# --对象被创建；
# --另外的别名被创建；
# --作为参数传递给函数；
# --成为容器对象的一个元素；
#
# 引用计数减少的情况：
# --一个本地引用离开其作用范围，比如函数结束时，所有局部变量都被自动销毁；
# --用del语句显式删除一个变量（同时该变量从name space中删除）；
# --对象的一个别名被赋值给其他对象；
# --对象被移出一个容器对象时；
# --容器对象本身的引用计数变成0；

# 循环垃圾收集器
# 处理循环引用（两个对象相互引用，但是没有其他变量引用他们）
# 作为引用计数的补充， 循环垃圾收集器也会留心被分配的总量很大（及未通过引用计数销毁的那些）的对象。
# 在这种情况下， 解释器会暂停下来， 试图清理所有未引用的循环。

# python的每个对象有以下三个属性：
# id，每个对象都有一个唯一标识(identity)，也就是对象的内存地址,可通过内建函数id(obj)查看
# type，对象的类型决定了该对象可以保存的值类型，可用内建函数type(obj)查看
# value，即对象的值

# 对两个变量赋予相同的值，它们有可能是同一个对象，也可能是两个不同的对象，取决于对象的类型（type）
