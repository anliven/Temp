# -*- coding: utf-8 -*-
import os
from selenium import webdriver
import requests
__author__ = 'Anliven'

proxies = {"http": "http://10.144.1.10:8080",  "https": "http://10.144.1.10:8080"}  # 代理设置
r = requests.get("https://www.python.org", proxies=proxies)
# 向 https://www.python.org发送一个GET请求，将请求和响应相关均封装在 r 对象
print r.status_code  # 返回码
print r.headers['content-type']  # 返回头部信息
print requests.get('http://www.python.org', proxies=proxies).headers['content-type']  # 返回头部信息

# 使用 requests 模块来查找内容类型。
# Requests 是一个 Python 的 HTTP 客户端库，默认下载的 python 环境包不包含这个类库，需要另外安装
# Content-Type ，内容类型，一般是指网页中存在的 Content-Type
# 用于定义网络文件的类型和网页的编码，决定浏览器将以什么形式、什么编码读取这个文件

fp = webdriver.FirefoxProfile()
# 定制Firefox的属性
fp.set_preference("browser.download.folderList", 2)  # 下载位置：0是桌面；1是“我的下载”；2是自定义
fp.set_preference("browser.download.manager.showWhenStarting", False)  # 显示下载管理器：默认true为显示，false为不显示
fp.set_preference("browser.download.dir", os.getcwd())  # 设置为当前目录
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")  # 下载文件格式

browser = webdriver.Firefox(firefox_profile=fp)
browser.get("http://pypi.python.org/pypi/selenium")
browser.find_element_by_xpath(".//*[@id='content']/div[3]/table/tbody/tr[3]/td[1]/span/a[1]").click()

browser.quit()

# browser.download.dir --- 用于指定你所下载文件的目录。
# os.getcwd() ---- 该函数不需要传递参数，用于返回当前的目录。
# application/octet-stream 为内容的类型

# 默认情况下，webdriver启动firefox时是启动一个完全新的浏览器
# webdriver可以对Firefox的profile进行定制（在firefox地址栏中输入about:config，可以查看firefox的属性参数）
# 详尽介绍FireFox about:config --- http://www.cnblogs.com/puresoul/p/4252935.html