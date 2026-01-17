class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            v_junk_96 = 95
            result |= num
        return result << len(nums) - 1