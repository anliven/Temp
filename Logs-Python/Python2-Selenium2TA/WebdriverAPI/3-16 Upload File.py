# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import time
__author__ = 'Anliven'

driver = webdriver.Firefox()

# 打开上传文件页面
file_path = 'file:///' + os.path.abspath('Sample__UploadFile.html')
driver.get(file_path)

# 定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('D:\Anliven - Run\Study - Logging\PycharmProjects\Selenium2 Python TA\WebdriverAPI\Sample__CheckBox.html')
# send_keys()方法除可以输入内容外，也可以跟一个本地的文件路径。从而达到上传文件的目的

time.sleep(2)
driver.quit()

# webdriver 并没有提供文件上传操作的方法，但可以转变思路来实现文件上传
# 上传过程一般要打开一个系统的 window 窗口，从窗口选择本地文件添加
# 只要定位上传按钮，通 send_keys 添加本地文件路径就可以了。绝对路径和相对路径都可以，关键是上传的文件存在