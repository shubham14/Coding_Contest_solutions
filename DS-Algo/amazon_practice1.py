import numpy as np

def longestPalindrome(string):
    n = len(string)
    dp = [[False] * n] * (n)
    maxLength = 1
    start = 0 
    
    for i in range(n):
        dp[i][i] = True
        maxLength = 1
        start = i

    for i in range(n-1):
        if string[i] == string[i+1]:
            maxLength = 2
            start = i
    
    k = 3
    for k in range(n):
        for i in range(n - k + 1):
            j = i + k - 1
            if string[i] == string[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if maxLength < k:
                    maxLength = k
                    start = i
    return maxLength, string[start : start + maxLength]

def kClosestPoints(points, k):
    dist = list(map(lambda x: x[0] ** 2, x[1] ** 2, points))
    d = dict(zip(points, dist))
    d1 = dict(sorted(d, lambda key: key[1]))
    return list(d1.keys())[:k]

def sortedSum(arr1, arr2, sum):
    n = len(arr1)
    m = len(arr2)
    i = 0
    j = m - 1
    ans = []
    temp = -100
    while i < n and j >= 0:
        sum1 = arr1[i] + arr2[j]
        if sum1 > temp and sum1 < sum:
            ans = []
            ans.append([i + 1, j + 1])
            temp = sum1
            i += 1
        elif sum1 == temp and sum1 < sum:
            ans.append([i + 1, j + 1])
            i += 1
        elif sum1 > sum:
            j -= 1
    return ans

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        temp = Node(new_data)
        if self.head is None:
            temp.next = temp
            self.head = temp
        
        if new_data < self.head.val:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = temp
            temp.next = self.head
            self.head = temp
        
        else:
            curr = self.head
            while curr.next != self.head and curr.val < new_data:
                curr = curr.next
            curr.next = temp.next
            curr.next = temp
    
    def printList(self):
        curr = self.head
        while curr != curr.next:
            print (curr.val)
            curr = curr.next
    
class RandomNode:
    def __init__(self, label):
        self.label = label
        self.random = None
        self.next = None

class LL:
    def __init__(self):
        self.visited = {}
        self.head = None

    def copyRandomList(self, head):
        if head is None:
            return None
        if head in self.visited:
            return self.visited[head]
        node = RandomNode(head.label)
        self.visited[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node

# points are in the following format
# [tlx tly, brx, bry]
def overlapArea(points1, points2):
    x1 = max(points1[0], points2[0])
    x2 = min(points1[2], points2[2])
    y1 = max(points1[1], points2[1])
    y2 = min(points1[3], points2[3])

    if x1 >= x2 or y1 >= y2:
        return 0
    return (x2 - x1) * (y2 - y1)

def validParanthesis(string):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for ch in string:
        if ch in ['{', '[', '(']:
            stack.append(ch)
        elif ch in mapping and stack[-1] == mapping[ch]:
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0

def twoSum(arr, sum):
    s = set()
    ans = []
    for ele in arr:
        temp = sum - ele
        if temp in s:
            if sorted([ele, temp]) in ans:
                ans.append(sorted([ele, temp]))
        s.add(ele)
    return ans

def threeSum(arr):
    ans = []
    for ele in arr:
        sum = -ele
        s = set()
        for ele1 in arr:
            temp = sum - ele1
            if sorted([ele, ele1, temp]) in ans:
                ans.append(sorted([sum, ele1, temp]))
            else:
                s.add(ele1)
    return ans

def rotateMatrix(mat):
    N = len(mat)
    for i in range(n//2):
        for j in range(N-i-1):
            temp = mat[i][j]
            mat[i][j] = mat[N-j-1][i]
            mat[N-j-1][i] = mat[N-i-1][N-j-1]
            mat[N-i-1][N-j-1] = mat[j][N-1-i]
            mat[j][N-1-j] = temp
    return temp

def clubAnagrams(strings):
    d = dict()
    for string in strings:
        str1 = ''.join(sorted(string))
        if str1 not in d:
            d[str1] = [string]
        else:
            d[str1].append(string)
    return list(d.values())

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

