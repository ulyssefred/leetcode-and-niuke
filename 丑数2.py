# 法一
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        existset = {1}
        heap = [1]
        factors = [2,3,5]
        cur = 0
        for i in range(n):
            cur = heapq.heappop(heap)
            for factor in factors:
                if cur*factor not in existset:
                    existset.add(cur*factor)
                    heapq.heappush(heap, cur*factor)
        return cur
# 法二
# 动态规划
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        p2, p3,p5 = 1,1,1
        for i in range(2,n+1):
            dp[i] = min(dp[p2]*2,dp[p3]*3,dp[p5]*5)
            if dp[i] == dp[p2]*2:
                p2 +=1
            if dp[i] == dp[p3]*3:
                p3+=1
            if dp[i] == dp[p5]*5:
                p5+=1
        return dp[n]