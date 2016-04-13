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
    
def insertSortWithBinSearch(arr):
    #比较待插入的数和已有的排序好的数用到二分查找，
    #经测试时间复杂度也不是O(nlgn),比归并排序慢一个量级，但比一般的插入排序快
    #升序排列一个数组，降序排列将while语句中改为arr[i]<key即可
    if(arr==None or len(arr)<2):
        return arr
    
    for j in range(1,len(arr)):
        key = arr[j]#待插入的数
        
        index = binSearch(arr,0,j-1,key)#二分查找适合插入的位置,O(lgn)
        i = j-1
        while(i>=index):
            arr[i+1] = arr[i]
            i -= 1
        arr[index] = key#遍历完将arr[j]插入到该位置
    
    return arr

def binSearch(arr,low,high,num):
    #二分查找num在数组中的位置，用到递归
    mid = int((low+high)/2)
    if(low>high):
        return low
    if(num == arr[mid]):
        return mid
    elif(num < arr[mid]):
        return binSearch(arr,low,mid-1,num)
    else:
        return binSearch(arr,mid+1,high,num)
