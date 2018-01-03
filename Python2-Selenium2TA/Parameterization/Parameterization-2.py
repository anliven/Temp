# -*- coding: utf-8 -*-
from selenium import webdriver
import time
__author__ = 'Anliven'

source = open("D:\\Anliven-Running\\Zen\\PycharmProjects\\Selenium2Python2TA\\Parameterization\\txt__username.txt", "r")
# open 方法以只读方式（r）打开本地的用户名 txt 文件
un = source.readlines()  # readlines 方法是逐行的读取文件内容
print un
source.close()

source2 = open("D:\\Anliven-Running\\Zen\\PycharmProjects\\Selenium2Python2TA\\Parameterization\\txt__password.txt", "r")
pw = source2.readlines()
print pw
source2.close()

driver = webdriver.Firefox()
driver.get("https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys(un)
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys(pw)
driver.find_element_by_class_name("logging").click()

time.sleep(3)
driver.quit()

# 分别打开两个 txt 文件，通过 un 和 pw 来接收用户名和密码信息，将接收的数据通过 send_key(xx)转入到执行程序中
# 本示例十分简陋，但是确实达到了数据与脚本分离的目的

# 本示例的缺陷
# 用户名密码分别在不同的文件里，修改用户名和密码比较麻烦
# username和 password文件中只能保存一个用户密码，无能很好的循环读取