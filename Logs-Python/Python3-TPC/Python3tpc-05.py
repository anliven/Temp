#! python3
# -*- coding: utf-8 -*-

from urllib import request
import pickle

# Solution - 1
proxy_handler = request.ProxyHandler({'http': 'http://10.144.1.10:8080/'})
opener = request.build_opener(proxy_handler)
page = opener.open("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(page)
print(data)
for line in data:
    print("".join([k * v for k, v in line]))

# Solution - 2
file = open('Python3tpc-05.source', 'rb')  # 下载文件并重命名：http://www.pythonchallenge.com/pc/def/banner.p
unPickled = pickle.load(file)
print(unPickled)
for lst in unPickled:
    line = ""
    for char, digit in lst:
        line += char * digit
    print(line)

# 根据提示获得线索信息
# Link: http://www.pythonchallenge.com/pc/def/peak.html
# Next: http://www.pythonchallenge.com/pc/def/channel.html
#
# Points：
# - 标准库urllib模块：https://docs.python.org/3/library/urllib.html
# - 标准库pickle模块：https://docs.python.org/3/library/pickle.html
