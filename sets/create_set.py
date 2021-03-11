# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title: create a set


class CreateSet:
    def create_a_set(self):
        
        try:
            set_elements = set(input("Enter set items: "))
            print(set_elements)
        except Exception as err:
             print("Invalid input:",err)  

if __name__ == "__main__":
    createset = CreateSet()
    createset.create_a_set() 