# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import time
__author__ = 'Anliven'

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('Sample__GetAttribute.html')
driver.get(file_path)

inputs = driver.find_elements_by_tag_name('input')  # 选择页面上所有的 tag name 为 input 的元素

# 然后循环遍历出 data-node 为594434493的元素，单击勾选
for x in inputs:
    if x.get_attribute('data-node') == '594434493':
        x.click()

time.sleep(3)

driver.quit()


# 获取测试对象的属性能够帮我们更好的进行对象的定位
# 3-8 Object Locate --- 判断一组相同属性的元素，对其进行操作
# 3-21 Get Attribute --- 判断一组属性值不同的元素, 对其进行操作
# 灵活运用这两种不同的方式
