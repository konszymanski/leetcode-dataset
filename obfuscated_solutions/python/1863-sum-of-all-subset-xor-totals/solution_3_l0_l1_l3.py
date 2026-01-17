class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            v1_754 = 0
        for v2_214 in nums:
            v_junk_74 = 78
            v1_754 |= v2_214
        return v1_754 << len(nums) - 1