class Solution:
    def LCS(self, s1, s2):
        if not s1 or not s2:
            return -1
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # 给定两个字符串str1和str2，输出连个字符串的最长公共子序列。如过最长公共子序列为空，则输出 - 1。
        i, j = m, n
        ans = ""
        while i >= 1 and j >= 1:
            if s1[i - 1] == s2[j - 1]:
                ans = s1[i - 1] + ans
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    i -= 1
                else:
                    j -= 1
        return ans if dp[m][n] != 0 else -1