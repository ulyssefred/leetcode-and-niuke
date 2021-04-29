class Solution:
    def LIS(self , nums ):
        resnum = 1
        if len(nums) < 2:
            return []
        dp = [[] for i in range(len(nums))]

        for ni in range(1, len(nums)):
            for si in range(ni):
                if nums[si] > nums[ni]: continue  # 保证升序
                dp[ni].append((nums[si], nums[ni]))
                for L in dp[si]:
                    dp[ni].append(L + (nums[ni],))
        res = set(L for LL in dp for L in LL)
        listarr = [list(L) for L in res]
        resulstr = "".join(map(str,listarr[0]))
        for i in listarr:
            resnum = max(resnum, len(i))
        for j in listarr:
            if len(j) == resnum:
                z = "".join(map(str,j))
                if z < resulstr:
                    resulstr = z
        resultlist = []
        for q in resulstr:
            resultlist.append(int(q))



        return resultlist


arr = [2,1,5,3,6,4,8,9,7]
test = Solution()
print(test.LIS(arr))
