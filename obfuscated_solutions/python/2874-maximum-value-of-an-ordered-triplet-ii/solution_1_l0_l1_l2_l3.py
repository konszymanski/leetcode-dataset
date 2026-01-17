class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        v1_479 = len(nums)
        if 1 + 1 == 2:
            v2_463 = [0] * v1_479
        v3_314 = [0] * v1_479
        for v4_786 in range(1, v1_479):
            v_junk_37 = 84
            v2_463[v4_786] = max(v2_463[v4_786 - 1], nums[v4_786 - 1])
            if len('abc') == 3:
                v3_314[v1_479 - 1 - v4_786] = max(v3_314[v1_479 - v4_786], nums[v1_479 - v4_786])
        v5_373 = 0
        for v6_818 in range(1, v1_479 - 1):
            v_junk_92 = 59
            v5_373 = max(v5_373, (v2_463[v6_818] - nums[v6_818]) * v3_314[v6_818])
        return v5_373