# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title: file existing

import os.path
open('file_check.txt', 'w')
print(os.path.isfile('file_check.txt'))