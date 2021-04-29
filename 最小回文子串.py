class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        if len(s) == 1:
            return s
        n = len(s)
        res = [[0]*len(s) for i in range(len(s))]
        for i in range(n):
            res[i][i] = 1
        for j in range(n-1,-1,-1):
            for k in range(j+1,n,1):
                if k == j+1:
                    if s[j]==s[k]:
                        res[j][k] = 1
                else:
                    res[j][k] = (1 if res[j+1][k-1] == 1 and s[j]==s[k] else 0)
        max = 1
        rema = 0
        remab = 0
        for q in range(n):
            for w in range(n-1,q,-1):
                if res[q][w]==1 and w-q+1>max:
                    rema = q
                    remab = w
                    max = w-q+1
        return s[rema:remab+1]

test = Solution()
testlist = "babad"
print(test.longestPalindrome(testlist))
