# -*- coding: utf-8 -*-
import urllib2
import cookielib
__author__ = 'Anliven'

# 从文件中获取Cookie并访问

readcookie = cookielib.MozillaCookieJar()  # 创建MozillaCookieJar实例对象
readcookie.load('Spider_cookielib_2.txt', ignore_discard=True, ignore_expires=True)  # 从文件中读取cookie内容到变量

req = urllib2.Request("http://www.cn.bing.com")  # 创建请求的request
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(readcookie))  # 利用urllib2的build_opener方法创建一个opener
response = opener.open(req)
print response.read()


# 设想cookie文件中保存的是登录的cookie，那么提取出这个cookie文件内容，就可以用以上方法模拟这个人的账号登录
# 创建一个带有cookie的opener，在访问登录的URL时，将登录后的cookie保存下来，然后利用这个cookie来访问其他网址