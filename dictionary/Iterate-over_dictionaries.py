# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title:iterating over dictionaries

dictionary = {'Red': 1, 'Green': 2, 'Blue': 3} 
for color_key, value in dictionary.items():
     print(color_key, 'corresponds to ', dictionary[color_key]) 