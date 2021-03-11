# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:convert list to a nested dictionay keys

class NestedDictionary:
  def get_nested_dictionary(self):
    list1 = ['Yesh', 'Wanth', 'akari'] 
    list2 = ['shadow', 'archer', 'venom'] 
    list3 = [2, 4, 6] 
   
    nested_dictionary = [{a: {b: c}} for (a, b, c) in zip(list1, list2, list3)] 
  
    print("Nested dictionary :",nested_dictionary)

if __name__ == "__main__":
    nested_dict = NestedDictionary()
    nested_dict.get_nested_dictionary()    