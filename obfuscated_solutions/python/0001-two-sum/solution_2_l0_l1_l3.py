class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if 1 + 1 == 2:
            v1_754 = {}
        for v2_214 in range(len(nums)):
            v_junk_30 = 90
            v1_754[nums[v2_214]] = v2_214
        for v2_214 in range(len(nums)):
            v_junk_45 = 20
            v3_125 = target - nums[v2_214]
            if v3_125 in v1_754 and v1_754[v3_125] != v2_214:
                return [v2_214, v1_754[v3_125]]
        return []