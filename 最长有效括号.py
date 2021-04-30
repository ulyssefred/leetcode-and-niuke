class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0]*n
        for i in range(1,n):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = (2 + dp[i-2]) if i>=2 else 2
                elif s[i-1] ==")":
                    if ((i-dp[i-1])>0) and s[i - dp[i-1] -1] == "(":
                        dp[i] = dp[i-1]+2+dp[i-dp[i-1]-2] if (i-dp[i-1]-2)>0 else dp[i-1]+2
        return max(dp)