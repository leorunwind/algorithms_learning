# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:05:24 2016

@author: Administrator
"""
import random

def genRandomOrderArr(arr):
    #原址排列给定数组，产生随机均匀排列数组
    '''保存原数组，非必需
    bak = []
    for i in range(len(arr)):
        bak.append(arr[i])
    '''

    for i in range(len(arr)):
        #产生一个当前下标到最大下标的随机数，注意randint(i,j)可能产生j
        rand = random.randint(i,len(arr)-1)
        #将两个数交换
        arr[i],arr[rand] = arr[rand],arr[i]
    
    return arr
        
x = [0,1,2,3,4,5,6,7,8,9,10]

tup = genRandomOrderArr(x)
print(tup)