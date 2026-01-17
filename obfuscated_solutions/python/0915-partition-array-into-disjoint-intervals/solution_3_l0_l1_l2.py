class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:
        v1_754 = nums[0]
        v2_214 = nums[0]
        v3_125 = 1
        for v4_859 in range(1, len(nums)):
            if nums[v4_859] >= v1_754:
                v2_214 = max(v2_214, nums[v4_859])
            else:
                v3_125 = v4_859 + 1
                v1_754 = v2_214
        return v3_125