# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 10:49:38 2018

@author: Shubham
"""
import re
import operator

class Solution:
    
    def mostCommonWord(self, paragraph, banned):
        paragraph = re.sub(r'[^\w\s]','',paragraph)
        paragraph.lower()
        word_list = paragraph.split()
        freq_dict = {i:word_list.count(i) for i in set(word_list)}
        freq_dict_sorted = sorted(freq_dict.items(), key = operator.itemgetter(1), reverse = True)
        for ele in freq_dict_sorted:
            if ele[0] in banned:
                continue
            ans = ele[0]
            return ans
        
if __name__ == "__main__":
    
    sol = Solution()
    str1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    ans = sol.mostCommonWord(str1, banned)
    print (ans)