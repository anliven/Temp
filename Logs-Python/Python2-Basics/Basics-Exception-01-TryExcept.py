# -*- coding: utf-8 -*-
__author__ = 'Anliven'

try:
    a = 10
    b = 0
    print (a / b)  # 因分母可以为零，会产生“ZeroDivisionError: integer division or modulo by zero”的异常错误
except ZeroDivisionError:  # 指明错误/异常的名称，这里使用ZeroDivisionError
    print ("除零错误，已经捕获！")

# 异常（Exception）
# 在编写和调试代码的过程中，如果Python无法正常处理程序时，Python会抛出一个异常，表示一个错误。
# 如果这种异常没有被处理或者捕捉，程序就会终止运行，抛出异常信息来提醒用户处理这些错误。
# 一个异常可以是一个字符串，类或对象。 Python的内核提供的异常，大多数都是实例化的类。
#
# 常见python标准异常
# Exception  ----- 常规错误
# Warning 	----- 警告
# SyntaxWarning	----- 可疑语法的警告
# RuntimeError 	----- 一般的运行时错误
# SyntaxError	----- Python语法错误
# IndentationError	----- 缩进错误
# TabError	----- Tab和空格混用


# 捕捉异常 - try-except语句
# try-except语句用来捕捉异常，检测try语句块中的错误，从而让except语句捕获异常信息并处理。
# 对于每个try从句，至少都有一个相关联的except从句。
# 如果当try语句执行时发生异常，python执行第一个匹配该异常的except子句，处理异常。
# 可以关联上一个else从句，当没有异常发生的时候，else从句将被执行。
# 如果异常没有匹配的except子句，异常将被递交到上层的try来捕捉，直到默认的Python处理器被调用，终止程序运行，并且打印一个异常消息
#
# 如果使用except而不指明异常类型或名称，那么try-except语句将捕获所有异常；不建议使用此方式，因为不能识别出具体的异常信息。
#
# except从句可以专门处理单一的异常，或者一组包括在圆括号内的异常。
# 如果需要同时捕捉多个可能的异常，可以把异常的类型，放入一个元组中，举例说明：except (ZeroDivisionError, TypeError）
