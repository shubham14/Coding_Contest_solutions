# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:04:22 2018

@author: Shubham
"""

def addBinaryString(a, b):
    if len(a) < len(b):
        a, b = b, a  
    a_rev = ''.join(reversed(a))
    d = len(a)-len(b)
    b_rev = ''.join(reversed(b))
    z = ['0'] * d        
    b_rev = b_rev + ''.join(z)
    sum_ans = ''
    carry = 0
    for i in range(len(a_rev)):
        if (a_rev[i] == '1' and b_rev[i] == '0' or (a_rev[i] == '0' and b_rev[i] == '1')) and carry == 0:
            sum_ans += '1'
            carry = 0
            print(sum_ans, 1)
        elif (a_rev[i] == '1' and b_rev[i] == '0' or (a_rev[i] == '0' and b_rev[i] == '1')) and carry == 1:
            sum_ans += '0' 
            carry = 1
            print(sum_ans, 2)
        elif a_rev[i] == '0' and b_rev[i] == '0' and carry == 0:
            sum_ans += '0'
            carry = 0
            print(sum_ans, 3)
        elif a_rev[i] == '0' and b_rev[i] == '0' and carry == 1:
            sum_ans += '1'
            carry = 0
            print(sum_ans, 4)
        elif a_rev[i] == '1' and b_rev[i] == '1' and carry == 0:
            sum_ans += '0'
            carry = 1
            print(sum_ans, 5)
        elif a_rev[i] == '1' and b_rev[i] == '1' and carry == 1:
            sum_ans += '1'
            carry = 1
            print(sum_ans, 6)
    print (i)        
    if i == len(a_rev) - 1:
        if carry == 1:
            print("Here")
            sum_ans += '1'
            
    return ''.join(reversed(sum_ans)), a_rev, b_rev