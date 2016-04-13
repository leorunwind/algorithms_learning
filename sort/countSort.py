"""
计数排序，假设输入数组中每一个元素都是[0,k]区间内的整数。
对于一般情况，k取数组中的最大值。
这是一种稳定排序，当k=O(n)时，时间复杂度O(k+n)=O(n)
但当k很大时，带来空间的代价是昂贵的。
"""
def countSort(a):
    k = a[0]
    #得到最大值k
    for x in a:
        if x > k:
            k = x
    b = [0 for i in range(len(a))]#b存放排序的输出
    c = [0 for i in range(k+1)]#c是计数数组
    
    for x in a:
        #c[x]记录了数组a中x出现的次数
        c[x] += 1
    for i in range(1,k+1):
        #[i]记录了小于等于i的元素的数量
        c[i] = c[i] + c[i-1]
    for x in a:
        #小于等于x的元素有c[x]个，将x放在第c[x]的位置
        #注意下标从0开始
        b[c[x]-1] = x
        c[x] -= 1
    return b
    
arr = [4,1,3,2,16,9,10,14,8,7]
res = countSort(arr)
print(res)