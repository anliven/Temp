# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# ----------------------------------------------------------------------------------------------------------------------
### 简单的测试

# def Testfunc():
#     a = 1
#     b = 2
#     assert a != b

# ----------------------------------------------------------------------------------------------------------------------
### 测试的执行

# def Testfunc1():
#     a = 1
#     b = 2
#     print a,b
#     assert a == b
# def Testfunc2():
#     print "testfunc2"
#     assert True

# ----------------------------------------------------------------------------------------------------------------------
### setUp和tearDown

# # 单独指定函数的setUp和tearDown
# def setUp():
#     print "function setup"
# def tearDown():
#     print "function teardown"
# def func3Start():
#     print "func3 start"
# def func3End():
#     print "func3 end"
# def Testfunc3():
#     print "Testfunc3"
#     assert True
# Testfunc3.setup = func3Start
# Testfunc3.tearDown = func3End

# from nose.tools import with_setup
# def setUp():
#     print "function setup"
# def tearDown():
#     print "function teardown"
# def func1Start():
#     print "func1 start"
# def func1End():
#     print "func1 end"
# def func2Start():
#     print "func2 start"
# def func2End():
#     print "func2 end"
# @with_setup(func1Start, func1End)
# def Testfunc1():
#     print "Testfunc1"
#     assert True
# @with_setup(func2Start, func2End)
# def Testfunc2():
#     print "Testfunc2"
#     assert True

# # 类的的setUp和tearDown
# class TestClass():
#     arr1 = 2
#     arr2 = 2
#     def setUp(self):
#         self.arr1 = 1
#         self.arr2 = 3
#         print "MyTestClass setup"
#     def tearDown(self):
#         print "MyTestClass teardown"
#     def Testfunc1(self):
#         assert self.arr1 != self.arr2
#     def Testfunc2(self):
#         assert self.arr1 != 2

# # 模块的setUp和tearDown
# def setUp():
#     print "function setup"
# def tearDown():
#     print "function teardown"
# def Testfunc1():
#     print "Testfunc1"
#     assert True
# def Testfunc2():
#     print "Testfunc2"
#     assert True

# ----------------------------------------------------------------------------------------------------------------------
