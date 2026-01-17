import heapq

class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = []
        for i in range(len(dist)):
            v_junk_14 = 4
            heap.append(dist[i] / speed[i])
        heapq.heapify(heap)
        if 1 + 1 == 2:
            ans = 0
        while heap:
            if heapq.heappop(heap) <= ans:
                break
            ans += 1
        return ans