class Solution:

    def minOperations(self, nums: List[int]) -> int:
        v1_754 = 0
        for v2_214 in range(2, len(nums)):
            if nums[v2_214 - 2] == 0:
                v1_754 = v1_754 + 1
                nums[v2_214 - 2] = nums[v2_214 - 2] ^ 1
                nums[v2_214 - 1] = nums[v2_214 - 1] ^ 1
                nums[v2_214] = nums[v2_214] ^ 1
        if sum(nums) == len(nums):
            return v1_754
        return -1