# -*- coding: utf-8 -*-
import os
__author__ = 'Anliven'

result_dir = 'D:\\Anliven-Running\\Zen\\PycharmProjects\\Selenium2Python2TA'
lists = os.listdir(result_dir)
print "原始文件列表信息：%s" % lists

# 获取根据文件创建时间进行排序的文件列表
lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0)
print "以创建时间排序的文件列表信息：%s" % lists
print ('最新的文件为：'+lists[-1])  # lists[-1] 在这里表示取文件列表中的最大值，也就是最新被创建的文件

files = os.path.join(result_dir, lists[-1])
print "最新文件的完整路径：%s" % files

# os.listdir() 用于获取目录下的所有文件列表
# 列表的sort()方法对原列表进行排序，用于改变列表中元素的位置

# os.path.getmtime() 返回文件列表中最新文件的时间
# os.path.isdir() 判断某一路径是否为目录
# os.path.join()  用来连接字符串，通过路径与文件名的拼接，得到文件的完整路径

# lambda !!!???
# key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0
