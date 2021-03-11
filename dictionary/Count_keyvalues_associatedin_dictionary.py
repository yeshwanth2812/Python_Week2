# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:count the values associated with a key in a dictionary

class ValueCount:
    def get_value_count(self):
        list_items =  [{'id': 1, 'success': True, 'name': 'Lary'}, 
                       {'id': 2, 'success': False, 'name': 'Rabi'}, 
                       {'id': 3, 'success': True, 'name': 'Alex'}]
        success_count = 0
        for dictionary_items in list_items:
            if 'success' in dictionary_items:
                if dictionary_items['success'] == True:
                    success_count +=1
        print("Success count as true is :",success_count)   

if __name__ == "__main__":
    value_count = ValueCount()
    value_count.get_value_count()                 