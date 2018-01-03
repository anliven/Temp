# -*- coding: utf-8 -*-
from selenium import webdriver
import time
__author__ = 'Anliven'

print "登录实例"
driver = webdriver.Firefox()
driver.get("https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn")
driver.find_element_by_id("username").clear()  # clear() 用于清除输入框的默认内容
driver.find_element_by_id("username").send_keys("xxx@yeah.net")
# send_keys("xx") 用于在一个输入框里输入 xx 内容
# 输入中文时,需要在脚本开头声明编码为 utf-8， 然后send_keys(u"中文内容"),表示转成 python Unicode 编码
driver.find_element_by_id("password").clear()  #
driver.find_element_by_id("password").send_keys("xxx")
driver.find_element_by_class_name("logging").click()
# click() 方法用于单击任何可以点击的元素，文字/图片连接，按钮，下拉按钮等

cookie = driver.get_cookies()  # 获得 cookie 信息
print cookie  # 将获得 cookie 的信息打印

# 退出
driver.find_element_by_class_name("icon-signout").click()
time.sleep(2)

# driver.find_element_by_class_name("logging").submit()  # submit() 提交表单
# 在本脚本中click()和submit()都可以正常使用。
# submit()要求提交对象是一个表单，更强调对信息的提交。
# click()更强调事件的独立性。 （比如，一个文字链接就不能用 submit()方法。 ）

time.sleep(15)  # 脚本休息15秒
driver.quit()
