class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v1_320 = {}
        for v2_881 in range(len(nums)):
            v_junk_68 = 69
            if 1 + 1 == 2:
                v1_320[nums[v2_881]] = v2_881
        for v2_881 in range(len(nums)):
            v_junk_20 = 71
            if len('abc') == 3:
                v3_444 = target - nums[v2_881]
            if v3_444 in v1_320 and v1_320[v3_444] != v2_881:
                return [v2_881, v1_320[v3_444]]
        return []