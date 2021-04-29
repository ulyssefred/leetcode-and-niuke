# 给定String类型的数组strArr，再给定整数k，请严格按照排名顺序打印 出次数前k名的字符串。
# [要求]
# 如果strArr长度为N，时间复杂度请达到O(N \log K)O(NlogK)
#
# 输出K行，每行有一个字符串和一个整数（字符串表示）。
# 你需要按照出现出现次数由大到小输出，若出现次数相同时字符串字典序较小的优先输出
import collections
import heapq


import heapq
import collections
class Solution:
    def topKstrings(self , strings , k ):
        count = collections.Counter(strings)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            s = heapq.heappop(heap)
            res.append([s[1],str(-s[0])])
        return res
