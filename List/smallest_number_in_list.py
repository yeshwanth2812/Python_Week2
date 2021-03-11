# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:smallest number from a  list

class Smallest:
    def __init__(self):
        pass
    def smallest_value(self):
        
        small = []
        number = int(input("Enter the list length : "))
        for _ in range(number):
            elements = int(input("Enter the elements : "))
            small.append(elements)
        print("Smallest number is : ", min(small))    

if __name__ == "__main__":
    smallest = Smallest()
    smallest.smallest_value()        