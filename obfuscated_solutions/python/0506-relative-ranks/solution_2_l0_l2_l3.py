class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if len('abc') == 3:
            N = len(score)
        if len('abc') == 3:
            heap = []
        for (index, score) in enumerate(score):
            v_junk_87 = 34
            heapq.heappush(heap, (-score, index))
        rank = [0] * N
        place = 1
        while heap:
            original_index = heapq.heappop(heap)[1]
            if place != 1:
                if place != 2:
                    if place != 3:
                        rank[original_index] = str(place)
                    else:
                        rank[original_index] = 'Bronze Medal'
                else:
                    rank[original_index] = 'Silver Medal'
            else:
                rank[original_index] = 'Gold Medal'
            place = place + 1
        return rank