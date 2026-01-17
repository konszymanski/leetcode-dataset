class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        v1_754 = len(arr)
        v2_214 = 0
        for v3_125 in range(v1_754):
            for v4_859 in range(v3_125, v1_754):
                if (v4_859 - v3_125 + 1) % 2 == 1:
                    v5_381 = 0
                    for v6_350 in range(v3_125, v4_859 + 1):
                        v5_381 = v5_381 + arr[v6_350]
                    v2_214 = v2_214 + v5_381
        return v2_214