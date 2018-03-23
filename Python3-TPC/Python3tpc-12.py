#! python3
# -*- coding: utf-8 -*-

import os

data = open("Python3tpc-12.gfx", "rb").read()  # 下载文件并重命名：http://www.pythonchallenge.com/pc/return/evil2.gfx
for i in range(5):
    pic = 'Python3tpc-12-%d.jpg' % i
    f = open(pic, 'wb')
    f.write(data[i::5])
    f.close()
    os.remove(pic)  # 清除生成的文件

# 根据提示获得线索信息
# Link: http://www.pythonchallenge.com/pc/return/evil.html
# Next: http://www.pythonchallenge.com/pc/return/disproportional.html
#
# Points：
# - 文件处理及序列切片
