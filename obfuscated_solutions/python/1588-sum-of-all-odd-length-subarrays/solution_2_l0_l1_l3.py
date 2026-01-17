class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            v1_754 = len(arr)
        v2_214 = 0
        for v3_125 in range(v1_754):
            v_junk_68 = 69
            v4_859 = 0
            for v5_381 in range(v3_125, v1_754):
                v_junk_43 = 6
                v4_859 += arr[v5_381]
                v2_214 += v4_859 if (v5_381 - v3_125 + 1) % 2 == 1 else 0
        return v2_214