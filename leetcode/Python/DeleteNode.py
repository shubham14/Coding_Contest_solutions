import numpy as np
import math

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # x is the node value 
    def deleteLinkedList(self, node):
        while node.next is not None:
            node.val = node.next.val
            if node.next.next is not None:
                node=node.next
            else:
                node.next=None
                break

    def productExceptSelf(self, nums):
        l = len(nums)
        