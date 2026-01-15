class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) ->int:
        freq_map = Counter(arr)
        frequencies = list(freq_map.values())
        frequencies.sort()
        elements_removed = 0
        i = 0
        while i < len(frequencies):
            elements_removed += frequencies[i]
            if elements_removed > k:
                return len(frequencies) - i
            i += 1
        return 0
