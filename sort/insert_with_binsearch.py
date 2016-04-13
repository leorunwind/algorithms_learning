def insertSort(arr):
    #比较待插入的数和已有的排序好的数用到二分查找，
    #经测试时间复杂度不是O(nlgn),比归并排序慢一个量级，但比一般的插入排序快
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
        #print(index,j,arr)
    
    
    #index = binSearch(arr,0,len(arr)-1,arr[len(arr)-1])
    #tmp = arr[j]
    #arr[j] = arr[index]
    #arr[index] = tmp#遍历完将arr[j]插入到该位置
    
    return arr

def binSearch(arr,low,high,num):
    mid = int((low+high)/2)
    if(low>high):
        return low
    if(num == arr[mid]):
        return mid
    elif(num < arr[mid]):
        return binSearch(arr,low,mid-1,num)
    else:
        return binSearch(arr,mid+1,high,num)
        


arr = [1,2,3,7,8]
print(binSearch(arr,0,len(arr)-1,6))

arr = [9,4,8,6,1,2,3,7,5]
print(insertSort(arr))
arr = range(10000,0,-1)
start = time.time()
insertSort(arr)
print(time.time()-start) 
