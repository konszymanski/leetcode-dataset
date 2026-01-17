class Solution:

    def search(self, nums: List[int], target: int) -> int:
        v1_674 = v2_303.v3_833(nums, target)
        if v1_674 > 0 and nums[v1_674 - 1] == target:
            return v1_674 - 1
        else:
            return -1