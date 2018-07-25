# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest  # 引入 unittest 框架包
import time
import re


# Baidu 类继承 unittest.TestCase 类，从 TestCase 类继承是告诉 unittest 模块的方式，这是一个测试案例
class Baidu(unittest.TestCase):
    def setUp(self):  # setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "www.baidu.com"  # 这里将浏览器的调用和 URL 的访问放到初始化部分
        self.verificationErrors = []  # 脚本运行时，错误的信息将被打印到这个列表中
        self.accept_next_alert = True  # 是否继续接受下一个警告

    def test_baidu(self):  # 定义了要执行的测试脚本
        driver = self.driver
        driver.get("https://www.baidu.com/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        driver.close()

# is_element_present 函数用来查找页面元素是否存在
# 在这里用处不大，通常删除，因为判断页面元素是否存在一般都加在 testcase 中
    def is_element_present(self, how, what):
        try:  # try...except....为 python 语言的异常捕捉
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:  # try...except....为 python 语言的异常捕捉
            return False
        return True

# 对弹窗异常的处理
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

# 关闭警告以及对得到文本框的处理
    def close_alert_and_get_its_text(self):
        try:  # try....finally...为 python的异常处理
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:  # try....finally...为 python的异常处理
            self.accept_next_alert = True

# tearDown 方法在每个测试方法执行后调用，完成所有测试用例执行完成的清理工作，如退出浏览器等
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()  # unitest.main()函数用来测试 Baidu 类中以 test 开头的测试用例

# 本示例代码来源于 Selenium IDE 脚本录制与保存，仅添加了注释和修改部分语法格式，未删除无用代码
# 在Windows cmd中执行本示例脚本