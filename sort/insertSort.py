# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:05:24 2016

@author: Administrator
"""
import time

def insertSort(arr):
    #插入排序，最坏为O(n^2)，最好为O(n)
    #升序排列一个数组，降序排列将while语句中改为arr[i]<key即可
    if(arr==None or len(arr)<2):
        return arr
    for j in range(1,len(arr)):
        key = arr[j]#待插入的数
        i = j-1
        while(i>=0 and arr[i]>key):
            #从后往前比较待插入的数和当前数，将arr[j-1]、arr[j-2]...向右移动直到找到arr[j]的适当位置
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key#遍历完将arr[j]插入到该位置
    return arr


arr = [9,4,8,6,1,2,3,7,5]
insertSort(arr)
print(arr)
arr = range(10000,0,-1)
start = time.time()
insertSort(arr)
print(time.time()-start) 
    