# -*- coding: utf-8 -*-
from selenium import webdriver
__author__ = 'Anliven'

print "设置浏览器宽和高"
driver = webdriver.Firefox()
driver.get("http://m.mail.10086.cn")
print "设置浏览器宽480、高800显示"
driver.set_window_size(480, 800)  # 参数数字为像素点，用来设置浏览器的宽和高
driver.quit()
