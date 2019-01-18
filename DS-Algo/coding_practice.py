# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 17:10:32 2019

@author: Shubham
"""

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def interleavingStrings(str1, str2, str3):
    '''
    str1 and str2 are the input strings
    str3 is the resultant strings
    '''
    m = len(str1); n = len(str2)
    DP = [[0] * len(n) + 1] * len(m) + 1
    
    if m + n != len(str3):
        return False
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                DP[i][j] = True
            if j == 0 and str1[i-1] == str3[i-1]:
                DP[i][j] = DP[i-1][j]
            if i == 0 and str2[j-1] == str3[j-1]:
                DP[i][j] = DP[i][j-1]
            else:
                if str1[i] == str3[i+j-1] and str2[j] != str3[i+j-1]:
                    DP[i][j] = DP[i-1][j]
                if str1[i] != str3[i+j-1] and str2[j] == str3[i+j-1]:
                    DP[i][j] = DP[i][j-1]
                if str1[i-1] == str3[i+j-1] and str2[j] == str3[i+j-1]:
                    DP[i][j] == DP[i-1][j] or DP[i][j-1]
    return DP[m][n]

class Solution1:
    def AmazonAircraft(self, forward, ret, maxValue):
        n = len(forward)
        m = len(ret)
        i = 0; j = m-1; ans = []
        temp = -1
        while i < n and j >= 0:
            print (i , j)
            sumVal = forward[i][1] + ret[j][1]
            if temp < sumVal and sumVal <= maxValue:
                ans = []
                temp = sumVal
                ans.append([i+1, j+1])
                i += 1
            elif temp == sumVal and sumVal <= maxValue:
                ans.append([i+1, j+1])
                i += 1
            elif sumVal > maxValue:
                j -= 1
        return ans
        

def closestsum(forward, rev, target):
    n = len(forward)
    m = len(rev)
    i = 0; j = m - 1
    ans = []
    temp = 10000000
    while i < n and j >=0:
        sumPair = forward[i] + rev[j]
        if temp > abs(sumPair-target):
            ans = []
            temp = abs(sumPair-target)
            ans.append([i + 1, j + 1])
            i += 1
        elif temp == abs(sumPair-target):
            ans.append([i + 1, j + 1])
            i += 1
        else:
            j -= 1
    return ans

class Solution:
    def binarySearch(self, A, l, r, x):
        if l > r:
            mid = int((r - l)/2 + l)
            if x > A[mid]:
                return (mid-1, mid)
            else:
                return (mid-1, mid)
        else:
            mid = int((r - l)/2 + l)
            if x == A[mid]:
                return (mid, mid)
            elif x > A[mid]:
                return self.binarySearch(A, mid+1, r, x)
            else:
                return self.binarySearch(A, l, mid-1, x)
            
    def findClosestElements(self, arr, k, x):
        ans = []
        n = len(arr)
        l,r = self.binarySearch(arr, 0, n-1, x)
        if l == -1:
            l = 0
        if r == n:
            r = n-1
        c = 0
        while c < k:
            print (l, r)
            if x - arr[l] >= arr[r] - x:
                ans.append(arr[l])
                l -= 1
                c += 1
            elif x - arr[l] < arr[r] - x:
                ans.append(arr[r])
                r += 1
                c += 1
            elif l < 0:
                r += 1
                c += 1
            elif r > n-1:
                l -= 1
                c += 1
            else:
                c += 1
        return ans
    
    def kClosest(self, points, K):
        l = list(map(lambda x: x[0]**2 + x[1]**2, points))
        d = dict(zip(points, l))
        sorted_by_value = sorted(d.items(), key=lambda kv: kv[1])
        k = sorted_by_value.keys()[:K]
        return k
    
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
            while curr.next != self.head:
                curr = curr.next
            curr.next = temp
            temp.next = self.head
            self.head = temp
        
        else:
            temp = Node(new_data)
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

def twoSum(A, sum):
    s = set()
    for ele in A:
        temp = sum - ele
        if temp in s:
            return True
        s.add(ele)
    return False

def threeSum(arr):
    for i in range(len(arr)):
        t = -arr[i]
        s = set()
        for j in range(i+1, len(arr)):
            temp = t - arr[j]
            if temp in s:
                return True
            else:
                s.add(arr[j])
    return False
            
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

def preorderStack(root):
    if root is None:
        return 
    else:
        stack = []
        stack.append(root)
        while stack:
            top = stack[0]
            stack.pop(0)
            if top.left:
                stack.append(top.left)
            print(top.val)
            if top.right:
                stack.append(top.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def permute(a, l, r):
    a = list(a)
    if l == r:
        print (''.join(a))
    for i in range(l, r+1):
        a[l], a[i] = a[i], a[l]
        permute(a, l+1, r)
        a[l], a[i] = a[i], a[l]

def revLL(head):
    prev = None
    curr = head
    while curr is not None:
        next1 = curr.next
        curr.next = prev
        prev = curr
        curr = next1
    head = prev
    return head

def reverseSecondHalf(head):
    slow = head
    temp = head
    fast = head
    while fast.next is not None and slow.next is not None:
        fast = fast.next.next
        slow = slow.next
        slow = temp.next
    temp.next = reverse(slow)
    return head
    
def levelOrderTraversal(root):
    if root is None:
        return []
    queue = []
    ans = []
    queue.append(root)
    while queue:
        n = len(queue)
        for i in range(n):
            t = queue[0]
            queue.pop(0)
            ans.append(t.val)
            if t.left is not None:
                queue.append(t.left)
            if t.right is not None:
                queue.append(t.right)
    return ans

def AmazonFresh(numDest, alloc, numDeli):
    dist = list(map(lambda x: x[0]**2 + x[1]**2, alloc))
    z = dict(zip(dist, alloc))
    z1 = dict(sorted(z.items(), key=lambda kv: kv[0]))
    return list(z1.values())[:numDeli]

def numberTri(arr):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(0, n-2):
        k = i+2
        for j in range(i+1, n):
            while k < n and arr[i] + arr[j] > arr[k]:
                k += 1
            if k > j:
                count += k - j - 1
    return count

def formSumMatrix(A):
    n = len(A); m = len(A[0])
    dp = [[0] * m] * n
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = A[i][j]
            elif i == 0 and j != 0:
                dp[i][j] = A[i][j] + dp[i][j-1]
            elif i !=0 and j == 0:
                dp[i][j] = A[i][j] + dp[i-1][j]
            elif i != 0 and j != 0:
                dp[i][j] = A[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
    return dp

def sumMat(A):
    n = len(A); m = len(A[0])
    dp = [[0] * m] * n
    dp[0][0] = A[0][0]
    for i in range(1, len(A)):
        dp[i][0] = A[i][0] + dp[i-1][0]
    for i in range(1, len(A[0])):
        dp[0][i] = A[0][i] + dp[0][i-1]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = A[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
    return dp
        
def revSpeChar(str1):
    str1 = list(str1)
    n = len(str1)
    i = 0; j = n - 1
    while i <= j:
        if not str1[i].isalpha():
            i += 1
        elif not str1[j].isalpha():
            j -= 1
        else:
            str1[i], str1[j] = str1[j], str1[i]
            i += 1
            j -= 1
    return ''.join(str1)

def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    head = new_node
    return head

def reverseUtil(head, curr, prev):
    if curr.next is None:
        head = curr
        curr.next = prev
        return head
    next = curr.next
    curr.next = prev
    head = reverseUtil(head, next, curr)
    return head

def reverse(head):
    if head is None:
        return None
    head = reverseUtil(head, head, None)
    return head

def printList(head):
    temp = head
    while(temp):
        print (temp.data)
        temp = temp.next
        
head = Node(1)
head = push(head, 2)
head = push(head, 5)
head = push(head, 3)

print ('--- Original List ---')
printList(head)

print ('--- Reversed List ---')
h = reverse(head)
printList(h)

def completeNode(root):
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return True
    return False

def widthOfBinaryTree(root):
    if root is None:
        return 0
    queue = []
    queue.append(root)
    while queue:
        count_comp = 0; count_incomp = 0
        n = len(queue)
        for i in range(n):
            front = queue[0]
            queue.pop(0)
            if completeNode(front):
                count_comp += 1
            if not completeNode(front):
                count_incomp += 1
            if front.left is not None:
                queue.append(front.left)
            if front.right is not None:
                queue.front(front.right)
    
    return 2 * (count_comp + count_incomp)       