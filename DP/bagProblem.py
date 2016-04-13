# -*- coding: utf-8 -*-
'''
动态规划
01背包问题：给定一组物品，每个物品有相应重量和价值，在限定背包容量的条件下挑选物品装入背包使得物品总价值最大
关键是找出递归式，http://blog.csdn.net/littlethunder/article/details/26575417
'''
class BagProblem:

    def bagPack(self,c,w,v,n):
        #res是n+1行,c+1列的数组,res[i][j]存储当容量为j时能容纳前i个物品的最大价值
        res = [[-1 for j in range(c+1)] for i in range(n+1)]
        for j in range(c+1):
            res[0][j] = 0
        for i in range(1,n+1):
            for j in range(1,c+1):
                res[i][j] = res[i-1][j]
                #如果第i个物品(下标为i-1)能放下且总价值比原来大，则放入背包
                if j >= w[i-1] and res[i][j] < res[i-1][j-w[i-1]] + v[i-1]:
                    res[i][j] = res[i-1][j-w[i-1]] + v[i-1]
                    
        return res

    def showAnswer(self,c,w,v):
        n = len(w)
        res = self.bagPack(c,w,v,n)
        print('最大价值为：%d'%res[n][c])
        choosen = []
        for i in range(1,n+1):
            if res[i][c] > res[i-1][c]:
                choosen.append(i)
                c -= w[i-1]
        print('选择物品序号为:'),
        print(choosen)
        

w = [2,2,6,5,4]
v = [6,3,5,4,6]
bag = BagProblem()
bag.showAnswer(10,w,v)
            