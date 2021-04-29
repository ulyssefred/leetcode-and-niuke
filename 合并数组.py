class Solution:
    def merge(self , intervals ):
        intervals.sort(key= lambda x:x.start)
        merge = []
        for i in intervals:
            if not merge or merge[-1].end < i.start:
                merge.append(i)
            else:
                merge[-1].end = max(merge[-1].end, i.end)
        return merge