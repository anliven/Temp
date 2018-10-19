# -*- coding: utf-8 -*-
__author__ = 'Anliven'

aaa = 111
bbb = 333
ccc = 222

if bbb > aaa:
    print ("bbb is greater than aaa.")

if bbb > aaa:
    print ("bbb is greater than aaa.")
else:
    print ("bbb is not greater than aaa")

if bbb > aaa:
    if ccc > bbb:
        print ("aaa < bbb < ccc")
    else:
        if ccc > aaa:
            print ("aaa < ccc <= bbb")
    exit(0)  # sys.exit()可以执行中断，而其中的数字参数用来表示中断的退出代码
elif bbb < aaa:
    print ("bbb is less than aaa.")
elif bbb == aaa:
    print ("bbb is equal to aaa.")
else:
    print ("Unknown")

# if语句用于控制程序的执行
#
# if 判断条件1:
#     执行语句1……
# elif 判断条件2:
#     执行语句2……
# elif 判断条件3:
#     执行语句3……
# else:
#     执行语句4……
#
# "判断条件"成立时运行执行语句，否则就跳过;执行语句的内容可以多行，以缩进来区分表示同一范围;
# 可以有多个elif语句来判断条件
# if语句的嵌套(nested) 建议不要超过2层，尽量保持只有1层；
# 布尔测试（判断条件）应该简洁，可以将复杂的运算事先放到一个变量，然后在判断条件中引用这个变量；
