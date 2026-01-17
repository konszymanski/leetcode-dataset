class Solution:

    def search(self, nums: List[int], target: int) -> int:
        v1_754 = v2_214.v3_125(nums, target)
        if v1_754 > 0 and nums[v1_754 - 1] == target:
            return v1_754 - 1
        else:
            return -1