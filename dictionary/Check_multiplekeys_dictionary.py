# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:Check multiple keys exists in dictionary

class CheckKeys:
    def multiple_keys(self):
      person = {"yesh" : 1, "wanth" : 2, "akari" :3} 
      print(person.keys() >= {"yesh", "wanth"}) 
      print(person.keys() >= {"akari", "shadow"})

if __name__ == "__main__":
    check_keys = CheckKeys()
    check_keys.multiple_keys()
