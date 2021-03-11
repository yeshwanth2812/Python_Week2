# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title:Concatenate of dictionarys

dictionary1={1:10, 2:20}
dictionary2={3:30, 4:40}
dictionary3={5:50,6:60}
dictionary4 = {}
for d in (dictionary1, dictionary2, dictionary3): dictionary4.update(d)
print("Expected Updated Dictionary",dictionary4)