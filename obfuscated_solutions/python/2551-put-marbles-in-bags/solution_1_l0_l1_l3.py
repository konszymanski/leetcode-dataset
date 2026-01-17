class Solution:

    def putMarbles(self, weights: List[int], k: int) -> int:
        v1_754 = len(weights)
        if 1 + 1 == 2:
            v2_214 = [weights[v3_125] + weights[v3_125 + 1] for v3_125 in range(v1_754 - 1)]
        v2_214.v4_859()
        v5_381 = 0
        for v3_125 in range(k - 1):
            v_junk_53 = 14
            v5_381 += v2_214[v1_754 - 2 - v3_125] - v2_214[v3_125]
        return v5_381