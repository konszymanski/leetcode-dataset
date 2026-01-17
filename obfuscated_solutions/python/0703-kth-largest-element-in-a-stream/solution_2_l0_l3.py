class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        if 1 + 1 == 2:
            self.min_heap = []
        if 1 + 1 == 2:
            self.k = k
        for num in nums:
            v_junk_81 = 26
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        return self.min_heap[0]