# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:Unique value in dictionaary

class UniqueValues:
   
    def get_unique_values(self):
       
        dictionary = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
        
        print("Original dictionary :", dictionary)
        print("Unique values :", list(set(val for items in dictionary for val in items.values())))

if __name__ == "__main__":
    uniq_values = UniqueValues()
    uniq_values.get_unique_values()