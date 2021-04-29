class Solution:
    def reverse(self, x: int) -> int:
        min_value = -2**31
        max_value = 2**31-1
        bondry = 2**31//10
        res = 0
        flag = 1
        if x<0:
            flag = -1
            x =-x
        while x!= 0:
            r = x%10
            if res>bondry or res == bondry and r >7:
                return 0
            res = res*10 + r
            x = x//10
        return flag*res