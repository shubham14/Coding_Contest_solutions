# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:26:06 2018

@author: Shubham
"""

import numpy as np
from collections import defaultdict
from queue import LifoQueue

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
   
# BFS approach to check acyclicity     
class Solution:
    def solve(self, A, B, C):
        G = defaultdict(list)
        for a, b in zip(B, C):
            G[a].append(b)
        C = {}
        K = 1
        for i in range(1, A+1):
            if i not in C:
                Visited = defaultdict(bool)
                S = LifoQueue()
                S.put(i)
                Visited[i] = True
                while not S.empty():
                    n = S.get()
                    for neighbour in G[n]:
                        if Visited[neighbour]:
                            return 0
                        else:
                            Visited[neighbour] = True
                            S.put(neighbour)
                    C[n] = K
                    K += 1
        return 1

# union find appraoch to check acyclicity
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])
    
    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set
        
    def isCyclic(self):
        
        parent = [-1] * self.V
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)
        return False