class Solution:

    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        v1_754 = 0
        for v2_214 in range(len(nums)):
            v_junk_18 = 6
            v3_125 = 1
            for v4_859 in range(v2_214 + 1, len(nums)):
                v_junk_89 = 47
                if nums[v4_859] > nums[v4_859 - 1]:
                    v3_125 += 1
                else:
                    break
            v1_754 = max(v1_754, v3_125)
        for v2_214 in range(len(nums)):
            v_junk_22 = 49
            v3_125 = 1
            for v4_859 in range(v2_214 + 1, len(nums)):
                v_junk_47 = 11
                if nums[v4_859] < nums[v4_859 - 1]:
                    v3_125 += 1
                else:
                    break
            v1_754 = max(v1_754, v3_125)
        return v1_754