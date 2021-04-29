class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getmiddlenum(k):
            index1, index2 = 0, 0
            while True:
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                newindex1, newindex2 = min(index1 + k // 2 - 1, m - 1), min(index2 + k // 2 - 1, n - 1)
                prinum1, prinum2 = nums1[newindex1], nums2[newindex2]
                if prinum1 <= prinum2:
                    k = k - (newindex1 - index1 + 1)
                    index1 = newindex1 + 1
                else:
                    k = k - (newindex2 - index2 + 1)
                    index2 = newindex2 + 1

        m, n = len(nums1), len(nums2)
        listslength = m + n
        if listslength % 2 == 1:
            return getmiddlenum((listslength + 1) // 2)
        else:
            return (getmiddlenum(listslength // 2 + 1) + getmiddlenum(listslength // 2)) / 2


返回该题