# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# 种类繁多的验证码在一定程度上增加了安全性。但对于测试人员来说，不管是进行性能测试还是自动化测试都是一个棘手的问题。
# 处理验证码的几种方法：

# ### 去掉验证码
# 这是最简单的方法，只是把验证码的相关代码注释掉即可
# 在测试环境，这样做可省去了测试人员不少麻烦，但如果是在正式环境，这样就给系统带来了风险

# ### 设置万能码
# 在程序中临时设置一个“万能验证码”

# ### 验证码识别技术
# 使用第三方的验证码识别
# 例如：Python-tesseract 是光学字符识别 Tesseract OCR 引擎的 Python 封装类，能够读取常规的图片文件
# 验证码形式繁多，目前任何一种验证码识别技术，都无法保证完整的识别率

# ### 记录 cookie
# 通过向浏览器中添加 cookie 可以绕过登录的验证码
# 在用户登录之前，通过 add_cookie(）方法将用户名密码写入浏览器 cookie ，再次访问系统登录链接将自动登录。
# 难点是如何获得cookie中用户名密码的 name ，如果找到不到 name 的名字，就没办法向 value 中输入用户名、密码信息
# 建议是可以通过 get_cookies()方法来获取登录的所有的 cookie 信息，从而进行找到用户名、密码的 name 对象的名字
# 当然，最简单的方法还是询问前端开发人员

# # cookie方法简单示例
# driver.get("http://www.xxxx.cn/")  # 访问 xxxx 网站
# driver.add_cookie({'name':'Login_UserNumber', 'value':'username'})  # 将用户名写入浏览器 cookie
# driver.add_cookie({'name':'Login_Passwd', 'value':'password'})  # 将密码写入浏览器 cookie
# driver.get("http://www.xxxx.cn/")  # 再次访问 xxxx 网站，将会自动登录
