# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title: find max and min in a set

class MaxMin:
    def get_max_min_values(self):
        
        try:
            set1 = set(input("Enter your values :"))
            print("Maximum value in set :",max(set1))
            print("Minimum value in set :",min(set1))
        except Exception as err:
            print(err)
        
if __name__ == "__main__":
    max_min = MaxMin()
    max_min.get_max_min_values()        
