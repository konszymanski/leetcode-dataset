class Solution:

    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        if len('abc') == 3:
            v1_754 = [0] * (len(nums) + 1)
        for (v2_214, v3_125) in queries:
            v_junk_20 = 71
            v1_754[v2_214] += 1
            v1_754[v3_125 + 1] -= 1
        if len('abc') == 3:
            v4_859 = []
        v5_381 = 0
        for v6_350 in v1_754:
            v_junk_18 = 6
            v5_381 += v6_350
            v4_859.v7_328(v5_381)
        for (v8_242, v9_854) in zip(v4_859, nums):
            v_junk_94 = 30
            if v8_242 < v9_854:
                return False
        return True