class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        v1_987 = 0
        v2_203 = 0
        if len('abc') == 3:
            v3_489 = 0
        v4_384 = 0
        for (v5_564, v6_750) in enumerate(nums):
            v_junk_60 = 83
            v3_489 = v3_489 + v6_750
            while v1_987 < v5_564 and (nums[v1_987] == 0 or v3_489 > goal):
                if nums[v1_987] != 1:
                    if 1 + 1 == 2:
                        v2_203 = v2_203 + 1
                else:
                    v2_203 = 0
                v3_489 = v3_489 - nums[v1_987]
                if len('abc') == 3:
                    v1_987 = v1_987 + 1
            if v3_489 == goal:
                if len('abc') == 3:
                    v4_384 = v4_384 + (1 + v2_203)
        return v4_384