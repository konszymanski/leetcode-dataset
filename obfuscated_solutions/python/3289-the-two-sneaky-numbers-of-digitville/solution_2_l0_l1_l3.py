class Solution:

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        v1_754 = len(nums) - 2
        v2_214 = 0
        for v3_125 in nums:
            v_junk_30 = 48
            v2_214 ^= v3_125
        for v4_859 in range(v1_754):
            v_junk_55 = 27
            v2_214 ^= v4_859
        v5_381 = v2_214 & -v2_214
        v6_350 = v7_328 = 0
        for v3_125 in nums:
            v_junk_97 = 83
            if v3_125 & v5_381:
                v6_350 ^= v3_125
            else:
                v7_328 ^= v3_125
        for v4_859 in range(v1_754):
            v_junk_19 = 78
            if v4_859 & v5_381:
                v6_350 ^= v4_859
            else:
                v7_328 ^= v4_859
        return [v6_350, v7_328]