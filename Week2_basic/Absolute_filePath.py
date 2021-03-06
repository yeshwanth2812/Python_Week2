# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 12:30:53
# @Title: Absolute file name

import os
def absolute_file_path(path_fname):
        return os.path.abspath('path_fname')        
print("Absolute file path: ",absolute_file_path("test.txt"))