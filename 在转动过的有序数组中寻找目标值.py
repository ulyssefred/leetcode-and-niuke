class Solution:
    def search(self , A , target ):
        # 寻找旋转数组中的最小值
        def midminindex(numbers):
            left = 0
            right = len(numbers) -1
            while left<right:
                mid = left + (right-left)//2
                if numbers[mid] < numbers[right]:
                    right = mid
                elif numbers[mid]> numbers[right]:
                    left = mid + 1
                else:
                    right-=1
            return left
        # 二分查找
        def binsearch(list1, left, right,target):
            low = left
            high = right
            while low <= high:
                mid = low + (high - low)//2
                if list1[mid] > target:
                    high = mid -1
                elif list1[mid] < target:
                    low = mid +1
                else:
                    return mid
            return -1
        minium = midminindex(A)
        left = 0
        right = len(A)-1
        if minium >0:
            if target >= A[minium] and target<=A[right]:
                return binsearch(A, minium, right, target)
            elif target>= A[left] and target<=A[minium-1]:
                return binsearch(A, left, minium-1, target)
            else:
                return -1
        else:
            if target >= A[minium] and target<=A[right]:
                return binsearch(A, minium, right, target)
            else:
                return -1
test = Solution()
A = [1]
target = 1
print(test.search(A,target))
