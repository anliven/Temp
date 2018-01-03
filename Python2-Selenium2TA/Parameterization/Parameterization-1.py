# -*- coding: utf-8 -*-
from selenium import webdriver
import time
__author__ = 'Anliven'

source = open("D:\\Anliven-Running\\Zen\\PycharmProjects\\Selenium2Python2TA\\Parameterization\\txt__date.txt", "r")
# open 方法以只读方式（r）打开本地的 txt 文件
values = source.readlines()  # readlines 方法是逐行的读取文件内容
print values
source.close()

for search in values:
    browser = webdriver.Firefox()
    browser.get("https://www.baidu.com")
    browser.find_element_by_id("kw").send_keys(search)
    browser.find_element_by_id("su").click()
    time.sleep(3)
    browser.quit()

# python读取文件的方式有：整个文件读取、逐行读取、固定字节读取
