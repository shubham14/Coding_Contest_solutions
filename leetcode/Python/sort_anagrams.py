# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:45:20 2018

@author: Shubham
"""

import numpy as np

class Solution:
    def sortAnagrams(self, str_list):
        str_list = map(lambda(x: sorted(x), str_list))
        ind_sort = np.argsort(list(str_list))
        ans = list(np.array(str_list)[ind_sort])
        return ans