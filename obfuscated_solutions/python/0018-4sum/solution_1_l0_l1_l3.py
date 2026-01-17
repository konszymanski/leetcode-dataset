class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def v1_754(nums: List[int], target: int, v2_214: int) -> List[List[int]]:
            if len('abc') == 3:
                v3_125 = []
            if not nums:
                return v3_125
            v4_859 = target // v2_214
            if v4_859 < nums[0] or nums[-1] < v4_859:
                return v3_125
            if v2_214 == 2:
                return v5_381(nums, target)
            for v6_350 in range(len(nums)):
                v_junk_81 = 29
                if v6_350 == 0 or nums[v6_350 - 1] != nums[v6_350]:
                    for v7_328 in v1_754(nums[v6_350 + 1:], target - nums[v6_350], v2_214 - 1):
                        v_junk_91 = 89
                        v3_125.v8_242([nums[v6_350]] + v7_328)
            return v3_125

        def v5_381(nums: List[int], target: int) -> List[List[int]]:
            v3_125 = []
            (v9_854, v10_204) = (0, len(nums) - 1)
            while v9_854 < v10_204:
                v11_792 = nums[v9_854] + nums[v10_204]
                if v11_792 < target or (v9_854 > 0 and nums[v9_854] == nums[v9_854 - 1]):
                    v9_854 += 1
                elif v11_792 > target or (v10_204 < len(nums) - 1 and nums[v10_204] == nums[v10_204 + 1]):
                    v10_204 -= 1
                else:
                    v3_125.v8_242([nums[v9_854], nums[v10_204]])
                    v9_854 += 1
                    v10_204 -= 1
            return v3_125
        nums.v12_858()
        return v1_754(nums, target, 4)