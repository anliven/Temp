# -*- coding: utf-8 -*-
from selenium import webdriver
import time
__author__ = 'Anliven'

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")
cookie = driver.get_cookies()  # 获得 cookie 信息
print cookie  # 将获得 cookie 的信息打印

# 向 cookie 的 name 和 value 添加会话信息。
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbb'})
# 遍历 cookies 中的 name 和 value 信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])

driver.delete_cookie("CookieName")  # 删除一个特定的 cookie
driver.delete_all_cookies()  # 删除所有 cookie
time.sleep(2)

driver.quit()

# webdriver 可以读取、添加和删除 cookie 信息：
# get_cookies() --- 获得所有 cookie 信息
# get_cookie(name) --- 返回特定 name 有 cookie 信息
# add_cookie(cookie_dict) --- 添加 cookie，必须有 name 和 value 值
# delete_cookie(name) --- 删除特定(部分)的 cookie 信息
# delete_all_cookies() --- 删除所有 cookie 信息
