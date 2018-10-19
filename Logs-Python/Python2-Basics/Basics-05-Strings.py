# -*- coding: utf-8 -*-
__author__ = 'Anliven'

w = "This is the left side of... "
e = "a string with a right side."
print (w + e)  # 拼接字符串

end1 = "A"
end2 = "B"
end3 = "C"
print (end1 + end2 + end3),  # 在print语句的结尾加了逗号后，换行就变成了空格
print (end1 + end2 + end3)

days = "Mon Tue Wed Thu Fri \nSat Sun"  # 字符串以\n开始，显示在新的一行
print ("Here are the days: "), (days)

test = """hello,\nworld"""
print ("this is test1: %s" % test)
print ("this is test2: %r" % test)

formatter = "%r %r %r %r %r %r"
print (formatter % ("one", "two three", 123, True, False, formatter))

# "%"实际上是一种“格式控制工具”：把右边的变量带到字符串中，并且把变量值放到 %code(字符串格式化代码) 所在的位置上。
# %% 	百分号标记，即在”格式标记字符串“中输出%本身
# %c 	字符及其ASCII码
# %s 	字符串
# %r    表示打印的是对象，打印所有内容；因为可以显示原始数据（raw data）能用来做debug
# %d 	有符号整数(十进制)
# %u 	无符号整数(十进制)
# %o 	无符号整数(八进制)
# %x 	无符号整数(十六进制)
# %X 	无符号整数(十六进制大写字符)
# %e 	浮点数字(科学计数法)
# %E 	浮点数字(科学计数法，用E代替e)
# %f 	浮点数字(用小数点符号)
# %g 	浮点数字(根据值的大小采用%e或%f)
# %G 	浮点数字(类似于%g)
# %p 	指针(用十六进制打印值的内存地址)
# %n 	存储输出字符的数量放进参数列表的下一个变量中

print ('%s %s %s' % (1, 2.3, ['one', 'two', 'three']))  # 如无特殊需求,都可以使用“%s”来转换成string类型输出

print ('%6.2f' % 1.235)  # 输出的长度为6个字符，其中小数2位,实际上输出结果中小数点也占用了一位
print ('%06.2f' % 1.235)  # 如果输出的位数不足6位就用0补足6位
print ('%*.*f' % (6, 2, 1.235))  # 不事先指定输出长度和位数，在程序运行过程中再产生
print ('#' * 10)

print ('%(name)s:%(score)06.1f' % {'score': 9.5, 'name': 'newsim'})
# 在要输出的内容为dictionary数据类型时，小括号中的(name)和(score)对应于后面的键值对中的键
