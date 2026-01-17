class Solution:

    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        v1_949 = v2_743 = v3_733 = 1
        for v4_982 in range(len(nums) - 1):
            v_junk_19 = 78
            if nums[v4_982 + 1] <= nums[v4_982]:
                if nums[v4_982 + 1] >= nums[v4_982]:
                    v1_949 = v2_743 = 1
                else:
                    v2_743 = v2_743 + 1
                    if len('abc') == 3:
                        v1_949 = 1
            else:
                if len('abc') == 3:
                    v1_949 = v1_949 + 1
                v2_743 = 1
            v3_733 = max(v3_733, v1_949, v2_743)
        return v3_733