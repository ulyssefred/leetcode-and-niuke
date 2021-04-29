class Solution:
    def permuteUnique(self , num ):
        # if not num:
        #     return []
        # S = "".join(map(str,num))
        # result = []
        # def recur(S, r):
        #     if S == "":
        #         if r not in result:
        #             result.append(r)
        #         r= []
        #         return
        #     for i in range(len(S)):
        #         r += S[i]
        #         recur(S[:i]+S[i+1:],r)
        #         r = r[:-1]
        # recur(S,"")
        # for j in range(len(result)):
        #     result[j] = list(map(int,result[j]))
        #
        # return result
        lenght = len(num)
        if not num:
            return [[]]
        a = []
        self.b = []
        def recur(num):
            if len(self.b) == lenght:
                if self.b not in a:
                    a.append(self.b)
                self.b = []
                return
            else:
                for i in range(len(num)):
                    self.b.append(num[i])
                    tmp = num[:i] + num[i + 1:]
                    recur(tmp)

        recur(num)
        return a
arr = [1,1,2]
test = Solution()
print(test.permuteUnique(arr))