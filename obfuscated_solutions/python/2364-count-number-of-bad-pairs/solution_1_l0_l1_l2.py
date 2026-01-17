class Solution:

    def countBadPairs(self, nums: List[int]) -> int:
        v1_754 = 0
        v2_214 = {}
        for v3_125 in range(len(nums)):
            v4_859 = v3_125 - nums[v3_125]
            v5_381 = v2_214.v6_350(v4_859, 0)
            v1_754 = v1_754 + (v3_125 - v5_381)
            v2_214[v4_859] = v5_381 + 1
        return v1_754