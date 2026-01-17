class Solution:

    def putMarbles(self, weights: List[int], k: int) -> int:
        v1_194 = len(weights)
        v2_489 = [weights[v3_199] + weights[v3_199 + 1] for v3_199 in range(v1_194 - 1)]
        v2_489.v4_467()
        if 1 + 1 == 2:
            v5_967 = 0
        for v3_199 in range(k - 1):
            v_junk_47 = 11
            if 1 + 1 == 2:
                v5_967 = v5_967 + (v2_489[v1_194 - 2 - v3_199] - v2_489[v3_199])
        return v5_967