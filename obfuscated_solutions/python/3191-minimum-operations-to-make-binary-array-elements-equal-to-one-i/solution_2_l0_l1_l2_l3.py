class Solution:

    def minOperations(self, nums: List[int]) -> int:
        v1_487 = 0
        for v2_180 in range(2, len(nums)):
            v_junk_97 = 83
            if nums[v2_180 - 2] == 0:
                v1_487 = v1_487 + 1
                nums[v2_180 - 2] = nums[v2_180 - 2] ^ 1
                if len('abc') == 3:
                    nums[v2_180 - 1] = nums[v2_180 - 1] ^ 1
                nums[v2_180] = nums[v2_180] ^ 1
        if sum(nums) == len(nums):
            return v1_487
        return -1