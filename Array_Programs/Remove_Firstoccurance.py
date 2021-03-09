# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title: Remove the first occurance

class RemoveElement:
    def remove_first_occurance(self):
        array = []
        try:
            for _ in range(int(input("Enter the number of elements : "))):
                array.append(int(input("Enter the array elements : "))) 
            print("Array elements :",array)
            array.remove(int(input("Enter the number you want to remove : "))) 
            print("Array after removal of an element :",array)    
        except Exception as err:
            print(err)

if __name__ == "__main__":
    remove_element = RemoveElement()
    remove_element.remove_first_occurance()