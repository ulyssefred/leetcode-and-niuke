class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = [0]*(len(nums)+1)
        dp2= [0]*(len(nums)+1)
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        dp1[1] = nums[0]
        for i in range(2,len(nums)):
            dp1[i] = max(dp1[i-2]+nums[i-1],dp1[i-1])
        dp2[2] = nums[1]
        for i in range(3,len(nums)+1):
            dp2[i] = max(dp2[i-2]+nums[i-1],dp2[i-1])
        return max(dp1[len(nums)-1],dp2[len(nums)])