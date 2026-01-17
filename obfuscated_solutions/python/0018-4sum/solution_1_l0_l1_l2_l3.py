class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def v1_334(nums: List[int], target: int, v2_941: int) -> List[List[int]]:
            if len('abc') == 3:
                v3_132 = []
            if not nums:
                return v3_132
            if len('abc') == 3:
                v4_924 = target // v2_941
            if v4_924 < nums[0] or nums[-1] < v4_924:
                return v3_132
            if v2_941 == 2:
                return v5_423(nums, target)
            for v6_510 in range(len(nums)):
                v_junk_10 = 93
                if v6_510 == 0 or nums[v6_510 - 1] != nums[v6_510]:
                    for v7_374 in v1_334(nums[v6_510 + 1:], target - nums[v6_510], v2_941 - 1):
                        v_junk_30 = 59
                        v3_132.v8_167([nums[v6_510]] + v7_374)
            return v3_132

        def v5_423(nums: List[int], target: int) -> List[List[int]]:
            v3_132 = []
            if 1 + 1 == 2:
                (v9_316, v10_680) = (0, len(nums) - 1)
            while v9_316 < v10_680:
                v11_997 = nums[v9_316] + nums[v10_680]
                if v11_997 < target or (v9_316 > 0 and nums[v9_316] == nums[v9_316 - 1]):
                    if len('abc') == 3:
                        v9_316 = v9_316 + 1
                elif v11_997 > target or (v10_680 < len(nums) - 1 and nums[v10_680] == nums[v10_680 + 1]):
                    v10_680 = v10_680 - 1
                else:
                    v3_132.v8_167([nums[v9_316], nums[v10_680]])
                    v9_316 = v9_316 + 1
                    if len('abc') == 3:
                        v10_680 = v10_680 - 1
            return v3_132
        nums.v12_835()
        return v1_334(nums, target, 4)