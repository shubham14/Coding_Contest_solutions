# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 12:02:18 2018
merge intervals
@author: Shubham
"""

import numpy as np
import operator
import functools

class Interval:
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e
           
class Solution:
    def merge(self, intervals):
        ans = []
        sorted(intervals, key=lambda x: x.start)
        start = intervals[0].start
        end = intervals[0].end
        for i in range(1, len(intervals)):
            if end > intervals[i].start:
                end = max(end, intervals[i].end)
            else:
                ans.append(Interval(start, end))
                start = intervals[i].start
                end = intervals[i].end
        ans.append(Intervals(s, e))
        return ans