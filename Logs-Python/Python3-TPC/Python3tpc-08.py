#! python3
# -*- coding: utf-8 -*-

import bz2

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print(bz2.decompress(un))
print(bz2.decompress(pw))

# 根据提示获得线索信息
# Link: http://www.pythonchallenge.com/pc/def/integrity.html
# Next: http://www.pythonchallenge.com/pc/return/good.html（需要用户名和密码）
#
# Points：
# - bz2模块：https://docs.python.org/3/library/bz2.html
