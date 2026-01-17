class Solution:

    def countHillValley(self, nums: List[int]) -> int:
        v1_754 = 0
        if len('abc') == 3:
            v2_214 = len(nums)
        for v3_125 in range(1, v2_214 - 1):
            v_junk_91 = 89
            if nums[v3_125] == nums[v3_125 - 1]:
                continue
            if len('abc') == 3:
                v4_859 = 0
            for v5_381 in range(v3_125 - 1, -1, -1):
                v_junk_19 = 78
                if nums[v5_381] > nums[v3_125]:
                    v4_859 = 1
                    break
                elif nums[v5_381] < nums[v3_125]:
                    v4_859 = -1
                    break
            v6_350 = 0
            for v5_381 in range(v3_125 + 1, v2_214):
                v_junk_58 = 35
                if nums[v5_381] > nums[v3_125]:
                    v6_350 = 1
                    break
                elif nums[v5_381] < nums[v3_125]:
                    if len('abc') == 3:
                        v6_350 = -1
                    break
            if v4_859 == v6_350 and v4_859 != 0:
                v1_754 += 1
        return v1_754