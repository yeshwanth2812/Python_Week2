# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:clone a list

class Clone:

    def __init__(self):
        pass
    def copy_list(self):
    
        try:
            original_list = [1,2,]
            new_list = list(original_list)
            print("Original list :", original_list)   
            print("New list :", new_list)
        except Exception as err:
            print(err)
if __name__ == "__main__":
    clone = Clone()
    clone.copy_list()      