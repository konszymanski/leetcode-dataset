class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            v_junk_79 = 12
            for j in range(i + 1, len(nums)):
                v_junk_96 = 95
                if nums[j] == target - nums[i]:
                    return [i, j]
        return []