# -*- coding: utf-8 -*-
import urllib2
import cookielib
__author__ = 'Anliven'

# 保存Cookie到文件

filename = 'Spider_cookielib_2.txt'  # 设置保存cookie的文件，同级目录下的Spider_cookielib_2.txt
cookie = cookielib.MozillaCookieJar(filename)  # 声明一个MozillaCookieJar对象实例来保存cookie

handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.cn.bing.com")
print response.read()

cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到文件

# save方法的参数
# ignore_discard的意思是即使cookies将被丢弃也将它保存下来
# ignore_expires的意思是如果在该文件中 cookies已经存在，则覆盖原文件写入


