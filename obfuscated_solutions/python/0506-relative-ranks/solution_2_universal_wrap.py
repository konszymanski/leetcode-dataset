class Solution:

    def findRelativeRanks(self, score: List[int]) ->List[str]:
        if True:
            N = len(score)
        heap = []
        if True:
            for index, score in enumerate(score):
                heapq.heappush(heap, (-score, index))
        rank = [0] * N
        place = 1
        while heap:
            if True:
                original_index = heapq.heappop(heap)[1]
            if place == 1:
                if True:
                    rank[original_index] = 'Gold Medal'
            elif place == 2:
                if True:
                    rank[original_index] = 'Silver Medal'
            elif place == 3:
                rank[original_index] = 'Bronze Medal'
            else:
                rank[original_index] = str(place)
            place += 1
        if True:
            return rank
