# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # webdriver 的 Keys()类提供键盘上所有按键的操作
import time
__author__ = 'Anliven'

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

# 输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")
time.sleep(3)  # 三秒的休眠时间

# 删除多输入的一个 m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(3)

# 输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
time.sleep(3)

# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
time.sleep(3)

# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(3)

# 输入框重新输入内容，搜索
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
time.sleep(3)

# 通过回车键盘来代替点击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)
time.sleep(3)

driver.quit()


# 常使用到的键盘操作：
# send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
# send_keys(Keys.SPACE) 空格键(Space)
# send_keys(Keys.TAB) 制表键(Tab)
# send_keys(Keys.ESCAPE) 回退键（Esc）
# send_keys(Keys.ENTER) 回车键（Enter）
# send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
# send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
# send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
# send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）

# Keys 类所提供的按键可查阅 webdriver API
# Selenium
# http://www.seleniumhq.org/
# 官方User Guide：　　
# http://seleniumhq.org/docs/
# http://www.seleniumhq.org/docs/03_webdriver.jsp
