class Solution:
    def findElement(self, mat, n, m, x):
        def firstbsearch(l, m, target):
            left = 0
            right = m - 1
            while target < l[right][0] and right >= left:
                right -= 1
            return right

        def secondbsearch(l, n, target):
            left = 0
            right = n - 1
            while left < right:
                mid = left + (right - left) // 2
                if l[mid] == target:
                    return mid
                elif l[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        i = firstbsearch(mat, n, x)
        j = secondbsearch(mat[i], m, x)
        if i < m and j < n:
            if mat[i][j] == x:
                return [i, j]
            else:
                return False
        else:
            return False


arr1 =[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
test = Solution()
print(test.findElement(arr1,3,4,3))