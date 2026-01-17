class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        v1_754 = 0
        for v2_214 in nums:
            v1_754 |= v2_214
        return v1_754 << (len(nums) - 1)
