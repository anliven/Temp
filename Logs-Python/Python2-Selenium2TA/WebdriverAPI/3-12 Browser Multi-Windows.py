# -*- coding: utf-8 -*-
from selenium import webdriver
import time
__author__ = 'Anliven'

# 本脚本运行之前需要设置浏览器为“在新窗口打开网页”
driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/")  # 打开博客园网站
driver.find_element_by_xpath(".//*[@id='side_nav']/div[3]/ul/li[1]/a").click()  # 打开"反馈与建议"新窗口
nowhandle = driver.current_window_handle  # 获得当前窗口
allhandles = driver.window_handles  # 获得所有窗口

# 循环判断窗口是否为当前窗口
for handle in allhandles:
    if handle != nowhandle:
        driver.switch_to.window(handle)

driver.find_element_by_xpath(".//*[@id='footer']/a[2]").click()  # 在新窗口中点击“联系我们”
time.sleep(3)
driver.close()  # close()用于关闭窗口

driver.switch_to.window(nowhandle)  # 回到原窗口
driver.find_element_by_xpath(".//*[@id='footer_bottom']/div[1]/a[2]").click()  # 在原窗口中点击“联系我们”
time.sleep(3)
driver.quit()  # quit()用于退出驱动程序并关闭所有相关窗口

# webdriver 提供了相关方法可在多个窗口之间切换并操作不同窗口上的元素
# 获得每一个窗口的唯一标识符号（句柄），通过获得的句柄来区别分不同的窗口，从而对不同窗口上的元素进行操作

# current_window_handle --- 获得当前窗口句柄
# window_handles --- 返回的所有窗口的句柄到当前会话
# switch_to_window() --- 用于处理多窗口之前切换
# switch_to_frame() --- 用于处理多框架的切换
# close() --- 用于关闭当前窗口，
# quit() --- 用于退出驱动程序并关闭所有相关窗口
