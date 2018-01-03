# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
__author__ = 'Anliven'

driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com")
sleep(3)

# 获取当前显示分页的数量，并打印
total_pages = len(driver.find_element_by_class_name("pager").find_elements_by_tag_name("a"))
print "total page is %s" % total_pages
sleep(3)

# 循环翻页操作(前10个页面)
page = 1
while page < 10:
    driver.find_element_by_class_name("p_%d" % page).click()
    page += 1
    sleep(3)

sleep(3)
driver.quit()

# find_elements 方法 --- 获取的是一组元素