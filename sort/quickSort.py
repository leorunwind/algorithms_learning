# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:05:24 2016

@author: Administrator
"""
import time
import random

def quickSort(arr,low,high):
    #随机选择基准元素的快速排序，达到期望时间复杂度O(nlgn)
    #注意high是最大下标
    if low < high:
        mid = getPartition(arr,low,high)
        #对基准元素两边的数组快排
        quickSort(arr,low,mid-1)
        quickSort(arr,mid+1,high)
        
def getPartition(arr,low,high):
    #随机选择一个数并与arr[high]交换，防止最坏情况
    #将arr[high]作为基准进行排序，使得基准左边的元素都比它小，右边的元素都比它大
    rand = random.randint(low,high)
    arr[high],arr[rand] = arr[rand],arr[high]
    
    index = low - 1
    for i in range(low,high):
        if arr[i] <= arr[high]:#保证index前面的数都比key小,降序排列则把这一行改为if arr>=key
            index += 1
            arr[index],arr[i] = arr[i],arr[index]
    arr[index+1],arr[high] = arr[high],arr[index+1]
    
    return index+1

arr= [1,3,2,4,9,8,11,7,6,5,0,12,10,13]
#arr = [1,5,4,3,6,2]
quickSort(arr,0,len(arr)-1)
print(arr)

start = time.time()
arr = range(100000,0,-1)
quickSort(arr,0,len(arr)-1)
print(time.time()-start)

