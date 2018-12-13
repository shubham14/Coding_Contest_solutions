import numpy as np

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
        d_new = {}
        for ele in sent:
            for ele1 in d:
                