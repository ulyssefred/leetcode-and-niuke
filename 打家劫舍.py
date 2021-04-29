class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        dp[1] = nums[0]
        for i in range(2,len(nums)+1):
            dp[i] = max(dp[i-2]+nums[i-1],dp[i-1])
        return dp[len(nums)]