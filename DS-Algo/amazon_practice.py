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
                if temp < sum_dist:
                    temp = sum_dist
                    ans = []
                    ans.append([i + 1, j + 1])
                elif temp == sum_dist:
                    ans.append([i + 1, j + 1])
    return ans
 
# O(n) solution               
def optDist(maxTr, fRD, rRD):
    n = len(fRD)
    m = len(rRD)
    i = 0; j = m - 1; t = -1
    ans = []
    while i < n or j > 0:
        print (i , j)
        sum_d = fRD[i][1] + rRD[j][1]
        if sum_d <= maxTr and sum_d == t:
            ans.append([i + 1, j + 1])
            i += 1 
        elif sum_d <= maxTr and sum_d > t:
            t = sum_d
            ans = []
            ans.append([i + 1, j + 1])
            i += 1
        elif sum_d > maxTr:
            if j == 0:
                return ans
            if j > 0:
                j -= 1
    return ans
            

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
    

def roundRotation(str1, str2):
    str1_new = str1 + str1
    if str2 in str1_new:
        return 1
    return -1

# Driver Code 
a = [ [1, 2, 3, 4, 5, 6], 
      [7, 8, 9, 10, 11, 12], 
      [13, 14, 15, 16, 17, 18],
      [13, 14, 15, 16, 17, 18],] 
        
R = 4; C = 6
spiralPrint(a, R, C) 
   
            
a= 7000; b = [[1,2000],[2,4000],[3,6000]]; c = [[1,2000]] 
print(optDist(a,b,c))

s = 'abc'; s1 = 'cab'
print(roundRotation(s, s1))

# memoized LIS implementation
def lis(A, n):
    L = [0]*n
    for i in range(n-1):
        L[i] = 1
        for j in range(i+1, n):
            if A[j] > A[i] and L[j] < L[i] + 1:
                L[j] = L[i] + 1
    
    return max(L)

class Solution:
    def isValid(self, s):
        if not s:
            return True
        mapping = {']':'[','}':'{',')':'('}
        stack = []
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            elif i in mapping:
                if mapping[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack) == 0
    

    
def heapify(A, n, i):
    largest = i
    r = 2 * i + 2
    l = 2 * i + 1
    if l < n and A[l] > A[largest]:
        largest = l
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)

def heapsort(A):
    n = len(A)
    for i in range(n, -1, -1):
        heapify(A, n, i)
    
    for i in range(n-1, -1, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0) 
        
def buildmaxHeap(A, n):
    for i in range(len(A)//2, -1, -1):
        heapify(A, n, i)
        
def reverseStr(string):
    string = list(string)
    i = 0
    n = len(string)
    j = n -1
    while i <= j:
        string[i], string[j] = string[j], string[i]
        i += 1
        j -= 1
    return ''.join(string)

# remove duplicates from an Array
def removeDuplicates(A):
    hashMap = {}
    for i, ele in enumerate(A):
        if hashMap.get(ele, 0) < 1:
            hashMap[ele] = 1
        else:
            A.pop(i)
    return A
    
def partition(A, st, end):
    i = st - 1
    x = A[end]
    for j in range(st, end):
        if A[j]  <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[end] = A[end], A[i+1]
    return i+1

def quicksort(A, st, end):
    if st <= end:
        p = partition(A, st, end)
        quicksort(A, st, p-1)
        quicksort(A, p+1, end)

# most frequent for one element
def mostFreq(A):
    n = len(A)
    st = 0; end = n-1
    quicksort(A, st, end)
    freq = {}
    ele = -1; maxcount = -1; c= 0
    for i in range(1, len(A)):
        if A[i] == A[i - 1]:
            c += 1
            if maxcount < c:
                maxcount = c
                ele = A[i]
                freq[ele] = c
        else:
            c = 0
    return ele, maxcount+1

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
# all permutations of the string
def permute(a, l, r):
    if l == r:
        print (''.join(a))
    else:
        for i in range(l, r + 1):
            a[i], a[l] = a[l], a[i]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtracking method
            

# frequency dictionary
def Freqdict(A):
    n = len(A)
    st = 0; end = n-1
    quicksort(A, st, end)
    freq = {}
    c= 1
    for i in range(0, len(A)):
        if A[i] == A[i - 1]:
            c += 1
            ele = A[i]
            freq[ele] = c
        else:
            c = 1
            ele = A[i]
            freq[ele] = c
    return freq
        
sol = Solution()
print (sol.isValid('{[(())()]}'))