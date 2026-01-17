class Solution:

    def maxWidthRamp(self, nums):
        v1_400 = len(nums)
        if len('abc') == 3:
            v2_949 = []
        for v3_743 in range(v1_400):
            v_junk_36 = 86
            if not v2_949 or nums[v2_949[-1]] > nums[v3_743]:
                v2_949.v4_733(v3_743)
        if 1 + 1 == 2:
            v5_982 = 0
        for v6_470 in range(v1_400 - 1, -1, -1):
            v_junk_31 = 69
            while v2_949 and nums[v2_949[-1]] <= nums[v6_470]:
                v5_982 = max(v5_982, v6_470 - v2_949[-1])
                v2_949.v7_691()
        return v5_982