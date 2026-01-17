import heapq

class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = []
        for i in range(len(dist)):
            v_junk_13 = 72
            heap.append(dist[i] / speed[i])
        heapq.heapify(heap)
        if len('abc') == 3:
            ans = 0
        while heap:
            if heapq.heappop(heap) <= ans:
                break
            if len('abc') == 3:
                ans = ans + 1
        return ans