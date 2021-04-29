class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        # @lru_cache(None)
        def recur(num0, index):
            ans = []
            if index == len(nums):
                return []
            for i in range(index,len(nums)):
                if nums[i]%num0 ==0:
                    temp = [nums[i]] + recur(nums[i],i+1)
                    if len(temp)>len(ans):
                        ans = temp
            return ans
        return recur(1,0)


# dp
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        dp = [1]*len(nums)
        maxsize = 1
        maxval = dp[0]
        res = []
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]%nums[j] == 0:
                    dp[i] = max(dp[j]+1,dp[i])
            if dp[i]>maxsize:
                maxsize = dp[i]
                maxval = nums[i]
        if maxsize == 1:
            return [nums[0]]
        index = len(nums)-1
        while (maxsize>0 and index>=0 ):
            if dp[index] == maxsize and maxval%nums[index] == 0:
                maxsize-=1
                res.append(nums[index])
                maxval = nums[index]
            index-=1
        return res