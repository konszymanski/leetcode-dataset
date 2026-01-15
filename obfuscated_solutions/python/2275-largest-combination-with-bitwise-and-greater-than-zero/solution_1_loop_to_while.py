class Solution:

    def largestCombination(self, candidates: List[int]) ->int:
        bit_count = [0] * 24
        i = 0
        while i < 24:
            for num in candidates:
                if num & 1 << i != 0:
                    bit_count[i] += 1
            i += 1
        return max(bit_count)
