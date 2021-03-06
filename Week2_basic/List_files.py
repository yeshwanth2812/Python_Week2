# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title: list files in directory

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/yeshwanth/Desktop/Programs/Basic') if isfile(join('/home/yeshwanth/Desktop/Programs/Basic', f))]
print(files_list)