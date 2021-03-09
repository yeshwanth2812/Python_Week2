# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title: occurance of elements in array

class CountOccurance:
    def get_no_of_occurances(self):
        array = []
        try:
            for _ in range(int(input("Enter the number of elements : "))):
                array.append(int(input("Enter the array elements : "))) 
            print("Array elements :",array)
            number_count = array.count(int(input("Enter the number you want to count :"))) 
            print("Number of occurance is :",number_count)    
        except Exception as err:
            print(err)

if __name__ == "__main__":
    count_occurance = CountOccurance()
    count_occurance.get_no_of_occurances()
