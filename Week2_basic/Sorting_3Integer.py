# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title: Sorting 3 integers

First_integer = int(input("Input first number: "))
Second_integer = int(input("Input second number: "))
Third_integer = int(input("Input third number: "))

Minimum_integer = min(First_integer, Second_integer, Third_integer)
Maximum_integer = max(First_integer, Second_integer, Third_integer)
Result = (First_integer + Second_integer + Third_integer) - Minimum_integer - Maximum_integer
print("Numbers in sorted order: ", Minimum_integer, Result, Maximum_integer)