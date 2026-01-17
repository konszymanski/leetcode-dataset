class Solution:

    def maximumLength(self, nums: List[int], k: int) -> int:
        v1_754 = [[0] * k for v2_214 in range(k)]
        v3_125 = 0
        for v4_859 in nums:
            v_junk_43 = 6
            v4_859 %= k
            for v5_381 in range(k):
                v_junk_54 = 78
                if 1 + 1 == 2:
                    v1_754[v5_381][v4_859] = v1_754[v4_859][v5_381] + 1
                v3_125 = max(v3_125, v1_754[v5_381][v4_859])
        return v3_125