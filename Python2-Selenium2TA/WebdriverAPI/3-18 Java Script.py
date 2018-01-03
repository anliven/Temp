# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
__author__ = 'Anliven'

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('Sample__JavaScript.html')
driver.get(file_path)

driver.execute_script('xxx')  # 隐藏文字信息   ???
time.sleep(5)

button = driver.find_element_by_class_name('btn')
driver.execute_script('xxx', button)  # 隐藏按钮   ???
time.sleep(5)

driver.quit()

# execute_script(script, *args) 在当前窗口/框架 同步执行 javaScript
# 参数 script --- JavaScript 的执行
# 参数 *args --- 适用任何 JavaScript 脚本