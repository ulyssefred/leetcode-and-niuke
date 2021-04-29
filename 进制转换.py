class Solution:
    def solve(self , M , N ):
        t = "0123456789ABCDEF"
        if M< 0:
            return "-" + self.solve(-M, N)
        if M < N:
            return t[M]
        return self.solve(M//N, N)+ t[M%N]