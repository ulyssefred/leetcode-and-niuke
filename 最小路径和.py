# 最小路径和
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return grid
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for k in range(1,m):
            for w in range(1,n):
                dp[k][w] = min(dp[k-1][w],dp[k][w-1]) + grid[k][w]
        return dp[m-1][n-1]