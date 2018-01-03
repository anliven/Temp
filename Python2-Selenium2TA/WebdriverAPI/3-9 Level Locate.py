# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
__author__ = 'Anliven'

print "层级定位"
# 层级定位。先定位父元素，然后再通过父元素定位子孙元素。
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('Sample__LeveLocate.html')
driver.get(file_path)

menu = driver.find_element_by_link_text('Menu3').click()
ActionChains(driver).move_to_element(menu)

menu1 = driver.find_element_by_xpath('html/body/ul/li[2]/div/a[2]')
ActionChains(driver).move_to_element(menu1).perform()

time.sleep(15)
driver.quit()
