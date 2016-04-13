# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:05:24 2016

@author: Administrator
"""
import time

def selectSort(arr):
    #选择排序，最坏为O(n^2)
    #升序排列一个数组，降序排列将while语句中改为arr[i]<key即可
    if(arr==None or len(arr)<2):
        return arr
    for j in range(len(arr)):
        
        index = j
        for i in range(j,len(arr)):
            if arr[i] < arr[index]:
                index = i#找出剩余的最小元素
                
        #未排序中最小的元素跟arr[j]交换
        tmp = arr[j]
        arr[j] = arr[index]
        arr[index] = tmp
        
    return arr

arr = [1,4,7,3,2,5,6]
print(selectSort(arr))
arr = range(10000)
start = time.time()
selectSort(arr)
print(time.time() - start)