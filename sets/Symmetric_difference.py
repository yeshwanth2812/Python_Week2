# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title: Symmetric differnce

class SymmeticDifference:
    def get_symmetric_difference(self):
        
        try:
            set1 = set(input("Enter set one elements :"))
            set2 = set(input("Enter set two elements :"))

            symmetric_difference_set = set1.symmetric_difference(set2)
            print("Symmetric difference of two set is :",symmetric_difference_set)
        except Exception as err:
            print(err)

if __name__ == "__main__":
    symmetric_diff = SymmeticDifference()
    symmetric_diff.get_symmetric_difference()        
