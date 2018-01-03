# -*- coding: utf-8 -*-
import os
__author__ = 'Anliven'

dirpath = 'D:\\Anliven-Running\\Zen\PycharmProjects\\Selenium2Python2TA\\SampleUnittest'
print dirpath
caselist = os.listdir(dirpath)  # os.listdir()函数获得指定目录中的内容
print caselist
cmdpath = 'D:\\"Anliven-Running"\\"Zen"\\"PycharmProjects"\\"Selenium2Python2TA"\\SampleUnittest'
print cmdpath
# 单独定义cmdpath的原因是：在windows系统cmd执行的的命令，如果路径中出现空格，需要用引号

for scriptname in caselist:
    print scriptname
    s = scriptname.split('.')[1]
    # 选取后缀名为 py 的文件；split()用于字符串分割，这里以文件名的点（.）作为分割
    # 字符串‘testing.py’会被分割成数组['testing','py']
    # 因为数组是从0开始计算的，所以[0]取的是‘testing’,那么[1]取的就是‘py’
    if s == 'py':
        fullpath = r'%s\%s 1>>Unittest-BatchExecution-log.txt 2>&1' % (cmdpath, scriptname)
        print fullpath
        os.system(fullpath)

# 虽然可以在一个.py 文件里编写多个测试用例，然后执行文件里的所有用例，unittest 支持这样的做法
# 但假如将成百上千的用例放置在同一个.py 文件里，显然不合理

# 比较合理的做法是把相关的几条用例放到一个.py 文件里
# 把所有.py 文件放到一个文件夹下，然后通过一个程序执行文件夹下面的所有用例