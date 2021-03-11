# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 2021-01-04 18:58:12
# @Last Modified by: Yeshwanth
# @Last Modified time: 2021-01-09 11:59:53
# @Title:Create a dictionary from a string

class CreateDictionary:
    def get_string_to_create_dictionary(self):
        string_input = input("Enter your string : ")
        new_dictionary = {character: string_input.count(character) for character in string_input}
        print("New dictionary :",new_dictionary)

if __name__ == "__main__":
    create_dictionary = CreateDictionary()
    create_dictionary.get_string_to_create_dictionary()       