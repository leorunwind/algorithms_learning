# -*- coding: utf-8 -*-
'''
动态规划
最长公共子序列问题，递归式见《算法导论》P224
'''
class LCS:
    def calLength(self,x,y):
        m = len(x)
        n = len(y)
        c = [[0 for j in range(n+1)] for i in range(m+1)]
        b = [['' for j in range(n+1)] for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if x[i-1] == y[j-1]:
                    c[i][j] = c[i-1][j-1] + 1
                    b[i][j] = 'NW'
                elif c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = 'N'
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = 'W'
        return c,b
        
    def printLCS(self,b,x,i,j):
        if i==0 or j==0:
            return
        if b[i][j] == 'NW':
            self.printLCS(b,x,i-1,j-1)
            print(x[i-1]),
        elif b[i][j] == 'N':
            self.printLCS(b,x,i-1,j)
        else:
            self.printLCS(b,x,i,j-1)
    
lcs = LCS()
x = 'abcbdab'
y = 'bdcaba'
ret = lcs.calLength(x,y)
b = ret[1]
lcs.printLCS(b,x,len(x),len(y))