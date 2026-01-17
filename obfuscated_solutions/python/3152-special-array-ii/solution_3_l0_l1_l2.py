class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        v1_754 = len(nums)
        v2_214 = [0] * v1_754
        v2_214[-1] = v1_754 - 1
        for v3_125 in range(v1_754 - 2, -1, -1):
            if nums[v3_125] % 2 == nums[v3_125 + 1] % 2:
                v2_214[v3_125] = v3_125
            else:
                v2_214[v3_125] = v2_214[v3_125 + 1]
        v4_859 = [False] * len(queries)
        for (v3_125, v5_381) in enumerate(queries):
            (v6_350, v7_328) = v5_381
            v4_859[v3_125] = v7_328 <= v2_214[v6_350]
        return v4_859