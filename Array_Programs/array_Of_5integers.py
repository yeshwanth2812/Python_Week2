# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title: array of 5 integers
#change it to array


import array as arr
    
def get_array_elements():
    newArray =arr.array('i', [1,2,3,4,5])
    try:
        for i in newArray:
            print(i)
    except Exception as err:
        print(err)    

if __name__ == "__main__": 
    get_array_elements() 