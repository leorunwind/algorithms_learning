reverPair = 0
def mergeSort(arr,p,r):
    #p17,归并排序，全局变量reverPair统计数组中逆序对数量，O(nlgn).注意r是数组的最大下标.
    if p<r:
        q = int((p+r)/2)
        mergeSort(arr,p,q)
        mergeSort(arr,q+1,r)
        Merge(arr,p,q,r)
        
def Merge(arr,p,q,r):
    #合并两个有序数组,arr1[p...q]和arr2[q+1...r]
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
    for k in range(p,r+1):#注意k的范围
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
            reverPair += n1 - i

    '''不设置哨兵值的写法，要统计逆序对时不建议用这个写法
    for k in range(p,r+1):#注意k的范围
        if i < n1 and j < n2:
            if arr1[i] > arr2[j]:
                arr[k] = arr2[j]
                pair += 1
                j += 1
                continue
            else:
                arr[k] = arr1[i]
                i += 1
                continue
        if i>= n1 and j < n2:
            arr[k] = arr2[j]
            j += 1
            continue
        if i < n1 and j>= n2:
            arr[k] = arr1[i]
            i += 1
            continue
    '''
