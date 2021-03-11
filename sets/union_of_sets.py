# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:union of sets

class SetUnion:
    def get_union_of_sets(self):
        
        set1 = set(input("Enter set one elements: "))
        set2 = set(input("Enter set two elements: "))

        union_of_both_sets = set1.union(set2)
        print("Union of two sets is :", union_of_both_sets)

if __name__ == "__main__":
    set_union = SetUnion()
    set_union.get_union_of_sets()        
