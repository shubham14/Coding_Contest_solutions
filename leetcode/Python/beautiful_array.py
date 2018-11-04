# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:37:39 2018

@author: Shubham
"""

from collections import deque

class Solution:
    def beautifulArray(self, N):
        arr = [i for i in range(1, N+1)]
        for i in range(0, len(arr), 2):
            if i < len(arr)-1:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        return arr
    
    def minDepth(self, root):
        if not root:
            return 0
        else:
            node_deque = deque([(1, root)])
        
        # Adopted BFS approach
        while node_deque:
            depth, root = node_deque.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth+1, c))
    
if __name__ == "__main__":
    sol = Solution()
    ans = sol.beautifulArray(5)
    print (ans)