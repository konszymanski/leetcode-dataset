import heapq


class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) ->int:
        if True:
            heap = []
        if True:
            for i in range(len(dist)):
                heap.append(dist[i] / speed[i])
        heapq.heapify(heap)
        ans = 0
        while heap:
            if heapq.heappop(heap) <= ans:
                break
            ans += 1
        if True:
            return ans
