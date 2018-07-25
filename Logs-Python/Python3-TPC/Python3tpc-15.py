#! python3
# -*- coding: utf-8 -*-

import datetime
import calendar

# Solution - 1
n = 1006
list_year = []
while 1006 <= n <= 1996:
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:  # 判断闰年
        if n % 10 == 6 and datetime.date(n, 1, 26).isoweekday() == 1:  # 判断年份尾号为6和具体日期
            list_year.append(n)
    n += 1
print(str(list_year[-2]) + "-01-27")  # 搜索此日期

# Solution - 2
list_year2 = []
for year in range(1006, 1996, 10):
    if calendar.isleap(year) and datetime.date(year, 1, 27).isoweekday() == 2:
        list_year2.append(year)
print(str(list_year2[-2]) + "-01-27")  # 搜索此日期

# 根据提示获得线索信息
# Link: http://www.pythonchallenge.com/pc/return/uzi.html
# Next: http://www.pythonchallenge.com/pc/return/mozart.html
#
# Points：
# - 逻辑理解与实现
# - 标准库datetime模块：https://docs.python.org/3/library/datetime.html
# - 标准库calendar模块：https://docs.python.org/3/library/calendar.html
