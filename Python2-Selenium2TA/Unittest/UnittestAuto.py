# -*- coding: utf-8 -*-
from UnittestWidget import Widget  # 引入被测试模块的被测试类
import unittest  # 用 import 语句引入 unittest 模块
__author__ = 'Anliven'


# 执行测试的类
# 可以在一个测试类中，写多个测试用例对被测试类的方法进行测试
class WidgetTestCase(unittest.TestCase):  # WidgetTestCase类继承于 unittest 的 TestCase 类

    def setUp(self):  # unittest.TestCase类中定义的setUp()方法,进行测试前的初始化工作
        self.widget = Widget()

    def testSize(self):  # 测试 getsize()方法的测试用例
        self.assertEqual(self.widget.getsize(), (40, 40))
        # 对 Widget 类中 getsize()方法的返回值和预期值进行比较，确保两者是相等的
        # assertEqual()也是 unittest.TestCase类中定义的方法

    def testResize(self):  # 测试 resize()方法的测试用例
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getsize(), (100, 100))

    def tearDown(self):  # unittest.TestCase类中定义的tearDown()方法,进行测试前的初始化工作
        self.widget.dispose()
        self.widget = None

# 运行测试
if __name__ == "__main__":
    suitetest = unittest.TestSuite()  # 构造测试集，作为整个单元测试的入口，unittest通过调用它来完成整个测试过程
    suitetest.addTest(WidgetTestCase("testSize"))  # 添加测试用例
    suitetest.addTest(WidgetTestCase("testResize"))
    runner = unittest.TextTestRunner()
    runner.run(suitetest)  # 执行测试
# unittest 使用 TestRunner 类作为测试用例的基本执行环境，来驱动整个单元测试过程
# 但在进行单元测试时一般使用其子类 TextTestRunner 来完成测试，并将测试结果以文本方式显示出来


# 如果以 test 开头来命名所有的测试方法，只需要如下代码即可运行测试：
# if __name__ == "__main__":
#     unittest.main()  # 直接使用 unittest.main()来运行所有用例


# 测试用例集包含多个测试用例，在unittest framework 里用 TestSuite 类来表示
# TestSuite 类可以看成是 TestCase 类的一个容器，用来对多个测试用例进行组织
# 这样多个测试用例可以自动在一次测试中全部完成

# .py 文件有两种使用方式：作为模块被调用和直接使用
# __name__作为模块的内置属性，简单点说呢，就是.py文件的调用方式
# 如果"__name__"等于"__main__"就表示是直接执行
# 如果.py 文件做为一个模块被调用；这个时候 if __name__ == “__main__”：后面的内容将不会被执行
