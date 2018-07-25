# -*- coding: utf-8 -*-
# BY_CSS_SELECTOR = find_element_by_css_selector()
__author__ = 'Anliven'

print "id 和 name 定位"

# webdriver 提供了一系列的元素定位方法，常用的有以下几种
# id  --- id 和 name 是最常用的定位方式，大多数元素都有这两个属性
# name
# class name --- 每个元素总是都会有id、name和class属性
# tag name  --- 同一个页面中具有相同 tag name 的元素极其容易出现,tag name 定位并一定准确
# link text  --- 需要操作的元素是一个文字链接，可以通过 link text 或 partial link text 进行元素定位
# partial link text  --- 链接很长时，可以只取其中的一部分，只要取的部分可以唯一标识元素
# xpath  --- 在 XML 文档中用相对路径或绝对路径定位元素；可以做布尔逻辑运算；缺陷明显（性能差、适宜性差、兼容性差）
# css selector --- selenium可以把CSS(Cascading Style Sheets)CSS 使用的选择器作为定位策略

# 分别对应 python webdriver 中的方法为：
# find_element_by_id()
# find_element_by_name()
# find_element_by_class_name()
# find_element_by_tag_name()
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_xpath()
# find_element_by_css_selector()
