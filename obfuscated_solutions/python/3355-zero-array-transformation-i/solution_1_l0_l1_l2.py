class Solution:

    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        v1_754 = [0] * (len(nums) + 1)
        for (v2_214, v3_125) in queries:
            v1_754[v2_214] = v1_754[v2_214] + 1
            v1_754[v3_125 + 1] = v1_754[v3_125 + 1] - 1
        v4_859 = []
        v5_381 = 0
        for v6_350 in v1_754:
            v5_381 = v5_381 + v6_350
            v4_859.v7_328(v5_381)
        for (v8_242, v9_854) in zip(v4_859, nums):
            if v8_242 < v9_854:
                return False
        return True