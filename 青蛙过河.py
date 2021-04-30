class Solution:
    def canCross(self, stones: list[int]) -> bool:
        n = len(stones)
        dp = [[False]*n for _ in range(n)]
        dp[0][0] = True
        for i in range(1,n):
            if stones[i]-stones[i-1]>i:
                return False
        for i in range(1,n):
            for j in range(i):
                k = stones[i]-stones[j]
                if k > j+1:
                    continue
                dp[i][k] = dp[j][k] or dp[j][k-1] or dp[j][k+1]
                if i == n - 1 and dp[i][k]:
                    return True
        return False
test =  [0,1,2,3,4,8,9,11]
a = Solution()
print(a.canCross(test))