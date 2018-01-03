# -*- coding: utf-8 -*-
from multiprocessing import Process


def f(name):
    print 'hello', name

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))  # 利用 multiprocessing.Process 对象来创建一个进程
    p.start()  # Process 对象与Thread 对象的用法相同，也有 start(), run(), join()的方法
    p.join()

# 由于全局解释锁(Global Interceptor Lock)的存在，在 CPU 密集型的程序当中，使用多线程并不能有效地利用多核 CPU 的优势
# 因为一个解释器在同一时刻只会有一个线程在执行
# multiprocessing 模块提供了本地和远程的并发性，通过全局解释锁(Global Interceptor Lock, GIL)来使用进程(而不是线程)
# multiprocessing 模块可以充分的利用硬件的多处理器来进行工作

# multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})
    # target 表示调用对象，
    # args 表示调用对象的位置参数元组
    # kwargs 表示调用对象的字典
    # Name 为别名
    # Group 实质上不使用

# 在一个 multiprocessing 库的典型使用场景下，所有的子进程都是由一个父进程启动起来的，这个父进程称为 master 进程
# 这个父进程非常重要，它会管理一系列的对象状态
# 一旦这个进程退出，子进程很可能会处于一个很不稳定的状态，因为它们共享的状态也许已经被损坏掉了
# 因此，这个进程最好尽可能做最少的事情，以便保持其稳定性

# 在*nix 上面创建的新的进程使用的是 fork() 函数
# fork()函数通过系统调用创建一个与原来进程几乎完全相同的进程，也可以设定初始参数和传入的变量