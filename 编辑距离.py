# 带权重
class Solution:
    def minEditCost(self , str1 , str2 , ic , dc , rc ):
        m, n = len(str1), len(str2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m+1)]
        # 删除的初始化
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + dc
        #插入的初始化
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ic
        for k in range(1, m + 1):
            for q in range(1, n + 1):
                if str1[k - 1] == str2[q - 1]:
                    dp[k][q] = dp[k - 1][q - 1]
                else:
                    dp[k][q] = min(dp[k - 1][q] + dc, dp[k][q - 1] + ic, dp[k - 1][q - 1] + rc)
        return dp[m][n]
arr1 = "abc"
arr2 = "adc"
ic,dc,rc = 5,3,2
test = Solution()
print(test.minEditCost(arr1,arr2,ic,dc,rc))
