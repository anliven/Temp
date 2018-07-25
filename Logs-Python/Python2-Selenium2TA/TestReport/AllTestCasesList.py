# -*- coding: utf-8 -*-
from TestReport import *  # 引入包含测试用例的所有测试文件，TesstReport是文件夹名称
import sys
sys.path.append("D:\Anliven-Running\Zen\PycharmProjects\Selenium2Python2TA\TestReport")
# 将 TestReport 目录添加到 sys.path，本示例中，这一步是“from TestReport import *”的前提条件
# 需要在 TestReport 目录下创建一个__init__.py 文件
# 在 TestReport 目录下创建新的测试用例文件，只需要在__init__.py 文件里添加就可以
__author__ = 'Anliven'


def alltestcaselist():
    alltestname = [TestReportTestSuite.Youdao]  # 将测试用例文件名称放入数组
    print "success read all case list!"
    return alltestname
