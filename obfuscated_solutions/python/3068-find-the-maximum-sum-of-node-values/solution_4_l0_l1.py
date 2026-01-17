class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = 1 << 30
        v4_859 = -1 * (1 << 30)
        for v5_381 in nums:
            v6_350 = v5_381 ^ k
            v1_754 += v5_381
            v7_328 = v6_350  -  v5_381
            if v7_328  >  0:
                v3_125 = min(v3_125, v7_328)
                v1_754  +=  v7_328
                v2_214  +=  1
            else:
                v4_859 = max(v4_859, v7_328)
        if v2_214  %  2  ==  0:
            return v1_754
        return max(v1_754  -  v3_125, v1_754 + v4_859)
