# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 21:37:03 2019

@author: Shubham
"""

import numpy as np

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CLL:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        if self.head is None:
            temp = Node(new_data)
            temp.next = temp
            self.head = temp
        
        curr = self.head
        temp = Node(new_data)
        if curr.data >= new_data:
            while curr.next != self.head:
                curr = curr.next
            curr.next = temp
            temp.next = self.head
            self.head = temp
        
        else:
            temp = Node(new_data)
            while(curr.next != self.head and curr.data <= new_data):
                curr = curr.next
            temp.next = curr.next
            curr.next = temp
    
    def printList(self):
        temp = self.head
        print(temp.data)
        temp = temp.next
        while (temp!=self.head):
            print(temp.data)
            temp = temp.next
        
arr = [12, 56, 2, 11, 1, 90] 
  
list_size = len(arr) 
  
# start with empty linked list 
start = CLL() 
  
# Create linked list from the array arr[] 
# Created linked list will be 1->2->11->12->56->90 
for i in range(list_size): 
    start.push(arr[i]) 
  
start.printList() 

def twoSum(arr, sum):
    s = set()
    for ele in arr:
        temp = sum - ele
        if temp in s:
            return True
        s.add(ele)
    return False

def isSafe(mat, visited, m, n, i, j):
    return not visited[i][j] and i >=0 and i < m and j >=0 and j < n and mat[i][j] == 1

def BFS(mat, start):
    n = len(mat)
    m = len(mat[0])
    neighbours = [(1, 0), (-1, 0), (-1, -1), (1, -1), (0, -1), (0, 1), (-1, 1), (1, 1)]
    visited = [[0 for i in range(m)] for i in range(n)]
    queue = []
    visited[start[0]][start[1]] = True
    ans = []
    queue.append(start)
    while len(queue) != 0:
        front = queue[0]
        queue.pop(0)
        ans.append(front)
        for neighbour in neighbours:
            x = front[0] + neighbour[0]
            y = front[1] + neighbour[1]
            next_coord = (x, y)
            if isSafe(mat, visited, n, m, next_coord[0], next_coord[1]):
                queue.append(next_coord)
                visited[next_coord[0]][next_coord[1]] = True
    return ans
            

def nearestNeighbors(numDestinations, allocations, numDeliveries):
    dist = list(map(lambda x: x[0]**2 + x[1]**2, allocations))
    dist_idx = np.argsort(dist)
    return np.array(allocations)[dist_idx][:numDeliveries]

def optimalDistance(maxTravelDist, forwardRouteDist, returnRouteDist):
    ans = []
    temp = -1
    for i in range(len(forwardRouteDist)):
        for j in range(len(returnRouteDist)):
            sum_dist = forwardRouteDist[i][1] + returnRouteDist[j][1]
            if sum_dist <= maxTravelDist:
                if temp > sum_dist:
                    temp = sum_dist
                    ans = []
                    ans.append([i+1, j+1])
                else:
                    ans.append([i + 1, j + 1])
    return ans

# assumption is that these arrays are sorted
def optDist(maxTr, fRD, rRD):
    n = len(fRD)
    m = len(rRD)
    i = 0; j = m - 1; t = -1
    ans = []
    while i < m or j >= 0:
        sum_d = fRD[i][1] + rRD[j][1]
        if sum_d <= maxTr and sum_d == t:
            ans.append([i+1, j+1])
            i += 1
            j -= 1
        elif sum_d <= maxTr and sum_d > t:
            ans = []
            ans.append([i+1, j+1])
            i += 1
        elif sum_d > maxTr:
            if i == n - 1 or j == 0:
                return ans
            j -= 1
        

def spiralPrint(A, m, n):
    k = 0;  l = 0
    while (k < m and l < n):
        for i in range(l, n):
            print(A[k][i], end = " ")
        k += 1
        
        for i in range(k, m):
            print(A[i][n-1], end = " ")
        n -= 1
        
        if k < m:
            for i in range(n - 1, l - 1, -1):
                print(A[m-1][i], end = " ")
            m -= 1
         
        if l < n:
            for i in range(m - 1, k - 1, -1):
                print(A[i][l], end = " ")
            l += 1
    
# Driver Code 
a = [ [1, 2, 3, 4, 5, 6], 
      [7, 8, 9, 10, 11, 12], 
      [13, 14, 15, 16, 17, 18],
      [13, 14, 15, 16, 17, 18],] 
        
R = 4; C = 6
spiralPrint(a, R, C) 
  
# This code is contributed by Nikita Tiwari. 
            
a= 7000; b =  [[1, 3000], [2, 5000], [3, 7000], [4, 10000]] ; c =[[1, 2000], [2, 3000], [3, 4000], [4, 5000]] 
print(optimalDistance(a,b,c))