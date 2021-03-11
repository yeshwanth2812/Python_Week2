# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:removing an item from a set

class RemoveItems:
    
    def revome_item_from_set(self):
        
        set_items = {'143', '67', '24683', '6789', '2', '45'}
        print("Before removing another member to the set",set_items)
        set_items.remove('24683')
        print("after removing another member to the set",set_items)

if __name__ == "__main__":
    remove_items = RemoveItems()
    remove_items.revome_item_from_set() 
