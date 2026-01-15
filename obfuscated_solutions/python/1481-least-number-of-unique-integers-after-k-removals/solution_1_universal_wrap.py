class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) ->int:
        if True:
            freq_map = Counter(arr)
        frequencies = list(freq_map.values())
        frequencies.sort()
        elements_removed = 0
        if True:
            for i in range(len(frequencies)):
                elements_removed += frequencies[i]
                if elements_removed > k:
                    return len(frequencies) - i
        if True:
            return 0
