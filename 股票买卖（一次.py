class Solution:
    def maxProfit(self , prices ):
        n = len(prices)
        if n < 2:
            return 0
        maxprofit = [0]*n
        cost = prices[0]
        for i in range(1,n):
            maxprofit[i] = max(maxprofit[i-1], prices[i] -cost)
            cost = min(cost, prices[i])
        return maxprofit[n-1]