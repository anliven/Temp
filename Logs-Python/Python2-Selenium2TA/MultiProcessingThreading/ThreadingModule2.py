# -*- coding: utf-8 -*-
import threading
from time import sleep, ctime
__author__ = 'Anliven'

loops = [4, 2]


class ThreadFunc(object):
    def __init__(self, func, args, name=''):  # __init__()方法在类的一个对象被建立时运行,用来初始化对象
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func, self.args)
        # apply() 函数用于当函数参数已经存在于一个元组或字典中时， 间接地调用函数 !!!???


def loop(nloop, nsec):
    print "start loop", nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()


def main():
    print 'all begin at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:  # 调用 ThreadFunc 实例化的对象，创建所有线程
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:  # 开始线程
        threads[i].start()

    for i in nloops:  # 等待所有结束线程
        threads[i].join()

    print 'all end at:', ctime()

if __name__ == '__main__':
    main()
