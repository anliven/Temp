# -*- coding: utf-8 -*-
__author__ = 'Anliven'


def add(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    print ("ADDING : %d + %d" % (a, b))
    return a + b


def subtract(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    print ("SUBTRACTING : %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    print ("MULTIPLYING : %d * %d" % (a, b))
    return 'Multiply:%d' % (a * b)


def divide(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    print ("DIVIDING : %d / %d" % (a, b))
    return "Divide:%d" % (a / b)


print ("Add:%d, Subtract:%d, %s, %s" % (add(5, 5), subtract(5, 5), multiply(5, 5), divide(5, 5)))


def secret_formula(started):
    """

    :param started:
    :return:
    """
    p1 = started + 333
    p2 = p1 - 222
    p3 = p2 / 111
    return p1, p2, p3


start_point = 999
v1, v2, v3 = secret_formula(start_point)  # secret_formula()返回三个值并分别赋值给三个变量
print ("Value-1:%d, Value-2:%d, Value-3:%d." % (v1, v2, v3))

# print - 打印到屏幕
# return - 返回值；如果函数没有通过return语句返回值，那么打印出来的结果是None


def run_again():
    """

    No params.
    """
    next_step = raw_input("# Select options: again? exit? > ")
    if "again" in next_step:
        run_again()
    elif "exit" in next_step:
        exit(0)  # sys.exit()可以执行中断，而其中的数字参数用来表示中断的退出代码
    else:
        print ("Wrong input.")
        run_again()  # 函数对自身的调用


run_again()

# 函数的返回值
# return是函数的结束语句，函数中任何地方的return语句一旦被执行，这个函数就会结束
# return后面的值作为函数的返回值