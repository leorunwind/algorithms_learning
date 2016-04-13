def maxSubarray(arr,low,high):
    #找出数组里的最大连续子数组,返回最大子数组的边界及和，时间复杂度为O(nlgn)
    #注意形参里的high是最大下标
    if(low == high):
        return (low,high,arr[low])
    
    else:
        mid = int((low+high)/2)
        (left_low,left_high,left_sum) = maxSubarray(arr,low,mid)
        (right_low,right_high,right_sum) = maxSubarray(arr,mid+1,high)
        (cross_low,cross_high,cross_sum) = maxCrossSubarray(arr,low,mid,high)#最大子数组跨越中点的情况
        
        #比较三种情况的最大者
        if left_sum>=right_sum and left_sum>=cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum>=left_sum and right_sum>=cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)
            

def maxCrossSubarray(arr,low,mid,high):
    #注意形参里的high是最大下标
    left_sum = -float('inf')
    sum = 0
    for i in range(mid,low-1,-1):
        sum += arr[i]
        if sum>left_sum:
            left_sum = sum
            left_index = i
            
    right_sum = -float('inf')
    sum = 0
    for j in range(mid+1,high+1):
        sum += arr[j]
        if sum>right_sum:
            right_sum = sum
            right_index = j
            
    return (left_index,right_index,left_sum+right_sum)#返回最大连续子数组的下标及和
    
        
arr = [3,-1,2,4,-2]
res_tuple = maxSubarray(arr,0,len(arr)-1)
print(res_tuple)