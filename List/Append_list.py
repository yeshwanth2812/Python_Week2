# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title: append a list

class AppendList:
    def __init__(self):
        pass
    def second_list(self):
        list1 = [1,2,[3,4],"list",67]
        list2 = [43,21,2,0,(3,4)]
        for elements in list2:
            list1.append(elements)
        print("Resultant of first list and second list")    
        print(list1)    

if __name__ == "__main__":
    appendlist = AppendList()
    appendlist.second_list()
