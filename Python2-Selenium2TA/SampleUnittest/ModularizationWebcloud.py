# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import ModularizationLogin  # 导入自定义的模块文件
__author__ = 'Anliven'

driver = webdriver.Firefox()
driver.implicitly_wait(30)
base_url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"

driver.get(base_url)
ModularizationLogin.login(driver)  # 调用自定义模块的方法
time.sleep(5)

driver.quit()

# 模块化: 一方面不用写重复代码，另一方面可以使测试用例更关注具体的用例代码
