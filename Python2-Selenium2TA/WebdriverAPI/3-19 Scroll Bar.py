# -*- coding: utf-8 -*-
from selenium import webdriver
import time
__author__ = 'Anliven'

# 访问百度
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

# 将页面滚动条拖到底部
jsdown = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(jsdown)  # 借助 JavaScript是来完成操作
time.sleep(3)

# 将滚动条移动到页面的顶部
jsup = "var q=document.documentElement.scrollTop=0"
driver.execute_script(jsup)  # 借助 JavaScript是来完成操作
time.sleep(3)

driver.quit()

# 滚动条并非页面上的元素， 可以借助 JavaScript是来完成操作
# 用于标识滚动条位置的代码
# <body onload= "document.body.scrollTop=0 ">  --- 滚动条在最上方,scrollTop=0
# <body onload= "document.body.scrollTop=100000 "> --- scrollTop=100000 ，滚动条在最下方