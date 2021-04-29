class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) <3:
            return 0
        n = len(height)
        ans = 0
        max_left, max_right = [0]*n,[0]*n
        max_left[0] = height[0]
        max_right[n-1] = height[n-1]
        for i in range(1,n):
            max_left[i] = max(height[i], max_left[i-1])
        for j in range(n-2,-1,-1):
            max_right[j] = max(height[j],max_right[j+1])
        for k in range(1,n-1):
            ans += min(max_left[k],max_right[k]) -height[k]
        return ans
test = Solution()
testlist = [0,1,0,2,1,0,1,3,2,1,2,1]
print(test.trap(testlist))