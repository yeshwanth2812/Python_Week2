# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title: Calander

import calendar  
# doc string heass
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))