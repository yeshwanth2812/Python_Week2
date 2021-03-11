# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:remove an item if present in set

class Remove:
    
    def revome_if_present(self):
        
        set_items = {'143', '67', '24683', '6789', '2', '45'}
        if '500' in set_items:
            #print("item not present in set")
            set_items.remove('500')
        print("item not present in set")
        print(set_items)

if __name__ == "__main__":
    remove = Remove()
    remove.revome_if_present() 
