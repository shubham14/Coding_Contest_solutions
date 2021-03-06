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
        curr = self.head
        temp = Node(new_data)
        if self.head is None:
            temp = Node(new_data)
            temp.next = temp
            self.head = temp
        
        elif curr.data >= new_data:
            print(new_data)
            while curr.next != self.head:
                curr = curr.next
            curr.next = temp
            temp.next = self.head
            self.head = temp
        
        else:
            temp = Node(new_data)
            print(new_data)
            while(curr.next != self.head and curr.next.data <= new_data):
                curr = curr.next
            temp.next = curr.next
            curr.next = temp
    
    def printList(self):
        temp = self.head
        while (temp.next!=self.head):
            print(temp.data)
            temp = temp.next
        print(temp.data)

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
            return True, 0
        c = 0
        mapping = {']':'[','}':'{',')':'('}
        stack = []
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            elif i in mapping:
                if mapping[i] == stack[-1]:
                    stack.pop()
                    c += 1
                else:
                    stack.append(i)
        return len(stack) == 0, c

# # point1 and point2 are quartets of points    
# def overlapRectangleArea(point1, point2):


    
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
        
def waysToDecode(string):
    n = len(string)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        if ord(chr(int(string[i-2] + string[i-1]) + 65)) in range(65, 91):
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]
    return dp[n]

def reorderList(head):
    h= head
    slow = head
    fast = head
    while slow and fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    return h, slow

def reverseList(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head

def printList(head):
    temp = head
    while (temp.next != None):
        print(temp.data)
        temp = temp.next
    print(temp.data)
    if temp.next is None:
        print ("None")

def combineReorder(head, head1):
#    c = head
#    c1 = head1
#    while c:
#        print(c.data)
#        c1.next = c.next
#        c.next = c1
#        c = c.next.next
#        c1 = c1.next
#    c.next = c1
#    return head
    head.next = head1
    return head

def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    head = new_node
    return head


def reverseSecondHalf(head):
    head1 = head
    if head is None:
        return None
    slow = fast = head1
    c = 0
    
    while slow.next and fast and fast.next:
        new_prev = slow
        slow = slow.next
        fast = fast.next.next
        c += 1
    curr, prev = slow, None
    tail, con = curr, new_prev
    while c+1:
        next = curr.next
        curr.next = new_prev
        new_prev = curr
        curr = next
        c -= 1
    
    head1 = new_prev
    tail.next = curr
    return head1


def reverseLL(head):
    curr = head
    prev = None
    while curr:
        next1 = curr.next
        curr.next = prev
        prev = curr
        curr = next1
    head = prev
    return head

#def reverseSecondHalf(head):
#    slow = head
#    temp = head
#    fast = head
#    while fast.next is not None and slow.next is not None:
#        temp = slow
#        fast = fast.next.next
#        slow = slow.next
#    temp.next = reverseLL(slow)
#    return head

head = Node(1)
head = push(head, 2)
head = push(head, 5)
head = push(head, 3)
head = push(head, 6)
head = push(head, 7)
head = push(head, 6)

h_second_half = reverseSecondHalf(head)

printList(head)
print('------------------')
printList(h_second_half)
print('------------------')

        
def binaryTreeTraversal(root):
    queue = []
    ans = []
    if root is None:
        return []
    queue.append(root)
    while queue:
        n = len(queue)
        for i in range(n):
            front = queue.pop(0)
            ans.append(front.val)
        if front.left:
            queue.append(front.left)
        if front.right:
            queue.append(front.right)