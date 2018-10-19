# -*- coding: utf-8 -*-
__author__ = 'Anliven'

sample = """
AAAAA
\tBBBBB
CCCCC\nDDDDDD
\n\t\tEEEEE
"""
# 一组三引号(triple-quotes)之间放入任意多行文字

print ('AAA\'BBBCCC\\DDD\nEEE\tFFF')
print ("----------------"), (sample), ("----------------")

# 转义序列(Escape Sequences)/转义字符(Escape Characters)
#
# 转义字符：反斜杠 \(back-slash)；双反斜杠(double backslash)“\\”会打印出一个反斜杠
# \\ --- Backslash (\)反斜杠
# \' --- Single quote(‘) 单引号
# \" --- Double quote(”) 双引号
# \a --- ASCII Bell(BEL) 响铃
# \b --- ASCII Backspace(BS) 退格
# \e --- 转义
# \f --- ASCII FormFeed(FF) 进纸/换页
# \n --- ASCII Linefeed(LF) 换行符
# \r ASCII --- CarriageReturn (CR)回车
# \t ASCII --- HorizontalTab (TAB) 水平制表
# \v --- ASCIIVertical Tab(VT) 垂直制表
# \oyy	八进制数，yy代表的字符，例如：\o12代表换行
# \xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
# \other	其它的字符以普通格式输出
