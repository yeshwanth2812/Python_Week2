# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:calculate the length of string

class stringlength:

    str = input("Enter a string: ")

# counter variable to count the character in a string
    counter = 0
    for s in str:
        counter = counter+1
        print("Length of the input string is:", counter)