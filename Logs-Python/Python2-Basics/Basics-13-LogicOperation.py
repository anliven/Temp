# -*- coding: utf-8 -*-
__author__ = 'Anliven'

print ("And : "), (True and True), (True and False), (False and False), (False and True)
print ("Or : "), (True or True), (True or False), (False or False), (False or True)
print ("Not : "), (not True), (not False)
print ("Equal or NotEqual : "), (1 == 1), (1 == 2), (1 != 1), (1 != 2)

print (True and 1 != 1), (1 != 0 or 1 == 1)
print (not ("test" == "testing")), (not (1 == 1 and not "test" == 1))

print (1 == 1 and not ("testing" == 1 or 1 == 0))
print (3 != 4 and not ("testing" != "test" or "Python" == "Python"))

print ("Special Case : "), ("show" and "test"), ("show" or "test"), (not "show")
print ("Special Case : "), (6 and 8), (6 or 8), (not 6)

# and    与
# or    或
# not    非
# !=  (not equal) 不等于
# ==  (equal) 等于
# >=    (greater-than-equal) 大于等于
# <=    (less-than-equal) 小于等于
# True    真
# False    假

# 布尔逻辑表达式(boolean logic expression)：逻辑组合的正式名称
# 判断顺序：相等判断的部分 (== or !=) ---》 括号里的 and/or ---》 每一个 not ---》 剩下的 and/or
