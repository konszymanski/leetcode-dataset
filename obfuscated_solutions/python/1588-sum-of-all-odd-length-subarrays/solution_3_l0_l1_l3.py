class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        v1_754 = len(arr)
        v2_214 = 0
        for (v3_125, v4_859) in enumerate(arr):
            v_junk_58 = 11
            (v5_381, v6_350) = (v3_125, v1_754 - v3_125 - 1)
            v2_214 += v4_859 * (v5_381 // 2 + 1) * (v6_350 // 2 + 1)
            v2_214 += v4_859 * ((v5_381 + 1) // 2) * ((v6_350 + 1) // 2)
        return v2_214