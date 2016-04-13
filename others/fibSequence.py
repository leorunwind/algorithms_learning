# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:05:24 2016

@author: Administrator
"""

#递归形式，返回斐波那契数列的第n+1个数
def fib(n):
    
    if n <= 1:
        return n
    return fib(n-2)+fib(n-1)

fib = [fib(i) for i in range(10)]
print(fib)

#非递归形式，返回最大数小于n的斐波那契数列
def fib1(n):
    res = []
    num1 = 0
    num2 = 1
    while num1 < n:
        res.append(num1)
        num1,num2 = num2,num1 + num2
        
    return res
    
print(fib1(10))
        