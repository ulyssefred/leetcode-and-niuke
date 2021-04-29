class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                x = str(nums[j])
                y = str(nums[j+1])
                if int(x+y)< int(y+x):
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        return "".join(map(str,nums)) if nums[0] != 0 else "0"