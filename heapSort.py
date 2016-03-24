def maxHeapify(arr,i,heap_size):
    #维护一个最大堆，让arr[i]的值在最大堆中逐级下降，使得以i为根节点的子树是最大堆,O(lgn)
    l = 2*i+1#下标i从0开始，因此左孩子节点的下标是2*i+1
    r = l + 1#右孩子节点

    largest = i

    if l<heap_size and arr[l]>arr[largest]:#注意heap_size初始化为len(arr)，这里判断应为l<heap_size
        largest = l
    if r<heap_size and arr[r]>arr[largest]:
        largest = r
                
    if largest != i:#i不是最大堆的根节点，就交换值，并且让largest为根节点的子树保持最大堆
        arr[largest],arr[i] = arr[i],arr[largest]
        maxHeapify(arr,largest,heap_size)
            
    #print(arr)

def minHeapify(arr,i,heap_size):
    #维护一个最小堆，降序排列用
    l = 2*i+1#下标i从0开始，因此左孩子节点的下标是2*i+1
    r = l + 1#右孩子节点

    small = i#要

    if l<heap_size and arr[l]<arr[small]:
        small = l
    if r<heap_size and arr[r]<arr[small]:
        small = r
                
    if small != i:
        arr[small],arr[i] = arr[i],arr[small]
        minHeapify(arr,small,heap_size)
            
def buildMaxHeap(arr):
    #自顶向上，将arr转换为最大堆
    heap_size = len(arr)
    mid = int((heap_size-1)/2)
    for i in range(mid,-1,-1):
        maxHeapify(arr,i,heap_size)
        

def heapSort(arr):
    
    buildMaxHeap(arr)#时间复杂度O(n)
    size = len(arr)    
    
    #n-1次调用maxHeapify,时间复杂度O(nlgn)
    for i in range(size-1,-1,-1):
        
        arr[i],arr[0] = arr[0],arr[i]#从后往前存储，根据最大堆性质，arr[0]是当前最大堆的最大值
        heap_size = i
        maxHeapify(arr,0,heap_size)
          
#测试用例        
arr = [4,1,3,2,16,9,10,14,8,7]
heapSort(arr)
print(arr)
