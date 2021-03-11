# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title:Print a dictionary in table format

dictionary = {'A':[1,2,3],'B':[1,2,3],'C':[1,2,3]}
for row in zip(*([key] + (value) for key, value in sorted(dictionary.items()))):
    print(*row)