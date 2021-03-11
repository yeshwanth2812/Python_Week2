# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:clear a set

class ClearSet:
    def to_clear_set(self):
       
        try:
            set1 = set(input("Enter your set elements :"))
            set1.clear()
            print("Set after clear :",set1)
        except Exception as err:
          print(err)

if __name__ == "__main__":
    clr_set = ClearSet()
    clr_set.to_clear_set()        
