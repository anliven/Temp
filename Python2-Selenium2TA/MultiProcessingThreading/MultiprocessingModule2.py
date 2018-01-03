# -*- coding: utf-8 -*-
from multiprocessing import Process
import os
__author__ = 'Anliven'


def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # 用于判断系统是否包含 getppid
        print 'parent process:', os.getppid()
    print 'info process id:', os.getpid()
    # getpid()  得到本身进程id
    # getppid()  得到父进程进程id，如果已经是父进程，得到系统进程id


def f(name):
    info('Get process ID test-2')
    print 'hello', name
    print 'f process id:', os.getpid()

if __name__ == '__main__':
    info('Get process ID test-1')

    print "\n"
    p = Process(target=f, args=('bob',))
    print p.pid  # Process.PID 中保存有 PID，如果进程还没有 start()，则 PID 为 None
    p.start()
    print p.pid
    p.join()


# multiprocessing 提供了 threading 包中没有的 IPC(比如 Pipe 和 Queue)，效率上更高。
# 应优先考虑 Pipe 和 Queue，避免使用 Lock/Event/Semaphore/Condition 等同步方式 (因为它们占据的不是用户进程的资源)

# !!!???
# multiprocessing 包中有 Pipe 类和 Queue 类来分别支持Pipe 和 Queue这两种 IPC（Internet Process Connection）机制
# Pipe 和 Queue 可以用来传送常见的对象