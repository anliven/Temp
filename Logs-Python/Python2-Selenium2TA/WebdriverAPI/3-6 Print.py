# -*- coding: utf-8 -*-
from selenium import webdriver
__author__ = 'Anliven'

# 通过获得页面的 title 、URL 地址，页面上的标识性信息来判断用例执行成功
driver = webdriver.Firefox()
driver.get("https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn")

# 登录
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("xxx@yeah.net")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("xxx")
driver.find_element_by_class_name("logging").click()

# 获得前面 title，打印
title = driver.title  # title 返回当前页面的标题
print title
# 拿当前 URL 与预期 URL 做比较
if title == u"我的CSDN":
    print "title ok!"
else:
    print "title on!"

# 获得当前 URL，打印
now_url = driver.current_url  # current_url 获取当前加载页面的 URL
print now_url

# 拿当前 URL 与预期 URL 做比较
if now_url == "http://my.csdn.net/my/mycsdn":
    print "url ok!"
else:
    print "url on!"

# 获得登录成功的用户，打印
now_user = driver.find_element_by_xpath("html/body/div[6]/div[2]/div[1]/div[1]/div[2]/div[1]/span/a").text  # ??? text
print now_user

driver.quit()
