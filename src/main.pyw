# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 22:40
# @Author  : Tony Goods
# @FileName: main.pyw
# @Software: PyCharm

import time

file = open("test.txt", "w")
file.write(time.asctime(time.localtime(time.time())) + "\n")
file.close()
exit()
