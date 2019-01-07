# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 13:08:08 2018

@author: Shubham
"""

import numpy as np

class Solution:
    # A is a numpy adjacency matrix
    # visited is a list of visited nodes
    def dfs(self, A, visited, i):
        stack = []
        stack.append(i)
        visited[i] = 1
        while stack is not None:
            top = stack.pop()
            for j in range(len(A[top,:])):
                if j not in visited and A[top][j]:
                    stack.append(j)
        return stack
        
    # eqn is an adjacency matrix format
    def validEquations(self, eqn, node_list):
        l = len(eqn)
        for i in node_list:
            
            
        