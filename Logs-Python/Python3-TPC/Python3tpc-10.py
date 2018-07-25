#! python3
# -*- coding: utf-8 -*-
import re
import itertools

# Solution - 1
a = '1'
b = ''
for i in range(0, 30):
    j = 0
    k = 0
    while j < len(a):
        while k < len(a) and a[k] == a[j]:
            k += 1
        b += str(k - j) + a[j]
        j = k
    # print(b)
    a = b
    b = ''
print(len(a))

# Solution - 2
x = "1"
for m in range(30):
    x = "".join([str(len(j) + 1) + i for i, j in re.findall(r"(\d)(\1*)", x)])
print(len(x))

# Solution - 3
y = "1"
for n in range(30):
    y = "".join([str(len(list(j))) + i for i, j in itertools.groupby(y)])
print(len(y))

# 根据提示获得线索信息
# Link: http://www.pythonchallenge.com/pc/return/bull.html
# Next: http://www.pythonchallenge.com/pc/return/5808.html
#
# Points：
# - 外观数列(Look-and-say sequence)的定义
# - 标准库itertools模块：https://docs.python.org/3/library/itertools.html
