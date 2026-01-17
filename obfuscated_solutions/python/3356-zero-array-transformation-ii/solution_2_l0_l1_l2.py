class Solution:

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        v1_754 = len(nums)
        v2_214 = 0
        v3_125 = 0
        v4_859 = [0] * (v1_754 + 1)
        for v5_381 in range(v1_754):
            while v2_214 + v4_859[v5_381] < nums[v5_381]:
                v3_125 = v3_125 + 1
                if v3_125 > len(queries):
                    return -1
                (v6_350, v7_328, v8_242) = queries[v3_125 - 1]
                if v7_328 >= v5_381:
                    v4_859[max(v6_350, v5_381)] = v4_859[max(v6_350, v5_381)] + v8_242
                    v4_859[v7_328 + 1] = v4_859[v7_328 + 1] - v8_242
            v2_214 = v2_214 + v4_859[v5_381]
        return v3_125