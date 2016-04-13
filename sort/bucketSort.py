"""
桶排序，假设输入数组的中每一个元素均匀分布在[0,1)区间上。
这是一种稳定排序，因为对输入数据作了假设，速度较快。
当不符合均匀分布时只要满足以下条件也能使得时间复杂度为O(n)：
所有桶的大小的平方和与总的元素数呈线性关系
"""
import random

def bucketSort(a):
    n = len(a)
    b = [[] for i in range(n)]#产生n个链表
    for i in range(n):
        #第i个链表存放的是半开区间[i/10,(i+1)/10]的值
        buc = int(n*a[i])
        b[buc].append(a[i])
    res = []
    for list in b:
        insertSort(list)#插入排序
        res += list
    return res

def insertSort(arr):
    #对每一个链表进行插入排序
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

#测试用例：
#产生一个[0,1)区间均匀分布的数组
ranArr = [random.random() for i in range(10)]
print(ranArr)
res = bucketSort(ranArr)
print(res)