# -*- coding: utf-8 -*-
__author__ = 'Anliven'


def say_hello():  # 使用def关键字定义函数
    """
    sample.
    """
    print ('hello world!')  # 定义函数体（缩进的代码块）


def hi_hello(someone):
    """
    sample.
    """
    print (someone + ' says Hello!')


def plus(num1, num2):
    """
    sample.
    """
    return num1 + num2  # return是函数的结束语句，一旦执行函数就会结束；return后面的值被作为函数的返回值


def print_one(arg1):  # 接受单个参数
    """

    :param arg1:
    """
    print ("arg1: %r" % arg1)


def print_none():  # 不接受参数
    """
    no args
    """
    print ("No args.")


def print_two(arg1="OOO", arg2="KKK"):  # 接受两个参数；指定默认参数值
    """

    :param arg1:
    :param arg2:
    """
    print ("arg1: %r, arg2: %r" % (arg1, arg2))


say_hello()
hi_hello("Anliven")  # 字符串类型的参数值不能少了引号
print (plus(num1=3, num2=5))  # 可以根据形参的名称指定实参，但必须提供所有的参数
print (plus(6, num2=6))  # 注意:没有指定参数名的参数必须在所有指定参数名的参数前面，且参数不能重复,否则会报错

str1 = "AAA"
str2 = "BBB"
print_one("AAA")
print_two()  # 默认参数值
print_two(str1, str2)  # 在函数里用变量名
print_two(str1 + str2, str1 + str2)  # 在函数里做运算
print_two(str1 + str2 + "CCC", str1 + str2 + "CCC")  # 将变量和运算结合
print_none()


# 函数是可重用的程序段，能提高应用的模块性和代码的重复利用率
# 定义函数:
#   函数代码块以def关键词开头，后接函数标识符名称和圆括号();
#   函数名只以字母数字以及下划线组成，而且不是数字开始;
#   任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。不能使用重复的参数名;
#   函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明;
#   函数内容以冒号起始，并且缩进;
#   Return[expression]结束函数，选择性地返回一个值给调用方;不带表达式的return相当于返回 None;


# 函数的帮助文档
# 函数的帮助文档就是定义函数时放在"""之间的内容，也被称作 documentation comments （文档注解）
# 命令行下执行help（模块名）或help（模块名.方法名）会得到对应的帮助文档信息


# 函数的参数
# 在括号里定义参数，多个参数之间用逗号隔开
# 参数在函数中相当于一个变量，参数的值可以在调用函数时赋予
# 函数调用时根据参数的位置进行匹配，因此参数赋值的数量和类型必须跟函数的定义保持一致
#
# 函数定义时的参数名(num1, num2)称为形参，调用时提供的参数值(3,5)称为实参
#
# 带默认值的函数
# 在函数定义时，可以指定参数的默认值，当没有提供实参时，使用默认值作为实参
# 指定参数默认值的函数可以在调用时更加简洁


def func1(*args):  # 传入不定数目的参数
    """

    :param args:
    """
    arg1, arg2, arg3 = args
    for i in args:
        print ("arg"), (i)
    print ("arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3))


def func2(**args):  # 以字典（键值对）的形式传入不定数目的参数
    """

    :param args:
    """
    for k in args:
        print (k, ':', args[k])


def func3(x, y=5, *a, **b):  # 多种参数传递方式混合使用(不建议)
    """

    :param x:
    :param y:
    :param a
    :param b
    """
    print (x, y, a, b)


func1("aaa", "bbb", "ccc")
func2(a=1, b=2, c=3)
func3(1, 2, 3)
func3(1, 2, 3, 4)
func3(1, 2, 3, 4, k=1, t=2, o=3)


# 不定数目的参数
#
# (*args)
# 函数在定义时在形参前加上星号前缀(*args)，并不指明参数个数，可以处理任意参数个数的情况；
# 调用时的实参会存储在一个 tuple（元组）对象中，赋值给形参；
# 在函数内部，需要对参数进行处理时，只对这个tuple 类型的形参（这里是 args）进行操作；
# 可以按参数名传递参数（不受参数位置和数量的限制）
# 注意：tuple（元组）是有序的，所以 args 中元素的顺序受到赋值时的影响；
#
# (**args)
# 把参数以字典（键值对）的形式传入，字典是无序的，在调用时只要对应合适的形参名就可以。
# 输出时并不一定按照提供参数的顺序。
#
# 多种参数传递方式混合使用（不建议）
# 定义函数形参的顺序：无默认值的形参(arg) 》有默认值的形参(arg=) 》元组参数(*args) 》字典参数(**args)
# 调用参数顺序：指定参数名称的参数要在无指定参数名称的参数之后；不可以重复传递。
# 函数被调用时，参数的传递过程为：
# 1.按顺序把无指定参数的实参赋值给形参；
# 2.把指定参数名称(arg=v)的实参赋值给对应的形参；
# 3.将多余的无指定参数的实参打包成一个 tuple 传递给元组参数(*args)；
# 4.将多余的指定参数名的实参打包成一个 dict 传递给字典参数(**args);
