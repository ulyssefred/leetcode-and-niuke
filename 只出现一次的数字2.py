# 二进制判断
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans
# hash
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        intdict = {}
        for i in nums:
            intdict[i] = intdict.get(i, 0)+1
        for i in nums:
            if intdict[i] == 1:
                return i