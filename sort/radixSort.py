# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:05:24 2016

@author: Administrator
"""
import time

def cntDigit(arr,radix):
    #获取数组元素的最大位数
    maxnum = arr[0]
    for x in arr:
        if x > maxnum:
            maxnum = x
    
    cnt = 0
    while(maxnum != 0):
        maxnum /= radix
        cnt += 1
    return cnt

def radixSort(arr,radix=10):
    k = cntDigit(arr,radix)#获取最大位数
    bucket = [[] for i in range(radix)]
    for i in range(1,k+1):
        for j in arr:
            #bucket[x]存储从低到高第i位为x的数，如数组中的543，i=1时存在bucket[3]里
            bucket[j/(radix**(i-1)) % (radix)].append(j)
        del arr[:]#先初始化arr
        #print(bucket)
        for z in bucket:#当前位数的数组按顺序放入arr中
            arr += z
            del z[:]
    return arr
    
    
arr = [16,341,9,254,543,1011]
print(radixSort(arr))

start = time.time()
arr = range(100000,0,-1)
quickSort(arr,0,len(arr)-1)
print(time.time()-start)