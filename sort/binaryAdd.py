# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:17:21 2016

@author: Administrator
"""
def binaryAdd(arr1,arr2):
    if(len(arr1)!=len(arr2) or len(arr1)<1):
        return 'invalid input array!'
    arr = []
    carry = 0
    for i in range(len(arr1)):
        val = arr1[i]+arr2[i]+carry
        if(val > 1):
            arr.append(val-2)
            carry = 1
        else:
            arr.append(val)
            carry = 0
            
    arr.append(carry)
    return arr

arr1 = [0,1,1,1]
arr2 = [1,0,1,1]
add_res = binaryAdd(arr1,arr2)
print(add_res)