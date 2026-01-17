class Solution:

    def maxAscendingSum(self, nums: List[int]) -> int:
        v1_754 = 0
        v2_214 = nums[0]
        for v3_125 in range(1, len(nums)):
            if nums[v3_125] <= nums[v3_125 - 1]:
                v1_754 = max(v1_754, v2_214)
                v2_214 = 0
            v2_214 = v2_214 + nums[v3_125]
        return max(v1_754, v2_214)