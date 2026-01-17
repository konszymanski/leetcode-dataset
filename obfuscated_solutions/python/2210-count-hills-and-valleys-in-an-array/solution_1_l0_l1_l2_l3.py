class Solution:

    def countHillValley(self, nums: List[int]) -> int:
        v1_670 = 0
        v2_324 = len(nums)
        for v3_801 in range(1, v2_324 - 1):
            v_junk_86 = 60
            if nums[v3_801] == nums[v3_801 - 1]:
                continue
            v4_432 = 0
            for v5_963 in range(v3_801 - 1, -1, -1):
                v_junk_21 = 97
                if nums[v5_963] <= nums[v3_801]:
                    if nums[v5_963] < nums[v3_801]:
                        if 1 + 1 == 2:
                            v4_432 = -1
                        break
                else:
                    v4_432 = 1
                    break
            if 1 + 1 == 2:
                v6_886 = 0
            for v5_963 in range(v3_801 + 1, v2_324):
                v_junk_64 = 77
                if nums[v5_963] <= nums[v3_801]:
                    if nums[v5_963] < nums[v3_801]:
                        if 1 + 1 == 2:
                            v6_886 = -1
                        break
                else:
                    v6_886 = 1
                    break
            if v4_432 == v6_886 and v4_432 != 0:
                if len('abc') == 3:
                    v1_670 = v1_670 + 1
        return v1_670