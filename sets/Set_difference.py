# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title: create a set difference

class SetDifference:
    def get_set_difference(self):
        
        try:
            set1 = set(input("Enter set one elements :"))
            set2 = set(input("Enter set two elements :"))

            onlyset1_elements = set1.difference(set2)
            onlyset2_elements = set2.difference(set1)

            print("Elements present only in my_set1 :",onlyset1_elements)
            print("Elements present only in my_set2 :",onlyset2_elements)
            print("Common elements from both sets :",str(onlyset1_elements)+str(onlyset2_elements))
        except Exception as err:
            print(err)
if __name__ == "__main__":
    set_diff = SetDifference()
    set_diff.get_set_difference()  