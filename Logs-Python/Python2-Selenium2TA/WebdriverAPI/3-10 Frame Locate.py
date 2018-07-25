# -*- coding: utf-8 -*-
__author__ = 'Anliven'


# 在 web 应用中经常会出现 frame 嵌套的应用，frame 中实际上是嵌入了另一个页面。
# switch_to_frame 方法可以把当前定位的主体切换了 frame 里，获取 frame 中嵌入的页面，对那个页面里的元素进行定位。
# 也就是说，假如有 A、B 两个 frame，其中 B 在 A 内，那么定位 B 中的内容则需要先到 A，然后再到 B。

# 假设 id 为 f1 的 frame，而 f1 中又嵌入了 id 为 f2 的 frame，
# 通过 switch_to_frame 方法来定位 frame 内的元素
# 先找到到 ifrome1（id = f1）
# driver.switch_to_frame("f1")
# 再找到其下面的 ifrome2(id =f2)
# driver.switch_to_frame("f2")
# 然后就可以正常的操作元素了