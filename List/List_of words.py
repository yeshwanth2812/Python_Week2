# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:list of words longer than n

class LongestLength:
    def __init__(self):
        pass
    def get_length_of_longest(self):
        
        try:
            list_of_words = input("Enter list of words separated by comma: ")
            longest_length = []
            for value in list_of_words.split(","):
                word_length = int(input("Enter word length :"))
                if len(value) > word_length:
                        longest_length.append(value)
                print("Longest words are ",longest_length)
        except Exception as err:
            print(err)        
      
if __name__ == "__main__":  
    lng = LongestLength()
    lng.get_length_of_longest()