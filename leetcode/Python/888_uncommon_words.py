# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 11:40:24 2018

@author: Shubham
"""

from collections import defaultdict

class Solution:
    def words_list(self, str1, str2):
        str1 = str1.strip()
        str2 = str2.strip()
        l1 = str1.split(' ')
        l2 = str2.split(' ')
        d = defaultdict(int)
        for ele in l1:
            d[ele] += 1
        for ele in l2:
            d[ele] += 1
        
        ans = []
        for ele in d.keys():
            if d[ele] == 1:
                ans.append(ele)
        
        return ans
    
if __name__ == "__main__":
    A ="this apple is sweet"
    B = "this apple is sour"
    sol = Solution()
    ans = sol.words_list(A, B)
    print(ans)