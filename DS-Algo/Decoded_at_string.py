# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 16:55:27 2018

@author: Shubham
"""

import numpy as np
from collections import defaultdict

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    s = s+'*'
    s_list = s.split(' ')
    if len(s_list) == 1:
        return len(s)
    return len(s_list[-1])

def groupAnagrams(strs):
    d = defaultdict(list)
    for ele in strs:
        key = ''.join(sorted(ele))
        d[key].append(ele)
        
    return list(d.values())