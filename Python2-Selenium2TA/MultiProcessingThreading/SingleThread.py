# -*- coding: utf-8 -*-
from time import sleep, ctime
__author__ = 'Anliven'


def loop0():
    print 'Loop0 begin at:', ctime()
    sleep(4)
    print 'Loop0 end at:', ctime()


def loop1():
    print 'Loop1 begin at:', ctime()
    sleep(2)
    print 'Loop1 end at:', ctime()


def main():
    print 'All loops begin at :', ctime()
    loop0()
    loop1()
    print 'All loops end at :', ctime()

if __name__ == '__main__':
    main()

# 本示例中，单线程顺序执行了两个循环loop0和loop1。
# 前一个循环结束后，另一个才能开始。总时间是各个循环运行时间之和。


# 什么是进程？
# 计算机程序只不过是磁盘中可执行的，二进制（或其它类型）的数据；
# 它们只有在被读取到内存中，被操作系统调用的时候才开始它们的生命期；
# 进程（有时被称为重量级进程）是程序的一次执行；
# 每个进程都有自己的地址空间，内存，数据栈以及其它记录其运行轨迹的辅助数据；
# 操作系统管理在其上运行的所有进程，并为这些进程公平地分配时间；

# 什么是线程？
# 线程（有时被称为轻量级进程）跟进程有些相似，不同的是，所有的线程运行在同一个进程中，共享相同的运行环境；
# 可以想像成是在主进程或“主线程”中并行运行的“迷你进程”；