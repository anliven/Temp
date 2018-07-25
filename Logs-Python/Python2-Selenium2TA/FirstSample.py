# -*- coding: utf-8 -*-
from selenium import webdriver  # 导入 selenium 的 webdriver 包后才能使用 webdriver API 进行自动化脚本的开发
import time
__author__ = 'Anliven'

browser = webdriver.Firefox()  # 实例化一个webdriver 的 Firefox 对象
browser.get("https://www.baidu.com")  # 获得浏览器对象后，通过 get()方法，可以向浏览器发送网址


browser.find_element_by_id("kw").send_keys("selenium")
# 通过 id=kw 定位到百度的输入框，并通过键盘方法send_keys()向输入框里输入 selenium
browser.find_element_by_id("su").click()  # 通过 id=su 定位的搜索按钮，并向按钮发送单击事件（ click() ）
time.sleep(3)
browser.get_screenshot_as_file("D:\\Anliven-Running\\Zen\\PycharmProjects\\Selenium2Python2TA\\FirstSampleShot.png")
# get_screenshot_as_file()函数截图当前页面并保存到指定的路径下面

browser.quit()  # 通过quit()方法退出并关闭窗口的每一个相关的驱动程序


# webdriver 原理：
# 1- WebDriver 启动目标浏览器，并绑定到指定端口。启动的浏览器实例，做为 web driver 的 remote server。
# 2- Client 端通过 CommandExcuter 发送 HTTPRequest 给 remote server 的侦听端口（通信协议： the webriver wire protocol）
# 3- Remote server 需要依赖原生的浏览器组件（如：IEDriverServer.exe等）来转化浏览器的 native 调用。


# 比较全面的掌握如何使用 webdriver 所提供的方法对页面上各种元素进行操作
# 在实际的web自动化测试过程中，可以从以下方面进行提高：
# 1、熟练掌握 xpath\CSS 定位的使用，这样在遇到各种难以定位的属性时才不会变得束手无策。
# 2、准备一份 python 版本的 webdriver API ，遇到不理解地方，及时查到 API 的使用
# 3、学习掌握 JavaScript 语言，可以让web自动化测试工作更加游刃有余。
# 4、web自动化测试归根结底是与前端打交道，多多熟悉前端技术，如 http 请求，HTML 语言 ，cookie/session 机制等。
