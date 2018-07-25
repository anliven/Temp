# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest  # 引入 unittest 框架包
import time
import HTMLTestRunner  # 引入 HTMLTestRunner 包
from TestReport import AllTestCasesList  # 引入包含测试用例的所有测试文件，TesstReport是文件夹名称
import sys
sys.path.append("D:\Anliven-Running\Zen\PycharmProjects\Selenium2Python2TA\TestReport")
# 将 TestReport 目录添加到 sys.path，本示例中，这一步是“from TestReport import AllTestCasesList”的前提条件
# 需要在 TestReport 目录下创建一个__init__.py 文件
# 在 TestReport 目录下创建新的测试用例文件，只需要在__init__.py 文件里添加就可以


# Baidu 类继承 unittest.TestCase 类，从 TestCase 类继承是告诉 unittest 模块的方式，这是一个测试案例
class Baidu(unittest.TestCase):
    def setUp(self):  # setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "www.baidu.com"  # 这里将浏览器的调用和 URL 的访问放到初始化部分
        self.verificationErrors = []  # 脚本运行时，错误的信息将被打印到这个列表中
        self.accept_next_alert = True  # 是否继续接受下一个警告

    def test_baidu_1(self):  # 定义了打开和关闭百度页面的测试用例
        u"""测试用例：打开和关闭百度页面selenium"""
        # 为每一个测试用例添加说明，使报告易读
        # 在 python 中是不区分单双引号的，但必须要成对出现；三引号用于表示多行注释，不分单双；
        # 使用 help()查看函数，会显示出函数的注释信息
        # u 是避免中文引起的乱码问题
        driver = self.driver
        driver.get("https://www.baidu.com/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        driver.close()

    def test_baidu_2(self):  # 定义了打开和关闭百度页面的测试用例
        u"""测试用例：打开和关闭百度页面python"""
        driver = self.driver
        driver.get("https://www.baidu.com/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("python")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        driver.close()

    def tearDown(self):  # tearDown 方法在每个测试方法执行后调用，完成所有测试用例执行完成的清理工作，如退出浏览器等
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testunit = unittest.TestSuite()     # 定义一个单元测试容器;
    # 如果使用 unittest.main() 的话默认会执行所有以 test 开头的测试用例

    # 将本示例脚本定义的测试用例加入到测试容器中
    testunit.addTest(Baidu("test_baidu_1"))
    testunit.addTest(Baidu("test_baidu_2"))

    alltestname = AllTestCasesList.alltestcaselist()  # 获取测试用例文件名称数组
    for test in alltestname:  # 循环执行
        testunit.addTest(unittest.makeSuite(test))
        # 将引入的测试文件中包含的测试用例，加入到测试容器(套件)中
        # unittest 的 makeSuite：用于生产 testsuite 对象的实例,把所有的测试用例组装成 TestSuite
        # 可以通过此方法，将包含测试用例的多个测试py文件的测试结果，整合到一个测试报告中

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))      # 获取当前时间
    # 定义个报告存放路径，支持相对路径
    filename = "D:\\Anliven-Running\\Zen\\PycharmProjects\\Selenium2Python2TA\\TestReport_"+now+".html"
    fp = file(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'Anliven的测试报告',
        description=u'用例执行情况：')
    # stream定义报告所写入的文件；
    # title为报告的标题；
    # description为报告的说明与描述；

    runner.run(testunit)      # 运行测试用例


# HTMLTestRunner 是 Python 标准库的 unittest 模块的一个扩展。它生成易于使用的 HTML 测试报告。
# HTMLTestRunner 是在 BSD 许可证下发布
# http://tungwaiyip.info/software/HTMLTestRunner.html
# Windows ：将下载的 HTMLTestRunner.py 文件放入...\Python27\Lib 目录下


# time 模块
# time.time() --- 获取当前时间戳
# time.localtime() --- 当前时间的 struct_time 形式
# time.ctime() --- 当前时间的字符串形式
# time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# __init__.py 文件的作用
# 要弄明白这个问题，首先要知道，python 在执行 import 语句时，到底进行了什么操作？
    # 按照 python 的文档，它执行了如下操作：
    # 第 1 步，创建一个新的，空的 module 对象（它可能包含多个 module） ；
    # 第 2 步，把这个 module 对象插入 sys.module 中
    # 第 3 步，装载 module 的代码（如果需要，首先必须编译）
    # 第 4 步，执行新的 module 中对应的代码。

    # 在执行第 3 步时，首先要找到 module 程序所在的位置，搜索的顺序是：
    # 当前路径 （以及从当前目录指定的 sys.path） ，然后是 PYTHONPATH，然后是 python 的安装设置相关的默认路径。
# python 中的 package 必须包含一个__init__.py 文件，以普通 module 的方式导入，就可以直接访问此 package中的各个 module


# unittest 的  TestLoader 成员discover()方法,可以通过文件的名称来判断是否为测试用例文件