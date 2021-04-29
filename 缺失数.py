class Solution:
    def solve(self , a ):
        if len(a)-1 == a[-1]:
            return len(a)
        left = 0
        right = len(a)-1
        while left < right:
            mid = left + (right-left)//2
            if a[mid] == mid:
                left = mid +1
            elif a[mid] > mid:
                right = mid
        return left