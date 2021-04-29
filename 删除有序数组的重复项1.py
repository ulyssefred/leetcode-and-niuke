class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        slow = 1
        for i in range(1, len(nums)):
            if nums[slow-1]!=nums[i]:
                nums[slow] = nums[i]
                slow+=1
        return slow