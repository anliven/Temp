# -*- coding: utf-8 -*-
__author__ = 'Anliven'

import re  # 引入re模块(Regular Expression正则表达式)提供了正则匹配操作

text1 = "(021)88776543 010-55667890 02584453362 0571 66345673'"
print (re.findall(r"\(0\d{2,3}\)\d{7,8}|0\d{2,3}[ -]?\d{7,8}", text1))
# findall() 显示出字符串中所有匹配项,以list形式返回结果
# 匹配字符"("，需要用"\("
# “?”表示这个括号是可有可无的
# “[]”表示满足括号内的任一字符，这里的“[ -]?”表示在区号之后跟着的可能是" "、"-"，也可能什么也没有
# "|"相当于 python 中“or”的作用
# 使用“|”匹配时，会按照从左往右的顺序，一旦匹配成功就停止验证后面的规则

text2 = "234 8384 sfs 56 2sf 13 453 23s d23 78 121 19 54d 3"
print (re.findall(r"\b[0-9]*\b", text2))  # 表示任意长度的数字
print (re.findall(r"\b\d*\b", text2))  # 表示任意长度的数字
print (re.findall(r"\b[0-9]+\b", text2))  # 匹配所有数字串
print (re.findall(r"\b\d+\b", text2))  # 匹配所有数字串
print (re.findall(r"\b\d{3}\b", text2))  # 匹配3位长度的数字串
print (re.findall(r"\b1\d{1,2}\b", text2))  # 匹配第一位为1长度长度为2位或3位的数字串

print ("\bhi"), ("\\bhi"), (r"\bhi")  # r是raw的意思,表示对字符串不进行转义
# "*"表示匹配前一个字符0次或无限次数
# "[0-9]" 或"\d"表示匹配数字
# “\b”不匹配任何字符,只表示单词的分割(开头或结尾，空格、标点、换行)
# "+"表示匹配前一个字符1次或无限次数
# {}限定长度,在大括号里注明想要匹配的长度
# 字符串碰到"\"就会转义后面的字符,如果想显示"\",则必须要打"\\"

text3 = "Hi, I am Shirley Hilton. I am his wife."
print (re.findall(r"i.", text3))  # "."表示除换行符以外的任意一个字符
print (re.findall(r"i..", text3))
print (re.findall(r".", text3))
print (re.findall(r"i.*e", text3))  # "*"表示前面任意一个字可以重复多次(包括0次)；".*"贪婪匹配,匹配尽可能长的结果
print (re.findall(r"i.*?e", text3))  # ".*?"懒惰匹配,匹配尽可能短的结果
print (re.findall(r"\S", text3))  # "\S"斜线加大写字符S,表示不是空白符的任意字符

txt4 = "site sea sue sweet see case sse ssee loses"
print (re.findall(r"\bs\S?e\b", txt4))  # 匹配出所有s开头,e结尾的单词

text5 = "Hi, I am Shirley Hilton. I am his wife."
m = re.findall(r"hi", text5)  # findall() 显示出字符串中所有匹配项,以list形式返回结果
if m:
    print (m)
else:
    print ('not match')
print (re.findall(r"\bhi\b", text5))  # “\b”不匹配任何字符,只表示单词的分割(开头或结尾，空格、标点、换行)
print (re.findall(r"\bhi", text5))
print (re.findall(r"\b[Hh]i", text5))  # []表示满足括号内的任一字符

phone = "2004-959-559 # This is Phone Number"
num1 = re.sub(r'#.*$', "", phone)  # re.sub方法；相当于删除了#号之后的内容
num2 = re.sub(r'\D', "", phone)  # re.sub方法；相当于去除了所有非数字字符
print ("Phone Num1: %s " % num1), ("Phone Num2: %s " % num2)

line = "Cats are smarter than dogs"
match_out = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)  # re.match方法
print ("m-group():", match_out.group(), "m-group(1):", match_out.group(1), "m-group(2):", match_out.group(2))
search_out = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)  # re.search方法
print ("s-group():", search_out.group(), "s-group(1):", search_out.group(1), "s-group(2):", search_out.group(2))

# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print ("match --> matchObj.group() : "), (matchObj.group())
else:
    print ("No match!!")
# re.search匹配整个字符串，直到找到一个匹配。
matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print ("search --> matchObj.group() : "), (matchObj.group())
else:
    print ("No match!!")

# 正则表达式（Regular Expression）是一个特殊的字符序列，能方便的检查一个字符串是否与某种模式匹配
# re模块使Python语言拥有全部的正则表达式功能
# 几乎所有的编程语言中，正则表达式的语法都是一样的，区别只在于它们实现支持的正则表达式语法的数量不一样

# re正则表表达式语法
#
# 匹配字符
# .       匹配任意除换行符，也就是“\n”以外的任何字符。
# \       转义符，改变原来符号含义，后面会有演示。
# [ ]     中括号用来创建一个字符集，第一个出现字符如果是^，表示反向匹配。
#
# 预定义字符集
# \d      匹配数字，如：[0-9]
# \D      与上面正好相反，匹配所有非数字字符。
# \s      空白字符，如：空格，\t\r\n\f\v等。
# \S      非空白字符。
# \w      单词字符，如：大写A~Z，小写a~z，数字0~9。
# \W      非上面这些字符。
#
# 可选项与重复子模式
# *       匹配前一个字符0次或无限次数。
# +       匹配前一个字符1次或无限次数。
# ?       匹配前一个字符0次或1次。
# {m}     匹配前一个字符m次。
# {m,n}   匹配前一个字符m至n次。


# re模块重要函数
#
# re.compile()    根据正则表达式字符串，创建re模式的对象，更高效率的匹配字符串。
# re.match()      在字符串的最开始部分进行匹配。
# re.split()      根据模式的匹配项来分割字符串
# re.findall()    显示出字符串中模式的所有匹配项。以列表的形式返回结果。
# sub(old,new)    方法的功能是，用将所有old的匹配项用new替换掉。
# re.escape()     可以对要查找的字符串中所有可能会被解释为正则运算符的字符进行转义。
# re.search()     寻找模式。会在给定的字符串中，寻找第一个匹配的正则表达式子串。
# re.search()     函数找到子字符串的话会返回MatchObject，值为 True，找不到会返回None，值为False。
#
# re.match方法
# 函数语法： re.match(pattern, string, flags=0)
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# flags	    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
# 匹配成功re.match方法返回一个匹配的对象，否则返回None。
#
# re.search方法
# 函数语法：re.search(pattern, string, flags=0)
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# flags	    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
# 匹配成功re.search方法方法返回一个匹配的对象，否则返回None。
#
# 获取匹配表达式
# re.match方法和re.search方法可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式
# group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组
# groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号
#
# re.match与re.search的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# re.search匹配整个字符串，直到找到一个匹配。
#
# re.sub方法
# 函数语法：re.sub(pattern, repl, string, max=0)
# 可选参数max是模式匹配后替换的最大次数；max 必须是非负整数。缺省值是 0 表示替换所有的匹配。
# 返回的字符串是在字符串中用 RE 最左边不重复的匹配来替换。如果模式没有发现，字符将被没有改变地返回。


# 正则表达式修饰符
# 正则表达式可以包含一些可选标志修饰符来控制匹配的模式
# 修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定
#
# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使 . 匹配包括换行在内的所有字符
# re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
