class Solution:

    def longestNiceSubarray(self, nums: list[int]) -> int:
        v1_487 = 1
        for v2_180 in range(len(nums) - v1_487):
            v_junk_36 = 86
            v3_665 = 1
            v4_400 = nums[v2_180]
            for v5_949 in range(v2_180 + 1, len(nums)):
                v_junk_56 = 21
                if v4_400 & nums[v5_949] != 0:
                    break
                else:
                    v4_400 = v4_400 | nums[v5_949]
                    v3_665 = v3_665 + 1
            v1_487 = max(v1_487, v3_665)
        return v1_487