# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:intersection of sets

class Intersection:
    def intersection_set(self):
       
        try:
            set_items = set(input("Enter set items: "))
            set_items2 = set(input("Enter set items: "))
            set1 = set_items.intersection(set_items2)
            print("Intersection of set")
            print(set1)
        except Exception as err:
            print("Invalid input:",err)  

if __name__ == "__main__":
    intersect = Intersection()
    intersect.intersection_set() 