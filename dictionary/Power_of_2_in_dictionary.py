# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title:Power of 2 in dictionary

number=int(input("Input a number "))
dictionary = dict()

for x in range(1,number+1):
    dictionary[x]=x*x

print(dictionary) 