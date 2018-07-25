# -*- coding: utf-8 -*-
from selenium import webdriver
import time
__author__ = 'Anliven'

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
# 点击登录链接
driver.find_element_by_xpath(".//*[@id='u1']/a[7]").click()
# 通过二次定位找到用户名输入框
div = driver.find_element_by_class_name("tang-content").find_element_by_name("userName")
# 第一次定位找到弹出的登录框，在登录框上再次进行定位找到了用户名输入框。
div.send_keys("nsn_ask")
# 输入登录密码
driver.find_element_by_name("password").send_keys("nsn_ask2011")
# 点击登录
driver.find_element_by_id("TANGRAM__PSP_8__submit").click()

time.sleep(15)
driver.quit()
