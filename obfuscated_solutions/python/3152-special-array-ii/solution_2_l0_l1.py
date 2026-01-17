class Solution:
    def isArraySpecial(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[bool]:
        v1_754 = [False]  *  len(queries)
        v2_214 = [0] * len(nums)
        v2_214[0] = 0
        for v3_125 in range(1, len(nums)):
            if nums[v3_125] % 2  ==  nums[v3_125 - 1] % 2:
                v2_214[v3_125] = v2_214[v3_125  -  1] + 1
            else:
                v2_214[v3_125] = v2_214[v3_125 - 1]
        for v3_125 in range(len(queries)):
            v4_859 = queries[v3_125]
            v5_381 = v4_859[0]
            v6_350 = v4_859[1]
            v1_754[v3_125] = v2_214[v6_350]  -  v2_214[v5_381]  ==  0
        return v1_754
