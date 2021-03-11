# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:add members in a set


class AddMembers:
    def add_members(self):
        
        set_items = {'45','67','2','6789','143','24683'}
        print("Before adding another member to the set", set_items)
        set_items.add('500')
        print("After adding another member to the set", set_items)

if __name__ == "__main__":
    addmembers = AddMembers()
    addmembers.add_members() 