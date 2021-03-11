# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:Remove specific items

class RemoveElements:
    def __init__(self):
        pass
    def elements_removal(self):
        
        given_list =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        del given_list[0]
        given_list.remove('Pink')
        given_list.pop() #pop removes elements from the end
        print("Elements remaining: ", given_list)
if __name__ == "__main__":
    removal = RemoveElements()
    removal.elements_removal()      