class Solution:
    def merge(self, A, m, B, n):
        while m and n:
            if A[m - 1] >= B[n - 1]:
                A[m + n - 1] = A[m - 1]
                m = m - 1
            else:
                A[m + n - 1] = B[n - 1]
                n = n - 1
        if n:
            A[:n] = B[:n]
        return A
list1 = []
list2 = [1]
a = Solution()
print(a.merge(list1,0,list2,1))