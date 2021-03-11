# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title:Remove a key from dictionary

Dictionary = {'a':1,'b':2,'c':3,'d':4}
print("Dictionary before removing a key",Dictionary)
if 'a' in Dictionary: 
    del Dictionary['a']
print("Dictionary after removing a Key",Dictionary)