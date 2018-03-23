#! python3
# -*- coding: utf-8 -*-

# Solution - 1 - proposal
temp = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. 
rfyrq ufyr amknsrcpq ypc dmp. 
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. 
lmu ynnjw ml rfc spj.'''

in_tab = "abcdefghijklmnopqrstuvwxyz"
out_tab = "cdefghijklmnopqrstuvwxyzab"
tran_tab = str.maketrans(in_tab, out_tab)
print(temp.translate(tran_tab))

# Solution - 2
# result = ""
# for c in temp:
#     if c >= 'a' and c <= 'z':
#         result += chr(((ord(c) + 2) - ord('a')) % 26 + ord('a'))
#     else:
#         result += c
# print(result)
print(''.join([chr(((ord(s) + 2) - ord('a')) % 26 + ord('a')) if 'a' <= s <= 'z' else s for s in temp]))

# Solution - 3
tempList = []
for i in range(0, len(temp)):
    if ord("a") <= ord(temp[i]) <= ord("z"):
        if ord(temp[i]) >= ord("y"):
            tempList.append(chr(ord(temp[i]) + 2 - 26))
        else:
            tempList.append(chr(ord(temp[i]) + 2))
    else:
        tempList.append(temp[i])

for item in tempList:  # 列表迭代
    print(item, end='')
print('\n')

ttt = """map"""
print(ttt.translate(tran_tab))

# 根据提示获得线索信息
# Link: http://www.pythonchallenge.com/pc/def/map.html
# Next: http://www.pythonchallenge.com/pc/def/ocr.html
#
# Points：
# - 字符串处理
# - str.maketrans()
