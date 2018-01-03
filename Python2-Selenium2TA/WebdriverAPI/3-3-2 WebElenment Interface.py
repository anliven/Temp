# -*- coding: utf-8 -*-
from selenium import webdriver
__author__ = 'Anliven'

print "WebElenment接口常用方法"
# WebElement 接口的其它更多方法请参考 webdriver API

browser = webdriver.Firefox()  # 实例化一个webdriver 的 Firefox 对象
browser.get("https://www.baidu.com")  # 获得浏览器对象后，通过 get()方法，可以向浏览器发送网址

size = browser.find_element_by_id("kw").size  # 返回百度页面输入框的宽高
print size

text = browser.find_element_by_id("cp").text  # #返回百度页面底部备案信息
print text

attribute = browser.find_element_by_id("kw").get_attribute('type')
# get_attribute(name) 获得属性值
# 返回元素的属性值，可以是 id、name、type 或元素拥有的其它任意属性
# 此方法在定位一组时将变得非常有用
print attribute

result = browser.find_element_by_id("kw").is_displayed()  # 返回元素的结果是否可见，返回结果为 True 或 False
print result

browser.quit()

# WebElement接口常用方法:
# clear ----- 清除元素的内容
# send_keys ----- 在元素上模拟按键输入
# click ----- 单击元素
# submit ----- 提交表单
# size ----- 返回元素的尺寸
# text ----- 获取元素的文本
# get_attribute(name) ----- 获得属性值
# is_displayed() ----- 设置该元素是否用户可见
