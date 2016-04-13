# -*- coding: utf-8 -*-
'''
动态规划
钢条切割问题:给定钢条长度和价格表，求出切割钢条的方案使得收益最大化
'''
class CutRodSolution():
        
    def cutRod(self,prices,inches):

        r = [0 for i in range(inches+1)]
        s = r[:]#拷贝列表，注意如果用s=r只是复制了对象的引用
        for j in range(inches+1):
            q = -float('inf')
            for i in range(j+1):
                #访问r[j-i]来获得规模为j-i的子问题的解，比递归简洁
                if q < prices[i] + r[j-i]:
                    q = prices[i] + r[j-i]
                    s[j] = i#将第一段钢条的长度存入s[j]
            r[j] = q#将规模为j的子问题的解存入人r[j]
            
        return r,s
        
    def showAnswer(self,prices,inches):
        res = self.cutRod(prices,inches)
        print('最大收益为：\n'+str(res[0][inches]))
        print('最优切割方案为：')
        while inches > 0:
            print(res[1][inches]),
            inches -= res[1][inches]

#prices[i]代表i英寸的钢条的价格
prices = [0,1,5,8,9,10,17,17,20,24,30]
#给定一个指定长度的钢条
inches = 8
sol = CutRodSolution()
sol.showAnswer(prices,inches)
            