import heapq
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        self.heap = self.nums
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
            heapq.heapify(self.heap)
        else:
            if val > self.heap[0]:
                heapq.heapreplace(self.heap,val)
        return self.heap[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# 1、heapq.heapify可以原地把一个list调整成堆[小顶堆] 而 heapq.nlargest 会调成大顶堆
# 2、heapq.heappop可以弹出堆顶，并重新调整
# 3、heapq.heappush可以新增元素到堆中，不会调整
# 4、heapq.heapreplace可以替换堆顶元素，并调整下
# 5、为了维持为K的大小，初始化的时候可能需要删减，后面需要做处理就是如果不满K个就新增，否则做替换；