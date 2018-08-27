# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 20:54:41 2018

@author: Shubham
"""

# Jarvis-March algorithm for Convex-Hull problem

# point class definition
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
class Solution:
    # A, B, C are point members
    def direction(self, A, B, C):
        B.x -= A.x
        B.y -= A.y
        C.x -= A.x
        C.y -= A.y
        
        # cross product definition
        cross_prod = B.x * C.y - B.y * C.x
        
        if cross_prod > 0:
            direc = "RIGHT"
        elif cross_prod < 0:
            direc = "LEFT"
        else:
            direc = "COLLINEAR"
        return direc
    
    # points is a list of Point objects
    def Convex_Hull(self, points):
        collinear = []
        stack = []
        flag = True
        i = 0
        # sort according to x-axis to find the left most points
        min_x = 0
        start = 0
        for i in range(len(points)):
            if min_x > points[i].x:
                min_x = points[i].x
                start = i
        i = 0
        stack.append(points[start])
        while flag:
            mark_col = 0
            first = start
            second = (start + 1) % n
            for i in range(len(points)):
                if self.direction(points[start], points[second], points[i]) == "LEFT":
                    second = i
                elif self.direction(points[start], points[second], points[i]) == "COLLINEAR" and i != second:
                    collinear.append(i)
                    second = i
                    mark_col = 1
            if mark_col == 0:
                first = second
                stack.append(first)
            else:
                first = collinear.pop()
                stack.append(first)
                stack.append(second)
                
            # break loop if cycle has been completed
            if first == start:
                flag = False
                
        return len(stack)  