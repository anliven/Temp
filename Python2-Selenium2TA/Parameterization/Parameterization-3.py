# -*- coding: utf-8 -*-
import csv  # 导入 csv 模块
__author__ = 'Anliven'

# 读取本地 CSV 文件
my_file = 'D:\\Anliven-Running\\Zen\\PycharmProjects\\Selenium2Python2TA\\Parameterization\\userinfo.csv'
data = csv.reader(file(my_file, 'rb'))

# 循环输出每一行信息
for user in data:
    print user[0], user[1], user[2], user[3]

# 通过 WPS 或 excel 创建表格，文件另存为选择 CSV 格式
# 可以循环读取CSV文件的每一条数据，又不局限每次所读取数据的个数
# csv.reader()用于读取 CSV 文件
# user[0] 表示表格中第一列的数据（用户名）
# user[1]表示表格中第二列的数据（邮箱） ，后面类推

# Python 读取csv文件到excel
# http://www.cnblogs.com/Skyyj/p/4753547.html

# 解决问题的方法是多样的，贴合需求，用最简洁的方法来解决复杂问题，高效易维护

# Python Console 界面中文字符显示问题
# 本示例示例中限定了 “# -*- coding: utf-8 -*-”，因此userinfo.csv文件中的中文编码也要以utf-8格式保存
# 可以利用Notepad++来转化格式，菜单栏--》格式--》转为UTF-8编码格式，然后保存即可
