class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for v1_754 in range(len(nums)):
            for v2_214 in range(v1_754 + 1, len(nums)):
                if nums[v2_214] == target  -  nums[v1_754]:
                    return [v1_754, v2_214]
        return []
