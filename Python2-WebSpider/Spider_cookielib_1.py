# -*- coding: utf-8 -*-
import urllib2
import cookielib
__author__ = 'Anliven'

# 获取Cookie保存到变量

cookie = cookielib.CookieJar()  # 声明一个CookieJar对象实例来保存cookie
handler = urllib2.HTTPCookieProcessor(cookie)  # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = urllib2.build_opener(handler)  # 通过handler来构建opener
response = opener.open('http://www.cn.bing.com')  # 此处的open方法同urllib2的urlopen方法，也可以传入request

for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value

# Cookie，指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据（通常经过加密）

# cookielib模块的主要作用是提供可存储cookie的对象，以便于与urllib2模块配合使用来访问Internet资源
# 可以利用本模块的CookieJar类的对象来捕获cookie并在后续连接请求时重新发送，比如可以实现模拟登录功能
# 该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar
# 它们的关系：CookieJar —-派生—->FileCookieJar —-派生—–>MozillaCookieJar和LWPCookieJar

# 当获取一个URL使用一个opener
# 需要创建opener来实现对Cookie的设置
# urlopen 其实是默认的opener，可以理解成opener的一个特殊实例，传入的参数仅仅是url，data，timeout