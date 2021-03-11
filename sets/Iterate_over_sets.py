# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title: iterate over sets

class Iteration:
    
    def iterate_set(self):
       
        try:
            set_items = set(input("Enter set items: "))
            for num in set_items:
                 print(num)
        except Exception as err:
            print("Invalid input:",err)  

if __name__ == "__main__":
    iteration = Iteration()
    iteration.iterate_set() 