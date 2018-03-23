#! python3
# -*- coding: utf-8 -*-

import zipfile
import re

f = zipfile.ZipFile("Python3tpc-06.zip")  # 根据提示下载文件，并重命名（http://www.pythonchallenge.com/pc/def/channel.zip）
print(f.read("readme.txt").decode("utf-8"))

num = '90052'
comments = []
while True:
    content = f.read(num + ".txt").decode("utf-8")
    comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
    match = re.search("Next nothing is (\d+)", content)
    if match is None:
        print(content)
        break
    num = match.group(1)

print("".join(comments))  # 查看页面提示内容（http://www.pythonchallenge.com/pc/def/hockey.html）

# 根据提示获得线索信息
# Link: http://www.pythonchallenge.com/pc/def/channel.html
# Next: http://www.pythonchallenge.com/pc/def/oxygen.html
#
# Points：
# - 标准库zipfile模块：https://docs.python.org/3/library/zipfile.html
# - 标准库re模块：https://docs.python.org/3/library/re.html
