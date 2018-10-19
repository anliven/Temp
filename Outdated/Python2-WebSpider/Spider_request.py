# -*- coding: utf-8 -*-
import requests
__author__ = 'Anliven'

response = requests.get("http://cn.bing.com")
print response.text
print type(response)
print response.status_code
print response.encoding
print response.cookies
