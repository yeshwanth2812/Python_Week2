# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:multiply all items in list

class Multiplication:
    def __init__(self):
        pass

    def multiply_list_elements(self,list1,list2):
       
        multiplication_list = []
        for number1, number2 in zip(list1,list2):
            multiplication_list.append(number1*number2)
        print("Product of list1 and list2 : ",multiplication_list)    

if __name__ == "__main__":
    multiply = Multiplication()
    multiply.multiply_list_elements([2,4,9,10],[1,5,14,2])  
