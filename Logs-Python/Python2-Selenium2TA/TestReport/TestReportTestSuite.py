# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest  # 引入 unittest 框架包
from selenium.common.exceptions import NoAlertPresentException
import time


# YouDao 类继承 unittest.TestCase 类，从 TestCase 类继承是告诉 unittest 模块的方式，这是一个测试案例
class Youdao(unittest.TestCase):
    def setUp(self):  # setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.youdao.com"  # 这里将浏览器的调用和 URL 的访问放到初始化部分
        self.verificationErrors = []  # 脚本运行时，错误的信息将被打印到这个列表中
        self.accept_next_alert = True  # 是否继续接受下一个警告

    def test_youdao_1(self):  # 定义了打开和关闭百度页面的测试用例
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys("an")
        driver.find_element_by_xpath(".//*[@id='form']/button").click()
        time.sleep(3)
        driver.close()

    def test_youdao_2(self):  # 定义了百度搜索设置的测试用例
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys("liven")
        driver.find_element_by_xpath(".//*[@id='form']/button").click()
        time.sleep(3)
        driver.close()

    # 对弹窗异常的处理
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):  # tearDown 方法在每个测试方法执行后调用，完成所有测试用例执行完成的清理工作，如退出浏览器等
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    # 如果使用 unittest.main() 的话默认会执行所有以 test 开头的测试用例