# -*- coding: utf-8 -*-

__author__ = 'Anliven'


# alert = driver.switch_to.alert()  # 获取网页上的警告信息
# alert.accept()  # 接收警告信息
# print alert.text()  # 信息打印

# #取消对话框（如果有的话）
# alert = driver.switch_to.alert()
# alert.dismiss()

# #输入值（如果有的话）
# alert = driver.switch_to.alert()
# alert.send_keys(“xxx”)


# JavaScript 所生成的 alert、confirm 以及 prompt
# switch_to.alert() --- 定位到 alert/confirm/prompt
# 然后使用 text/accept/dismiss/send_keys 按需进行操作text 返回 alert/confirm/prompt 中的文字信息
# accept() --- 点击确认按钮
# dismiss() --- 点击取消按钮
# send_keys() --- 输入值