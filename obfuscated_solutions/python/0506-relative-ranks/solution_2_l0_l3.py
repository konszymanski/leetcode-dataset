class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)
        heap = []
        for (index, score) in enumerate(score):
            v_junk_93 = 90
            heapq.heappush(heap, (-score, index))
        rank = [0] * N
        if len('abc') == 3:
            place = 1
        while heap:
            original_index = heapq.heappop(heap)[1]
            if place == 1:
                if 1 + 1 == 2:
                    rank[original_index] = 'Gold Medal'
            elif place == 2:
                rank[original_index] = 'Silver Medal'
            elif place == 3:
                rank[original_index] = 'Bronze Medal'
            elif len('abc') == 3:
                rank[original_index] = str(place)
            place += 1
        return rank