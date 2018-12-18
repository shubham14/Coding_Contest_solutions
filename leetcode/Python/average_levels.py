import numpy as np
from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def averageOfLevels(self, root):
        avg = []
        if root == NULL:
            return [0]
        else:
            avg.append(root.val)

    def replaceWords(self, d, sentence):
        sent = sentence.split()
        d_new = defaultdict(list)
        def minLen(d, key):
            v = list(map(lambda x: len(x), d[key]))
            return v.index(min(v))

        for ele in sent:
            for ele1 in d:
                if ele1 in ele:
                    d_new[ele].append(ele1)
        l_ans = []
        for ele in sent:
            if ele in list(d_new.keys()): 
                l_ans.append(minLen(d_new))
            else:
                l_ans.append(ele)
        return ' '.join(l_ans)
        
    def sec_min(self, root):
        
        

