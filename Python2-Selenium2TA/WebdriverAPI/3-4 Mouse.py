# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 引入 ActionChains 类
import time
__author__ = 'Anliven'

print "鼠标事件"

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

# print "鼠标右击操作"
# # context_click() 右键点击一个元素
# right = driver.find_element_by_class_name("cp-feedback")  # 定位到要右击的元素
# ActionChains(driver).context_click(right).perform()  # 对定位到的元素执行鼠标右键操作
# time.sleep(5)
# # ActionChains(driver) 表明是对wedriver的实例driver生成用户的行为
# # perform() 执行所有 ActionChains 中存储的行为；通常与ActionChains（）配合使用
#
# print "鼠标移动到元素上"
# # move_to_element() 模拟鼠标移动到一个元素上
# above = driver.find_element_by_name("tj_trhao123")  # 定位到鼠标移动到上面的元素
# ActionChains(driver).move_to_element(above).perform()  # 对定位到的元素执行鼠标移动到上面的操作
# time.sleep(5)
#
# print "按下鼠标左键"
# # click_and_hold（） 按住鼠标左键在一个元素
# left = driver.find_element_by_xpath(".//*[@id='lh']/a[4]")
# ActionChains(driver).click_and_hold(left).perform()
# ActionChains(driver).click_and_hold(left).release()
# time.sleep(5)

print "鼠标双击操作"
# double_click() 双击页面元素
double = driver.find_element_by_xpath(".//*[@id='u1']/a[4]")
ActionChains(driver).double_click(double).perform()
time.sleep(15)

# print "鼠标拖放操作"
# # drag_and_drop(source, target) 在源元素source上按下鼠标左键，然后移动到目标元素target上释放。
# # 需要先定义源元素source和目标元素target
# element = driver.find_element_by_xpath(".//*[@id='lh']/a[3]")  # 定位元素的原位置
# target = driver.find_element_by_xpath(".//*[@id='kw']")  # 定位元素要移动到的目标位置
# ActionChains(driver).drag_and_drop(element, target).perform()  # 执行元素的移动操作
# time.sleep(15)

driver.quit()

# ActionChains 类鼠标操作的常用方法：
#  context_click() 右击
#  double_click() 双击
#  drag_and_drop() 拖动
#  move_to_element() 鼠标悬停在一个元素上
#  click_and_hold() 按下鼠标左键在一个元素上