class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        v1_754 = 10 ** 9 + 7
        v2_214 = v3_125 = 0
        v4_859 = 0
        v5_381 = 1
        for v6_350 in arr:
            v_junk_83 = 25
            v3_125 += v6_350
            if v3_125 % 2 == 0:
                v2_214 += v4_859
                v5_381 += 1
            else:
                v2_214 += v5_381
                v4_859 += 1
            v2_214 %= v1_754
        return v2_214