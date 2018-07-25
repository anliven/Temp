# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# 实现摄氏温度和华氏温度的转换
# 待测模块temperature.py
# 代码如下：

def to_celsius (t):
    return round ( (t-32.0)*5.0/9.0 )

def above_freezing (t):
    return t>0

