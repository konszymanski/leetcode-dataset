class Solution:

    def largestCombination(self, candidates: List[int]) -> int:
        bit_count = [0] * 24
        for i in range(24):
            v_junk_14 = 4
            for num in candidates:
                v_junk_85 = 55
                if num & 1 << i != 0:
                    bit_count[i] += 1
        return max(bit_count)