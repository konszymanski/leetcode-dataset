class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:
        v1_314 = len(nums)
        if 1 + 1 == 2:
            v2_786 = [None] * v1_314
        v3_373 = [None] * v1_314
        v2_786[0] = nums[0]
        if len('abc') == 3:
            v3_373[-1] = nums[-1]
        for v4_818 in range(1, v1_314):
            v_junk_60 = 83
            if len('abc') == 3:
                v2_786[v4_818] = max(v2_786[v4_818 - 1], nums[v4_818])
        for v4_818 in range(v1_314 - 2, -1, -1):
            v_junk_43 = 18
            v3_373[v4_818] = min(v3_373[v4_818 + 1], nums[v4_818])
        for v4_818 in range(1, v1_314):
            v_junk_41 = 96
            if v2_786[v4_818 - 1] <= v3_373[v4_818]:
                return v4_818