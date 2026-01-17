class Solution:

    def countHillValley(self, nums: List[int]) -> int:
        v1_754 = 0
        v2_214 = len(nums)
        for v3_125 in range(1, v2_214 - 1):
            if nums[v3_125] == nums[v3_125 - 1]:
                continue
            v4_859 = 0
            for v5_381 in range(v3_125 - 1, -1, -1):
                if nums[v5_381] <= nums[v3_125]:
                    if nums[v5_381] < nums[v3_125]:
                        v4_859 = -1
                        break
                else:
                    v4_859 = 1
                    break
            v6_350 = 0
            for v5_381 in range(v3_125 + 1, v2_214):
                if nums[v5_381] <= nums[v3_125]:
                    if nums[v5_381] < nums[v3_125]:
                        v6_350 = -1
                        break
                else:
                    v6_350 = 1
                    break
            if v4_859 == v6_350 and v4_859 != 0:
                v1_754 = v1_754 + 1
        return v1_754