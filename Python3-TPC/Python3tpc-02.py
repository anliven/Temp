#! python3
# -*- coding: utf-8 -*-

import re
import string
from urllib import request

testFile = 'Python3tpc-02.txt'

# Solution - 1
with open(testFile, 'r') as f:
    print("".join(re.findall("[A-Za-z]", f.read())))

# Solution - 2
testStr = ''
with open(testFile, 'r') as f:
    for line in f.readlines():
        for i in line:
            if i in string.ascii_letters:
                testStr += i
print(testStr)

# Solution - 3
with open(testFile, 'r') as f:
    print(list(filter(lambda x: x in string.ascii_letters, f.read())))

# Solution - 4
guts = open(testFile, 'r').read()
d = {}
for i in guts:  # 统计数目
    d[i] = d.get(i, 0) + 1
# print(d)
for key, value in d.items():
    if value == 1:
        print('{}'.format(key), end="")

# Solution - 5
proxy_handler = request.ProxyHandler({'http': 'http://10.144.1.10:8080/'})
opener = request.build_opener(proxy_handler)
page = opener.open("http://www.pythonchallenge.com/pc/def/ocr.html")
# print('Status:', page.status, page.reason)
html = page.read().decode('utf-8')
# print('Data:', html)
data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
print("".join(re.findall("[A-Za-z]", data)))

# 根据提示获得线索信息
# Link: http://www.pythonchallenge.com/pc/def/ocr.html
# Next: http://www.pythonchallenge.com/pc/def/equality.html
#
# Points：
# - 文件处理
# - 标准库string模块：https://docs.python.org/3/library/string.html
# - 标准库re模块（正则表达式）：https://docs.python.org/3/library/re.html
