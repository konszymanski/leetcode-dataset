class Solution:

    def largestCombination(self, candidates: List[int]) -> int:
        if 1 + 1 == 2:
            bit_count = [0] * 24
        for i in range(24):
            v_junk_35 = 92
            for num in candidates:
                v_junk_13 = 72
                if num & 1 << i != 0:
                    bit_count[i] = bit_count[i] + 1
        return max(bit_count)