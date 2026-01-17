class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        nums.v1_754(v2_214=True)
        v3_125 = 1
        v4_859 = nums[0]
        for v5_381 in range(len(nums)):
            if nums[v5_381] != v4_859:
                v3_125 = v3_125 + 1
                v4_859 = nums[v5_381]
            if v3_125 == 3:
                return nums[v5_381]
        return nums[0]