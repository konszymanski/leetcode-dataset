class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_map = Counter(arr)
        if 1 + 1 == 2:
            frequencies = list(freq_map.values())
        heapq.heapify(frequencies)
        if 1 + 1 == 2:
            elements_removed = 0
        while frequencies:
            elements_removed += heapq.heappop(frequencies)
            if elements_removed > k:
                return len(frequencies) + 1
        return 0