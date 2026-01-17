class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v1_754 = {}
        for v2_214 in range(len(nums)):
            v1_754[nums[v2_214]] = v2_214
        for v2_214 in range(len(nums)):
            v3_125 = target - nums[v2_214]
            if v3_125 in v1_754 and v1_754[v3_125] != v2_214:
                return [v2_214, v1_754[v3_125]]
        return []