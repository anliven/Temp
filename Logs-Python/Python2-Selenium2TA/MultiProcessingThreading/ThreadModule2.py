# -*- coding: utf-8 -*-
import thread
from time import sleep, ctime
__author__ = 'Anliven'

loops = [4, 2]


def loop(nloop, nsec, lock):
    print 'Loop', nloop, 'begin at :', ctime()
    sleep(nsec)
    print 'Loop', nloop, 'end at :', ctime()
    lock.release()  # 解锁；在线程结束的时候，线程自己去做解锁操作


def main():
    print 'All loops begin at :', ctime()
    locks = []
    nloops = range(len(loops))  # 以 loops 数组创建列表，并赋值给 nloops

    for i in nloops:
        lock = thread.allocate_lock()  # 返回一个新的锁定对象
        lock.acquire()  # 锁定
        locks.append(lock)  # 追加到追加到 locks[]数组中
        # 先调用thread.allocate_lock()函数创建一个锁的列表
        # 然后分别调用各个锁的acquire()函数获得锁
        # 然后把锁放到锁列表locks中

    for i in nloops:  # 执行多线程
        thread.start_new_thread(loop, (i, loops[i], locks[i]))
        # 循环创建线程，每个线程都用各自的循环号，睡眠时间和锁为参数；去调用 loop()函数

    for i in nloops:
        while locks[i].locked():  # 当线程为锁定锁定状态时，一直运行；知道线程解锁
            pass
    # 此循环的作用：等待两个锁都被解锁为止才继续运行下一条语句（达到暂停主线程的目的）

    print 'All loops end at :', ctime()

if __name__ == '__main__':
    main()
