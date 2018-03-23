#! python3
# -*- coding: utf-8 -*-

from PIL import Image

# Solution - 1
# If the pixel ahead is (0,0,0), copy from source. Otherwise, turn right and try again.
src = Image.open('Python3tpc-14.png')  # 下载并重命名：http://www.pythonchallenge.com/pc/return/wire.png
dst = Image.new(src.mode, (100, 100))
x, y, idx = -1, 0, 0
steps = [1, 0, 0, 1, -1, 0, 0, -1]
while idx < 10000:
    nx, ny = x + steps[0], y + steps[1]
    if 0 <= nx < 100 and 0 <= ny < 100 \
            and dst.getpixel((nx, ny)) == (0, 0, 0):
        x, y = nx, ny
        dst.putpixel((x, y), src.getpixel((idx, 0)))
        idx += 1
    else:
        steps = steps[2:] + steps[:2]
dst.show()  # http://www.pythonchallenge.com/pc/return/cat.html

# Solution - 2
im = Image.open('Python3tpc-14.png')  # 下载并重命名：http://www.pythonchallenge.com/pc/return/wire.png
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
out = Image.new('RGB', [100, 100])
i, j, p = -1, 0, 0
d = 200
while d / 2 > 0:
    for v in delta:
        steps = d // 2
        for s in range(steps):
            i, j = i + v[0], j + v[1]
            out.putpixel((i, j), im.getpixel((p, 0)))
            p += 1
        d -= 1
out.show()  # http://www.pythonchallenge.com/pc/return/cat.html

# Solution - 3
img = Image.open('Python3tpc-14.png')  # 下载并重命名：http://www.pythonchallenge.com/pc/return/wire.png
left, top, right, bottom = 0, 0, 99, 99
m, n = 0, 0
dir_x, dir_y = 1, 0
target = Image.new(img.mode, (100, 100))
for i in range(10000):
    target.putpixel((m, n), img.getpixel((i, 0)))
    if dir_x == 1 and m == right:
        dir_x, dir_y = 0, 1
        top += 1
    elif dir_y == 1 and n == bottom:
        dir_x, dir_y = -1, 0
        right -= 1
    elif dir_x == -1 and m == left:
        dir_x, dir_y = 0, -1
        bottom -= 1
    elif dir_y == -1 and n == top:
        dir_x, dir_y = 1, 0
        left += 1
    m += dir_x
    n += dir_y
target.show()

# 根据提示获得线索信息
# Link: http://www.pythonchallenge.com/pc/return/italy.html
# Next: http://www.pythonchallenge.com/pc/return/uzi.html
#
# Points：
# - 逻辑理解与实现
