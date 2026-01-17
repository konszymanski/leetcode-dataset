class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            v_junk_14 = 4
            for j in range(i + 1, len(nums)):
                v_junk_85 = 55
                if nums[j] == target - nums[i]:
                    return [i, j]
        return []