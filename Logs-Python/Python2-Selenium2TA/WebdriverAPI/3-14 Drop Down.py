# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import time
__author__ = 'Anliven'

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('Sample__DropDown.html')
driver.get(file_path)
time.sleep(3)

m = driver.find_element_by_id("ShippingMethod")  # 先定位到下拉框
m.find_element_by_xpath("//option[@value='10.69']").click()  # 再点击下拉框下的选项
time.sleep(3)
driver.quit()

# 对于一般的下拉框，可通过二次定位来完成；首先定位到下拉框，然后定位下拉框中的内容
# 在实际的 web 测试时，会发现各种类型下拉框，
# 对于需要两次点击的下拉框，第一次点击弹出下拉框，第二次点击操作元素
# 对于鼠标移动到元素直接显示的下拉框，可以使用 move_to_element()进行操作