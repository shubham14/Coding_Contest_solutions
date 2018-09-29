# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 15:09:43 2018

@author: Shubham
"""

# longest common substring
import numpy as np
import pandas as pd
from collections import defaultdict
import pandas as pd
import numpy.linalg as LA

class Solution:
    def LCS(self, a, b):
        m = len(a); n = len(b)
        DP = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    DP[i][j] = 0
                elif a[i-1] == b[j-1]:
                    DP[i][j] = 1 + DP[i-1][j-1]
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        return DP[m][n]
    
    def maxSubArraySum(self, A):
        curr_sum = A[0]
        max_so_far = A[0]
        for i in range(len(A)):
            curr_sum= max(curr_sum, curr_sum + A[i])
            max_so_far = max(curr_sum, max_so_far)
        return max_so_far
    
    # here A is a 2D matrix
    # where all elements are positive
    def kadane2D(self, A):
        col = len(A)
        row = len(A[0])
        maxSum = -1
        for i in range(0, col):
            temp = []
            for j in range(i, col):
                sum1 = 0
                for z in range(row):
                    sum1 += M[i][j]
                
    def includeEle(self, A, sum1):
        for i in range(len(A)):
            if (sum1 - A[i]) >= 0:
                sum1 = sum1 - A[i]
                print (A[i])        

# graphnode has neighbors which are also graphnodes
class GraphNode:
    def __init__(self, val, neighbors):
        self.neighbors = []
        self.val = val O
  
# add all the graph related things here      
class Graph:
    # G is an adjacency list representation
    def __init__(self, V):
        self.V = V
    
    def BFS(self):
        visited = [0] * self.V
        for i in range(self.V):
            queue = []
            visited[i] = 1
            for node in self.V[i].neighbors:
                queue.append(node)
                temp = queue[0]
                while len(queue) != 0:
                    t = queue.pop(0)    
                    for child in t.neighbors:
                        queue.append(child)
                        if !visited[t.val]:
                            visited[t.val] = 1

class KMeans:
    # data is a pd dataframe
    def __init__(self, data, K, tol):
        self.data = data
        self.K = K
        self.tol = tol
        self.centers = []
    
    def dist(self, a, b):
        return np.linalg.norm(a-b)
    
    def fit(self):
        clusters = defaultdict(list)
        C_x = np.random.randint(0, np.max(X)-20, size=self.K)
        C_y = np.random.randint(0, np.max(X)-20, size=self.K)
        C = np.array(list(zip(C_x, C_y)))
        cluster_idx = [i for i in range(self.K)]
        for i in range(self.K):
            clusters[i].append(C[i])
        # intialize all data points to the nearest cluster
        asso = []
        prev_centers = C
        error = 100000
        while np.abs(error) > tol:
            for ele in self.data:
                min_idx_list = list(np.argsort(list(map(lambda x: self.dist(x, ele), C))))
                min_idx = min_idx_list.index(0)
                clusters[min_idx].append(ele)
                next_centers = []
                for ele in list(clusters.key()):
                    next_clusters.append(sum(clusters[ele]) / len(clusters[ele]))
                
                # measure change in centroid positions through L2-norm
                error = LA.norm(prev_clusters-next_clusters)
                
                # change cluster positions 
                prev_clusters = next_clusters
    
    # predicting cluster
    def predict(self, data_point):
        l = self.clusters
        ans_list = list(np.argsort(list(map(lambda x: LA.norm(x-data_point), l))))
        ans = min_idx_list.index(0)
        return ans
            
        
    
if __name__ == "__main__":
    str1 = "AGGTAB"; 
    str2 = "GXTXAYB";
    sol = Solution()
    ans = sol.LCS(str1, str2)
    print (ans
           
    A = [1, 2, 3, 5, 3]
    sum1 = 10
    sol = Solution()
    sol.includeEle(A, sum1)