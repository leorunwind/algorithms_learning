# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:05:24 2016

@author: Administrator
"""
import time

def shellSort(arr):
    #改进版的插入排序-希尔排序，最坏为O(n^2)，最好为O(n)，平均为O(n^1.3)
    gap = len(arr)/2
    while gap > 0:
        
        for i in range(gap,len(arr)):
            if arr[i] < arr[i-gap]:#后面的元素比前面的小，以gap为步长进行插入排序
                key = arr[i]
                j = i - gap
                while j>=0 and arr[j]>key:
                    arr[j+gap] = arr[j]
                    j -= gap
                arr[j+gap] = key
        #步长减一半     
        gap /= 2

    return arr


arr = [9,4,8,6,1,2,3,7,5]
shellSort(arr)
print(arr)
arr = range(100000,0,-1)
start = time.time()
shellSort(arr)
print(time.time()-start) 
    