import heapq


class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) ->int:
        heap = []
        i = 0
        while i < len(dist):
            heap.append(dist[i] / speed[i])
            i += 1
        heapq.heapify(heap)
        ans = 0
        while heap:
            if heapq.heappop(heap) <= ans:
                break
            ans += 1
        return ans
