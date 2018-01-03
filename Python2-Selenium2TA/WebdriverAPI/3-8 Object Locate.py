# -*- coding: utf-8 -*-
from selenium import webdriver
import os  # 标准库中的 os 模块包含普遍的操作系统功能,主要用于操作本地目录文件
import time
__author__ = 'Anliven'


driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('Sample__CheckBox.html')  # path.abspath()方法用于获取当前路径下的文件
driver.get(file_path)

# 选择页面上所有的 tag name 为 input 的元素
inputs = driver.find_elements_by_tag_name('input')

# 过滤出 tpye 为 checkbox 的元素，单击勾选
for x in inputs:
    if x.get_attribute('type') == 'checkbox':
        x.click()
time.sleep(5)
# 取消勾选
for x in inputs:
    if x.get_attribute('type') == 'checkbox':
        x.click()
time.sleep(5)

# 通过 css 方式选择所有的 type 为 checkbox 的元素并单击勾选
checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
time.sleep(5)
# 通过 css 方式打印当前页面上 type 为 checkbox 的个数
print len(driver.find_elements_by_css_selector('input[type=checkbox]'))  # len()返回一个对象的长度（或个数）
# 通过 css 方式把页面上最后1个 checkbox 的勾给去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
# pop()用于删除指定们位置的元素，pop()为空默认选择最一个元素
time.sleep(5)

driver.quit()


# 定位一组对象一般用于以下场景：
# 批量操作对象，比如将页面上所有的 checkbox 都勾上
# 先获取一组对象，再在这组对象中过滤出需要具体定位的一些对象。比如定位出页面上所有的checkbox，然后选择最后一个
