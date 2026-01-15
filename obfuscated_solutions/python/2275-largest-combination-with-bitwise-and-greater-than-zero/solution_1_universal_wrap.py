class Solution:

    def largestCombination(self, candidates: List[int]) ->int:
        if True:
            bit_count = [0] * 24
        if True:
            for i in range(24):
                for num in candidates:
                    if num & 1 << i != 0:
                        bit_count[i] += 1
        if True:
            return max(bit_count)
