# -*- coding: utf-8 -*-
import time
__author__ = 'Anliven'

# 定时执行 #
k = 1
while k < 2:
    timing = time.strftime('%H_%M_%S', time.localtime(time.time()))
    if timing == '12_00_00':
        print u"开始运行脚本:"
        print "This is a sample for Timer Task! The time is %s ！" % timing  # 定义执行命令
        print u"运行完成退出"
        break
    else:
        time.sleep(5)
        print timing
