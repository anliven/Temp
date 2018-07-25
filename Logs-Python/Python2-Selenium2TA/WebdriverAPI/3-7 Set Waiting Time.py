# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 导入 WebDriverWait 包
from time import sleep  # 直接导入了 time 包的 sleep()方法后，可以直接使用sleep()
__author__ = 'Anliven'

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

# WebDriverWait()方法使用
element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("kw"))  # ??? lambda函数
element.send_keys("selenium")

# 添加智能等待
driver.implicitly_wait(30)
driver.find_element_by_id("su").click()

# 添加固定休眠时间
sleep(5.5)  # sleep()方法以秒为单位，可以用小数表示

driver.quit()


# sleep()： 设置固定休眠时间。
# time 包提供了休眠方法 sleep() ，是将脚本的执行过程进行休眠。
# sleep()方法以秒为单位，可以用小数表示；只能在一个固定的时间点等待

# implicitly_wait()：是 webdirver 提供的一个超时等待。
# 等待一个元素被发现，或一个命令完成。如果超出了设置时间的则抛出异常。
# 可以在一个固定的时间点或时间范围内智能的等待

# WebDriverWait()：同样也是 webdirver 提供的方法。
# 在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常。

# WebDriverWait() 详细格式如下：
# WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
# driver --- WebDriver 的驱动程序(Ie, Firefox, Chrome 或远程)
# timeout --- 最长超时时间，默认以秒为单位
# poll_frequency --- 休眠时间的间隔（步长）时间，默认为 0.5 秒
# ignored_exceptions --- 超时后的异常信息，默认情况下抛 NoSuchElementException 异常。

# WebDriverWai()一般由 unit()或 until_not()方法配合使用，
# until(method, message=’ ’) --- 调用该方法提供的驱动程序作为一个参数，直到返回值不为 False。
# until_not(method, message=’ ’) --- 调用该方法提供的驱动程序作为一个参数，直到返回值为 False。