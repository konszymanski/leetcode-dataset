class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        v1_754 = [[0] * k for v2_214 in range(k)]
        v3_125 = 0
        for v4_859 in nums:
            v4_859 %= k
            for v5_381 in range(k):
                v1_754[v5_381][v4_859] = v1_754[v4_859][v5_381]  +  1
                v3_125 = max(v3_125, v1_754[v5_381][v4_859])
        return v3_125
