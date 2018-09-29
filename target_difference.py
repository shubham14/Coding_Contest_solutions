# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 10:12:55 2018

@author: Shubham
"""


# Python program to find if there are 
# two elements wtih given sum 
  
# function to check for the given sum 
# in the array 

def cutSticks(lengths):
    count_sticks = []
    while len(lengths) != 0:
        count_sticks.append(len(lengths))
        m = min(lengths)
        lengths =list(map(lambda x: x - m, lengths))
        lengths = list(filter(lambda x: x != 0, lengths))
    return count_sticks
    
def kDifference(a, k):  
    
    s = set() 
    count = 0  
    for i in range(len(a)): 
        temp = a[i] - k
        if (temp>=0 and temp in s): 
            count += 1
            s.add(a[i])
        else:
            s.add(a[i])
    return count
  
def kDifference1(a, k):
    c = dict()
    count = 0
    for ele in a:
        if ele in list(c.keys()):
            c[ele] += 1
        else:
            c[ele] = 1
            
    for i in range(len(a)):
        temp = a[i] - k
        if temp >= 0 and temp in c.keys():
            count += min(c[temp], c[a[i]])
    return count

def kDifference2(a, k):
    c = 0
    for ele in a:
        a =list(map(lambda x: x - ele, a))
        print('Here')
        c += len(list(filter(lambda x: x == abs(2), a)))
        a = list(filter(lambda x: x != abs(2), a))
    return c
        

# driver program to check the above function 
A = [1,5,3,4,2]
B = [5,4,4,2,2,8]
k = 1
ans = kDifference2(A, k)

ans1 = cutSticks(B)
print(ans1)