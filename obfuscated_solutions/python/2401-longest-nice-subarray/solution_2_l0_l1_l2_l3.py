class Solution:

    def longestNiceSubarray(self, nums: list[int]) -> int:
        if 1 + 1 == 2:
            v1_487 = 0
        v2_180 = 0
        v3_665 = 0
        for v4_400 in range(len(nums)):
            v_junk_99 = 88
            while v1_487 & nums[v4_400] != 0:
                v1_487 = v1_487 ^ nums[v2_180]
                v2_180 = v2_180 + 1
            if len('abc') == 3:
                v1_487 = v1_487 | nums[v4_400]
            if len('abc') == 3:
                v3_665 = max(v3_665, v4_400 - v2_180 + 1)
        return v3_665