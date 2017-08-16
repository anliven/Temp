# -*- coding: utf-8 -*-
import urllib2
__author__ = 'Anliven'

request = urllib2.Request("http://www.cn.bing.com")  # Request方法，用来构建请求

try:  # try-except语句来捕获相应的异常
    response = urllib2.urlopen(request)  # 调用urllib2库里面的urlopen方法，传入一个URL请求
except urllib2.HTTPError, e:  # HTTPError的父类是URLError，
    if hasattr(e, "code"):  # hasattr属性,提前对异常的属性进行判断，以免出现属性输出报错的现象
        print e.code  # 如果捕获到了HTTPError，则输出code，不会再处理URLError异常
except urllib2.URLError, e:  # 父类的异常应当写到子类异常的后面，如果子类捕获不到，那么可以捕获父类的异常
    if hasattr(e, "reason"):
        print e.reason  # 如果发生的不是HTTPError，则会去捕获URLError异常，输出错误原因
else:
    print response.read()  # read方法，返回获取到的网页内容


# 也可以写成：response = urllib2.urlopen("http://www.cn.bing.com")
# 但这种写法不太适合构建请求，不推荐。

# 网页信息是由浏览器解释才呈现出来的，实质它是一段HTML代码和JS、CSS
# 如果把网页比作一个人，那么HTML便是他的骨架，JS是肌肉，CSS是衣服

# urlopen(url, data, timeout)
# 参数url即为URL，参数data是访问URL时要传送的数据，timeout是设置超时时间。
# 参数URL是必须要传送的；参数data和timeout可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT
