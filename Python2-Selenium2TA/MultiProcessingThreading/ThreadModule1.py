# -*- coding: utf-8 -*-
import thread
from time import sleep, ctime
__author__ = 'Anliven'


def loop0():
    print '\n Loop0 begin at:', ctime()
    sleep(4)
    print '\n Loop0 end at:', ctime()


def loop1():
    print '\n Loop1 begin at:', ctime()
    sleep(2)
    print '\n Loop1 end at:', ctime()


def main():
    print 'All loops begin at :', ctime()
    thread.start_new_thread(loop0, ())  # start_new_thread()要求前两个参数必填；所以，对于不定义的参数要传一个空的元组
    thread.start_new_thread(loop1, ())
    sleep(6)
    # 如果没有让主线程停下来，那主线程就会运行下面的语句，然后关闭运行着 loop0()和 loop1()的两个线程并退出
    # 这里设置sleep(6)是为了让主线程等待 6秒，防止主线程过早退出，但这样使用 sleep()函数做线程的同步操作是不可靠的
    print 'All loops end at :', ctime()

if __name__ == '__main__':
    main()


# Python 通过两个标准库 thread 和 threading 提供对线程的支持
# thread 提供了低级别的、原始的线程以及一个简单的锁。避免使用 thread 模块，它不支持守护线程；
# threading 基于 Java 的线程模型设计

# 锁（Lock）和条件变量（Condition）在 Python 中则是独立的对象
# 而在 Java 中是对象的基本行为（每一个对象都自带了锁和条件变量）
