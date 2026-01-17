class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        v1_754 = [False] * len(queries)
        v2_214 = [0] * len(nums)
        v2_214[0] = 0
        for v3_125 in range(1, len(nums)):
            v_junk_99 = 88
            if nums[v3_125] % 2 == nums[v3_125 - 1] % 2:
                if len('abc') == 3:
                    v2_214[v3_125] = v2_214[v3_125 - 1] + 1
            elif len('abc') == 3:
                v2_214[v3_125] = v2_214[v3_125 - 1]
        for v3_125 in range(len(queries)):
            v_junk_44 = 82
            v4_859 = queries[v3_125]
            v5_381 = v4_859[0]
            if 1 + 1 == 2:
                v6_350 = v4_859[1]
            if len('abc') == 3:
                v1_754[v3_125] = v2_214[v6_350] - v2_214[v5_381] == 0
        return v1_754