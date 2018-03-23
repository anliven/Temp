#! python3
# -*- coding: utf-8 -*-

from PIL import Image

# Solution - 1
img = Image.open("Python3tpc-16.gif")  # 下载并重命名：http://www.pythonchallenge.com/pc/return/mozart.gif
# print(img.size)
cols, rows = img.size
PINK = 195  # the pink pixels are color #195

p = list(img.getdata())
for r in range(0, rows * cols, cols):
    x = p.index(PINK, r)
    p[r:r + cols] = p[x:r + cols] + p[r:x]
img.putdata(p)
img.show()


# Solution - 2


def straighten(source):
    target = source.copy()
    for y in range(source.size[1]):
        line = [source.getpixel((x, y)) for x in range(source.size[0])]
        pink = line.index(195)
        line = line[pink:] + line[:pink]
        for i, pixel in enumerate(line):
            target.putpixel((i, y), pixel)
    return target


out = straighten(Image.open("Python3tpc-16.gif"))
out.show()

# 根据提示获得线索信息
# Link: http://www.pythonchallenge.com/pc/return/mozart.html
# Next: http://www.pythonchallenge.com/pc/return/romance.html
#
# Points：
# - 第三方Pillow模块(PIL, Python Imaging Library，用于图像处理)：https://python-pillow.org
# - 内置enumerate函数:https://docs.python.org/3/library/functions.html#enumerate
