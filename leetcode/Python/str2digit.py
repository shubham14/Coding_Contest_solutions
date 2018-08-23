# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 13:06:50 2018

@author: Shubham
"""

# Python implementation for comverting words to numbers
import math

class Solution:
    def __init__(self, ones, tens, multipliers):
        self.ones = ones
        self.tens = tens
        self.mult = multipliers
    
    def return_ind(self, l, word):
        return l[word] if word in l else -1
    
    # str1 is the string with the word representation of the number
    def word2nums(self, str1):
        str1 = str1.split()
        str1 = list(filter(lambda x: x != "and", str1))
        ans = 0
#        for ele in str1:
#            val_o = self.return_ind(self.ones, ele)
#            val_t = self.return_ind(self.tens, ele)
#            val_m = self.return_ind(self.mult, ele)
#            print(ele, val_m)
#            if val_o != -1:
#                ans += val_o
#            elif val_t != -1:
#                ans += val_t*10
#            else:
#                ans *= int(math.pow(10,val_m))
#            print(ans)
        if val_o != -1:
            ans += val_o
            ans *= 10
        elif val_t != -1:
            ans += val_t
            ans *= 10
        else:
            ans /= 10
            ans *= int(math.pow(10, val_m)) 
        return int(ans)
        
    
if __name__ == "__main__":
    ones = ["", "one ", "two ", "three ", "four ",
                 "five ", "six ", "seven ", "eight ",
                 "nine ", "ten ", "eleven ", "twelve ",
                 "thirteen ", "fourteen ", "fifteen ",
                 "sixteen ", "seventeen ", "eighteen ",
                 "nineteen "]
    
    ones = dict((ones[i].strip(),i) for i in range(len(ones)))
    
    
    tens = ["", "", "twenty ", "thirty ", "forty ",
                 "fifty ", "sixty ", "seventy ", "eighty ",
                 "ninety "]
    
    tens = dict((tens[i].strip(),i) for i in range(len(tens)))
    
    multipliers = ["", "ten", "hundred", "thousand", "", "",  "million", "billion"]
    
    multipliers = dict((multipliers[i].strip() ,i) for i in range(len(multipliers)))
    
    print(multipliers, tens)
    
    str1 = "five hundred thousand"
    sol = Solution(ones, tens, multipliers)
    ans = sol.word2nums(str1)
    print (ans)