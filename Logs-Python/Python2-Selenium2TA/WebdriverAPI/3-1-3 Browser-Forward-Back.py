# -*- coding: utf-8 -*-
from selenium import webdriver
__author__ = 'Anliven'

print "控制浏览器前进和后退"
driver = webdriver.Firefox()

# 访问百度首页
first_url = 'http://www.baidu.com'
print "now access %s" % first_url
driver.get(first_url)

# 访问新闻页面
second_url = 'http://news.baidu.com'
print "now access %s" % second_url
driver.get(second_url)

# 返回（后退）到百度首页
print "back to %s " % first_url
driver.back()  # webdriver 提供了 back()和 forward()方法实现后退、前进浏览网页

# 前进到新闻页
print "forward to %s" % second_url
driver.forward()

driver.quit()

# 格式化字符串
# 在 print 打印字符串中指定变量类型， “%s”表示输出的类型为字符串， “%d”表示输出类型为整型数字
# 如果不确定变量类型的话可以使用“%r”，它的含义是“不管什么都打印出来”