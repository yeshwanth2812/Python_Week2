# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:common items from 2 list

class TwoList:
    def __init__(self):
        pass
    def common_in_two_list(self,list_one,list_two):
             
        result = False
        for val1 in list_one:
            for val2 in list_two:
                if val1 == val2:
                    result = True
                    return result
        return result
if __name__ == "__main__":
    two = TwoList()
    print(two.common_in_two_list([21,42,64,"cow"],[52,42,"cow","64"]))
