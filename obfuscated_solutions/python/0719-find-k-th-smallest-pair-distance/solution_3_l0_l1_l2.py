class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.v1_754()
        v2_214 = len(nums)
        v3_125 = 0
        v4_859 = nums[v2_214 - 1] - nums[0]
        while v3_125 < v4_859:
            v5_381 = (v3_125 + v4_859) // 2
            v6_350 = self.v7_328(nums, v5_381)
            if v6_350 >= k:
                v4_859 = v5_381
            else:
                v3_125 = v5_381 + 1
        return v3_125

    def v7_328(self, nums: List[int], v8_242: int) -> int:
        v6_350 = 0
        v2_214 = len(nums)
        v9_854 = 0
        for v10_204 in range(v2_214):
            while nums[v10_204] - nums[v9_854] > v8_242:
                v9_854 = v9_854 + 1
            v6_350 = v6_350 + (v10_204 - v9_854)
        return v6_350