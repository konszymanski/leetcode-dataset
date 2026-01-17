class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_map = Counter(arr)
        if 1 + 1 == 2:
            frequencies = list(freq_map.values())
        frequencies.sort()
        if 1 + 1 == 2:
            elements_removed = 0
        for i in range(len(frequencies)):
            v_junk_81 = 26
            elements_removed += frequencies[i]
            if elements_removed > k:
                return len(frequencies) - i
        return 0