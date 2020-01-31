# This as very bad style of OOP
# Learn about OOP in depth in python and about __init__ and 'self'
"""
Only initialization of values in __init__ and no function calls should be made in it as a good practice
Also it should not return anything
"""

class Anagram:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def remove_spaces(self, string):
        self.string = string
        self.res = ""

        for char in string:
            if char != " ":
                self.res += char

        return  self.res

    def sort_string(self, string):
        self.string = string
        self.arr = [char for char in string]
        self.res = ""

        for i in range( len(self.arr) ):
            j = i + 1

            for j in range(len( self.arr) ):
                if self.arr[i] < self.arr[j]:
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        for char in self.arr:
            self.res += char

        return self.res

    def check_anagram(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

        self.str1_wo_space = self.remove_spaces(self.str1)
        self.str2_wo_space = self.remove_spaces(self.str2)

        if len(self.str1_wo_space) != len(self.str2_wo_space):
            print("Not an anagram")

        else:
            self.sorted_str1 = self.sort_string(self.str1_wo_space)
            self.sorted_str2 = self.sort_string(self.str2_wo_space)

            if self.sorted_str1 == self.sorted_str2:
                print("Anagram")
            else:
                print("Not an Anagram")

if __name__ == "__main__":
    str1 = input("Enter first string")
    str2 = input("Enter second string")

    anagram_obj = Anagram(str1, str2)
    anagram_obj.check_anagram(str1, str2)

