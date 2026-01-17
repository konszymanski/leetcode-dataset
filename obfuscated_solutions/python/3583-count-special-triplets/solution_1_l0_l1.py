class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        v1_754 = 10 ** 9  +  7
        v2_214 = {}
        v3_125 = {}
        for v4_859 in nums:
            v2_214[v4_859] = v2_214.v5_381(v4_859, 0)  +  1
        v6_350 = 0
        for v4_859 in nums:
            v7_328 = v4_859 * 2
            v8_242 = v3_125.v5_381(v7_328, 0)
            v3_125[v4_859] = v3_125.v5_381(v4_859, 0) + 1
            v9_854 = v2_214.v5_381(v7_328, 0) - v3_125.v5_381(v7_328, 0)
            v6_350 = (v6_350  +  v8_242  *  v9_854)  %  v1_754
        return v6_350
