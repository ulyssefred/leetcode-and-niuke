import collections


class Solution:
    def set(self, key, value, k):
        if key in self.od:
            self.od.move_to_end(key)
            return
        if len(self.od) < k:
            self.od[key] = value
            self.od.move_to_end(key)
        else:
            self.od.popitem(last=False)
            self.od[key] = value
            self.od.move_to_end(key)

    def get(self, key):
        if key not in self.od:
            self.result.append(-1)
        else:
            self.od.move_to_end(key)
            self.result.append(self.od[key])

    def LRU(self, operators, k):
        self.od = collections.OrderedDict()
        self.result = []
        for i in operators:
            if i[0] == 1:
                self.set(i[1], i[2], k)
            else:
                if i[0] == 2:
                    self.get(i[1])
        return print(self.result)
test = Solution()
testitem = [[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]]
test.LRU(testitem,3)