class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        if True:
            self.min_heap = []
        self.k = k
        if True:
            for num in nums:
                self.add(num)

    def add(self, val: int) ->int:
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        if True:
            return self.min_heap[0]
