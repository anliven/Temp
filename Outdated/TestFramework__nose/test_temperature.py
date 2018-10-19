# -*- coding: utf-8 -*-
__author__ = 'Anliven'


# 每个Nose测试模块都应该包含以下内容：
#    用于引入Nose及待测模块的语句
#    实际用于测试模块的函数
#    用于触发那些测试函数的调用

# 测试模块test_temperature.py  # 测试文件的名字以“test”开始，Nose运行时，它会自动寻找以“test”开始的文件。
# 代码如下：

import TestFramework__nose  # 引入Nose
from temperature import to_celsius  # 引入待测模块
from temperature import above_freezing  # 引入待测模块

def test_above_freezing ():  # 测试函数的名称也必须以“test”开头。
	print '''Test above_freezing '''
	assert above_freezing(89.4), 'A temperature above freezing'
	assert not above_freezing(-42), 'A temperature below freezing'
	assert not above_freezing(0), 'A temperature at freezing'

def test_boiling ():  # 测试函数的名称也必须以“test”开头。
	print '''Test boiling point'''
	assert to_celsius(212) == 100

def test_roundoff ():  # 测试函数的名称也必须以“test”开头。
	print '''Test that roundoff works'''
	assert to_celsius(100) == 38, 'Returning an unrounded result'   #not 37.77...

if __name__ == "__main__":  # 触发测试函数
	TestFramework__nose.runmodule()
