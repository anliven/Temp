# -*- coding: utf-8 -*-
import re  # re模块提供正则表达式功能
import urllib  # Urllib 模块提供了读取web页面数据的接口，可以读取www和ftp上的数据
__author__ = 'Anliven'


# 创建getHtml()函数，用于获取页面信息
def gethtml(url):
    page = urllib.urlopen(url)  # urllib.urlopen()方法用于打开一个URL地址
    html = page.read()  # read()方法用于读取URL上的数据，向getHtml()函数传递一个网址，并把整个页面下载下来
    return html  # 整个网页打印输出


# 创建getImg()函数，用于在获取的整个页面中筛选需要的图片连接
def getimg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)  # re.compile() 可以把正则表达式编译成一个正则表达式对象
    imglist = re.findall(imgre, html)  # re.findall() 方法读取html 中包含 imgre（正则表达式）的数据
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)  # urllib.urlretrieve()方法，直接将远程数据下载到本地
        x += 1
    return imglist
# 通过一个for循环对获取的图片连接进行遍历，为了使图片的文件名看上去更规范，对其进行重命名，命名规则通过x变量加1。
# 保存的位置默认为程序的存放目录。

html = gethtml("http://tieba.baidu.com/p/2460150866")
# print html
print getimg(html)
print len(getimg(html))
