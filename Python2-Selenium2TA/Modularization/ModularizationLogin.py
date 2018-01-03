# -*- coding: utf-8 -*-
import userinfo  # 导入包含用户名和密码的自定义模块
__author__ = 'Anliven'

us, pw = userinfo.fun()  # 通过两个变量，来接收调用函数获得用户名&密码
print us, pw  # 打印两个变量

info = userinfo.zidian()  # 获取字典数据
# 通过 items()循环读取元组（键/值对）
for us, pw in info.items():
    print "username is %s : password is %s " % (us, pw)


def login(self):
    self.maximize_window()
    self.find_element_by_id("username").clear()  # clear() 用于清除输入框的默认内容
    self.find_element_by_id("username").send_keys(us)
    # send_keys("xx") 用于在一个输入框里输入 xx 内容
    # 输入中文时,需要在脚本开头声明编码为 utf-8， 然后send_keys(u"中文内容"),表示转成 python Unicode 编码
    self.find_element_by_id("password").clear()  #
    self.find_element_by_id("password").send_keys(pw)
    self.find_element_by_class_name("logging").click()
    # click() 方法用于单击任何可以点击的元素，文字/图片连接，按钮，下拉按钮等
