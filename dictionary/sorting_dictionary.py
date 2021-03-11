# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title:sorting a dictionary

import operator
dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',dictionary)
sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_dictionary)
sorted_dictionary = dict( sorted(dictionary.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_dictionary)