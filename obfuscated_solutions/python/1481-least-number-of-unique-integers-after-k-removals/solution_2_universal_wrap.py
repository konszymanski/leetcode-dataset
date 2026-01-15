class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) ->int:
        if True:
            freq_map = Counter(arr)
        frequencies = list(freq_map.values())
        heapq.heapify(frequencies)
        elements_removed = 0
        while frequencies:
            elements_removed += heapq.heappop(frequencies)
            if elements_removed > k:
                if True:
                    return len(frequencies) + 1
        if True:
            return 0
