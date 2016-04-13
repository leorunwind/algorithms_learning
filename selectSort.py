def selectSort(arr):
    #选择排序，最坏为O(n^2)
    #升序排列一个数组，降序排列将while语句中改为arr[i]<key即可
    if(arr==None or len(arr)<2):
        return arr
    for j in range(len(arr)):
        
        index = getMin(arr,j,len(arr))
        #未排序中最小的元素跟arr[j]交换
        tmp = arr[j]
        arr[j] = arr[index]
        arr[index] = tmp
        
    return arr


def getMin(arr,low,high):
    index = low
    for i in range(low,high):
        if arr[i] < arr[index]:
            index = i
    return index
