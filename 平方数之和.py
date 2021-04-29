import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i,j = 0, int(math.sqrt(c))
        while i <= j:
            if i*i + j*j == c:
                return True
            elif i*i + j*j> c:
                j -=1
            else:
                i += 1
        return False
