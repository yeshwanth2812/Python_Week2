# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:count the number of strings in list

class StringCount:
    def __init__(self):
        pass
    def count(self):
        
        string_count = 0
        string = ['abc', 'xyz', 'aba', '1221']
        for elements in string:
            length = len(elements) 
            if length >= 2:
                if elements[0] == elements[-1]: 
                    string_count +=1
        print("String count :", string_count)
                    
if __name__ == "__main__":
    stringcount = StringCount()
    stringcount.count()