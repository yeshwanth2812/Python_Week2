# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title: display calender

from datetime import date
from_date = date(2021, 1, 1)
last_date = date(2021, 2, 25)
delta = last_date - from_date
print(delta.days)