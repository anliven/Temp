#! python3
# -*- coding: utf-8 -*-

from PIL import Image
import re

# import requests
# from io import BytesIO
# s = requests.session()
# s.proxies = {'http': '10.144.1.10:8080'}
# img = Image.open(BytesIO(s.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))

img = Image.open("Python3tpc-07.png")  # 下载图片并重命名：http://www.pythonchallenge.com/pc/def/oxygen.png
row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
row = row[::7]
data = [r for r, g, b, a in row if r == g == b]
char = "".join(map(chr, data))
nums = re.findall("\d+", char)

for i in range(0, len(nums)):
    print(chr(int(nums[i])), end="")

# 根据提示获得线索信息
# Link: http://www.pythonchallenge.com/pc/def/oxygen.html
# Next: http://www.pythonchallenge.com/pc/def/integrity.html
#
# Points：
# - 第三方Pillow模块(PIL, Python Imaging Library，用于图像处理)：https://python-pillow.org
# - 三原色光模式(RGB color model，RGB颜色模型）及像素（px, pixel）的定义
