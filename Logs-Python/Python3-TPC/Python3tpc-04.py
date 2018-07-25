#! python3
# -*- coding: utf-8 -*-

import re
from urllib import request


# Solution - 1
def get_addr(n):
    proxy_handler = request.ProxyHandler({'http': 'http://10.144.1.10:8080/'})
    opener = request.build_opener(proxy_handler)
    page = opener.open(url + str(n))
    html = page.read().decode('utf-8')
    print("html ::", html)
    if n == "16044":
        print("number ::", int(n) / 2)
        return int(n) / 2
    else:
        number = re.search(r'([0-9]+)$', html).group(0)
        print("number ::", number)
        return number


url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
n = 12345
for i in range(1, 400):
    n = get_addr(n)
    print(i, "::", url + str(n))


# Solution - 2
def get_addr2(url):
    proxy_handler = request.ProxyHandler({'http': 'http://10.144.1.10:8080/'})
    opener = request.build_opener(proxy_handler)
    page = opener.open(url)
    html = page.read().decode('utf-8')
    print(html)
    pre_address = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

    try:
        if "Divide" in html:
            number = str(int(re.findall("([0-9]+)", url, re.DOTALL)[0]) / 2)
            address = pre_address + number
        elif "nothing" in html:
            address = pre_address + re.findall("nothing is ([0-9]+)", html, re.DOTALL)[0]
    except UnboundLocalError:
        exit(1)
    finally:
        return address


url2 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
for i in range(1, 400):
    url2 = get_addr2(url2)
    print(i, "::", url2)

# 根据提示获得线索信息
# Link: http://www.pythonchallenge.com/pc/def/linkedlist.php
# Next: http://www.pythonchallenge.com/pc/def/peak.html
#
# Points：
# - 标准库re模块：https://docs.python.org/3/library/re.html
# - 标准库urllib模块：https://docs.python.org/3/library/urllib.html
