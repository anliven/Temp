#! python3
# -*- coding: utf-8 -*-
from PIL import Image

im = Image.open('Python3tpc-11.jpg')
print(im.size)
(w, h) = im.size

evenPic = Image.new('RGB', (w // 2, h // 2))
oddPic = Image.new('RGB', (w // 2, h // 2))

for i in range(w):
    for j in range(h):
        p = im.getpixel((i, j))
        if (i + j) % 2 == 1:
            oddPic.putpixel((i // 2, j // 2), p)
        else:
            evenPic.putpixel((i // 2, j // 2), p)

# evenPic.save('Python3tpc-11-even.jpg')
# oddPic.save('Python3tpc-11-odd.jpg')
evenPic.show()
oddPic.show()

# 根据提示获得线索信息
# Link: http://www.pythonchallenge.com/pc/return/5808.html
# Next: http://www.pythonchallenge.com/pc/return/evil.html
#
# Points：
# - 第三方Pillow模块(PIL, Python Imaging Library，用于图像处理)：https://python-pillow.org
