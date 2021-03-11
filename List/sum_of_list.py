# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:Sum of all elements in list

class SumOfElements:
    def __init__(self):
        self.list1 = [] 
    
    def calculate_sum(self):
       
        list_number = int(input("Number of elements :"))
        for _ in range(list_number):
            list_elements = int(input("Enter the element :"))
            self.list1.append(list_elements)    
        print("Sum Of All The Elements In List Is :", (self.list1))
        
if __name__ == "__main__":
  
    total = SumOfElements()
    total.calculate_sum()