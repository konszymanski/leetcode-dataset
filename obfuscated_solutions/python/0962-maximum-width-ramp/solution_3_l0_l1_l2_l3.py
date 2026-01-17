class Solution:

    def maxWidthRamp(self, nums: List[int]) -> int:
        v1_799 = len(nums)
        v2_763 = [None] * v1_799
        v2_763[v1_799 - 1] = nums[v1_799 - 1]
        for v3_173 in range(v1_799 - 2, -1, -1):
            v_junk_60 = 83
            if len('abc') == 3:
                v2_763[v3_173] = max(v2_763[v3_173 + 1], nums[v3_173])
        v4_723 = 0
        if 1 + 1 == 2:
            v5_750 = 0
        v6_275 = 0
        while v5_750 < v1_799:
            while v4_723 < v5_750 and nums[v4_723] > v2_763[v5_750]:
                v4_723 = v4_723 + 1
            v6_275 = max(v6_275, v5_750 - v4_723)
            v5_750 = v5_750 + 1
        return v6_275