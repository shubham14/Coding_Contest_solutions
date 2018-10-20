# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 14:18:18 2018

@author: Shubham
"""

import ast
import sys
import json
from collections import defaultdict

class Solution:
    # d is the defaultdict
    def __init__(self, d):
        self.d = d
        
    def convert_to_dict(self, str_dict):
        str_dict = str_dict.split()
        if 'add' == str_dict[0]:
            d_bw = json.loads(str_dict[1])
            self.d[int(d_bw['id'])] = d_bw
            
    def convert_stdin(self):
        for line in sys.stdin:
            self.convert_to_dict(line)

if __name__ == "__main__":
    sys.stdout.write('add {"id":1,"last":"Doe","first":"John","location":{"city":"Oakland","state":"CA","postalCode":"94607"},"active":true}\n'
                     'add {"id":2,"last":"Doe","first":"Jane","location":{"city":"San Francisco","state":"CA","postalCode":"94105"},"active":true}\n'
                     'add {"id":3,"last":"Black","first":"Jim","location":{"city":"Spokane","state":"WA","postalCode":"99207"},"active":true}\n'
                     'add {"id":4,"last":"Frost","first":"Jack","location":{"city":"Seattle","state":"WA","postalCode":"98204"},"active":false}\n'
                     'get {"location":{"state":"WA"},"active":true}\n'
                     'get {"id":1}')

#    l = []
#    for line in sys.stdin.readline():
#        l.append(line)
#    
#    d = defaultdict(int)
#    s = Solution(d)
#    s.convert_stdin()