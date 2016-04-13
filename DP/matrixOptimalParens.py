# -*- coding: utf-8 -*-
'''
动态规划
矩阵链乘问题(较难),递归式见《算法导论》P213
'''
class MatrixOptimalParen:
        
    def matrixChain(self,p):
        n = len(p) - 1
        #m[i][j]记录表示计算矩阵Ai..j所需标量乘法次数的最小值
        m = [[0 for j in range(n+1)] for i in range(n+1)]
        #s[i][j]保存Ai...Aj最优括号化方案的分割点k
        s = [[0 for j in range(n+1)] for i in range(n+1)]
        for chain in range(2,n+1):
            for i in range(1,n-chain+2):
                j = i + chain-1
                m[i][j] = float('inf')
                for k in range(i,j):
                    #递归式
                    q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                    if q < m[i][j]:
                        m[i][j] = q
                        s[i][j] = k
            
        return m,s
        
    def printOptimal(self,s,i,j):
        if i == j:
            print("A%d"%i),
        else:
            print("("),
            self.printOptimal(s,i,s[i][j])
            self.printOptimal(s,s[i][j]+1,j)
            print(")"),

#Ai矩阵规模为p[i-1]*p[i]
p = [30,35,15,5,10,20,25]
n = len(p) - 1
mat = MatrixOptimalParen()
ret = mat.matrixChain(p)
m = ret[0]
s = ret[1]
print('最小标量乘法次数为：')
for i in range(len(m)):
    print(m[i])
print('最优括号化方案为：')
mat.printOptimal(s,1,len(p)-1)
        

            