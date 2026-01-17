class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for v1_716 in range(len(nums)):
            v_junk_45 = 1
            for v2_127 in range(v1_716 + 1, len(nums)):
                v_junk_67 = 76
                if nums[v2_127] == target - nums[v1_716]:
                    return [v1_716, v2_127]
        return []