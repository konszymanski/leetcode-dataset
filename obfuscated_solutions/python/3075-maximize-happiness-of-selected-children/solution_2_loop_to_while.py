class Solution:

    def maximumHappinessSum(self, happiness: List[int], k: int) ->int:
        max_heap = [(-h) for h in happiness]
        heapq.heapify(max_heap)
        total_happiness_sum = 0
        turns = 0
        i = 0
        while i < k:
            total_happiness_sum += max(-heapq.heappop(max_heap) - turns, 0)
            turns += 1
            i += 1
        return total_happiness_sum
