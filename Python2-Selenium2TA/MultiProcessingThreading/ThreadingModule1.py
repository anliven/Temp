# -*- coding: utf-8 -*-
import threading
from time import sleep, ctime
__author__ = 'Anliven'

loops = [4, 2]


def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()


def main():
    print 'all begin at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))  # 创建线程
        threads.append(t)

    for i in nloops:
        threads[i].start()  # start() 开始线程活动

    for i in nloops:
        threads[i].join()  # join([time]): 等待至线程中止
        # join()会等到线程结束，或者在给了 timeout 参数的时候，等到超时为止
        # join()可以完全不用调用:一旦线程启动后，就会一直运行，直到线程的函数结束，退出为止

    print 'all end at:', ctime()

if __name__ == '__main__':
    main()


# 避免使用 thread 模块，它不支持守护线程。当主线程退出时，所有的子线程不论它们是否还在工作， 都会被强行退出
# threading模块则支持守护线程