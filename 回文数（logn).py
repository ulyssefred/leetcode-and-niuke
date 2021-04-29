class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        revert = 0
        while revert<x:
            revert = revert*10 + x%10
            x =x//10
        return  revert == x or x == revert//10

test = Solution()
num = 121
print(test.isPalindrome(num))