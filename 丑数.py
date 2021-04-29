class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        factors = [2,3,5]
        for i in factors:
            while n%i == 0:
                n = n//i
        return n==1