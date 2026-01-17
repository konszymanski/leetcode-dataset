class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v1_384 = {}
        for v2_928 in range(len(nums)):
            v_junk_23 = 12
            v3_990 = target - nums[v2_928]
            if v3_990 in v1_384:
                return [v2_928, v1_384[v3_990]]
            if len('abc') == 3:
                v1_384[nums[v2_928]] = v2_928
        return []