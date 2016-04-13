# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:05:24 2016

@author: Administrator
"""
#import time

pair = 0
def binDiv(arr,p,r):
    #p24,求数组中逆序对的对数,p是开始下标，r是结束下标,开始时r=len(arr)-1
    #时间复杂度O(nlgn)
    #在归并排序的基础上,归并时加入一个统计逆序对的语句
    if p<r:
        q = int((p+r)/2)
        binDiv(arr,p,q)
        binDiv(arr,q+1,r)
        compareAndCnt(arr,p,q,r)
        
def compareAndCnt(arr,p,q,r):
    #合并两个有序数组,arr1[p...q]和arr2[q+1...r]
    global pair
    n1 = q-p+1#左边数组的长度(因为q中位数是向下取整，所以q-p+1)
    n2 = r-q#右边数组的长度
    arr1 = []
    arr2 = []
    for i in range(n1):
        arr1.append(arr[p+i])
    for j in range(n2):
        #注意j的范围
        arr2.append(arr[q+j+1])

    arr1.append(float('inf'))#放置一个无穷大的数作为“哨兵值”
    arr2.append(float('inf'))
    #print(arr1,arr2)
    i,j = 0,0
    for k in range(p,r+1):#注意k的范围，不需要归并时把赋值给arr[k]的语句注释掉
        if arr1[i] <= arr2[j]:
            #arr[k] = arr1[i]
            i += 1
        else:
            #arr[k] = arr2[j]
            j += 1
            pair += n1 - i#!!!这句是关键，注意不是pair+=1
               


arr = [12,11,10,9,8,7,6,5,4,3,2,1]
mergeSort(arr,0,len(arr)-1)
#print(arr)
print(pair)