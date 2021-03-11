# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:difference between two list

class Difference:
    def __init__(self):
        self.list1 = list1
        self.list2 = list2
        self.list_differcence = []
    def difference_of_two_list(self,list_differcence):

        for elements in list1:
            if elements not in list2:
                list_differcence.append(elements)        
        print("List difference :",list_differcence)

if __name__ == "__main__":
    list1=[1,2,3,4,'python','(2,"a")']
    list2=[1,2,"xy",'dog',6,10]
    differ = Difference()
    differ.difference_of_two_list([])      