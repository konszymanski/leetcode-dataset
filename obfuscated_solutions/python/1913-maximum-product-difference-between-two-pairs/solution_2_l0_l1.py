class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = v4_859
        v5_381 = v4_859
        for v6_350 in nums:
            if v6_350  >  v1_754:
                v2_214 = v1_754
                v1_754 = v6_350
            else:
                v2_214 = max(v2_214, v6_350)
            if v6_350  <  v3_125:
                v5_381 = v3_125
                v3_125 = v6_350
            else:
                v5_381 = min(v5_381, v6_350)
        return v1_754  *  v2_214 - v3_125 * v5_381
