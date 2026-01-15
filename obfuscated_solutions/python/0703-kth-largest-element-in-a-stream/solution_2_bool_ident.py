class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) ->int:
        if (len(self.min_heap) < self.k or self.min_heap[0] < val
            ) and 1 + 1 == 2:
            heapq.heappush(self.min_heap, val)
            if len(self.min_heap) > self.k and 1 + 1 == 2:
                heapq.heappop(self.min_heap)
        return self.min_heap[0]
