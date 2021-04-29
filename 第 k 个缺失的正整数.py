# 1
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cur = 1
        miscount = 0
        i = 0
        while miscount<k:
            if cur == arr[i]:
                if i<len(arr)-1:
                    i+=1
            else:
                miscount+=1
            cur+=1
        return cur-1
# 2.缺失的正整数一定 >= k
# 数组中每出现一个 <= k 的数字, 意味着少了一个缺失的数字, 此时k+1
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(len(arr)):
            if arr[i]<=k:
                k+=1
        return k