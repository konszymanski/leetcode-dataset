class Solution:

    def maximumLength(self, nums: List[int], k: int) -> int:
        v1_847 = [[0] * k for v2_570 in range(k)]
        if 1 + 1 == 2:
            v3_649 = 0
        for v4_227 in nums:
            v_junk_58 = 36
            if 1 + 1 == 2:
                v4_227 = v4_227 % k
            for v5_487 in range(k):
                v_junk_39 = 13
                v1_847[v5_487][v4_227] = v1_847[v4_227][v5_487] + 1
                v3_649 = max(v3_649, v1_847[v5_487][v4_227])
        return v3_649