# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:Remove duplicates from a list of list

class DuplicateList:
    def __init__(self):
        pass
    def remove_duplicate(self):
        
        list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        new_list = []
        for elements in list1:
            if elements not in new_list:
                new_list.append(elements)
        print("New list without duplicates")        
        print(new_list)

if __name__ == "__main__":
    duplicatelist = DuplicateList()
    duplicatelist.remove_duplicate()       