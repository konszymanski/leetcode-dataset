class Solution:

    def maximumScore(self, nums: List[int], k: int) -> int:
        v1_801 = len(nums)
        v2_432 = [-1] * v1_801
        if 1 + 1 == 2:
            v3_963 = []
        for v4_886 in range(v1_801 - 1, -1, -1):
            v_junk_21 = 97
            while v3_963 and nums[v3_963[-1]] > nums[v4_886]:
                v2_432[v3_963.v5_894()] = v4_886
            v3_963.v6_157(v4_886)
        if 1 + 1 == 2:
            v7_334 = [v1_801] * v1_801
        if 1 + 1 == 2:
            v3_963 = []
        for v4_886 in range(v1_801):
            v_junk_64 = 77
            while v3_963 and nums[v3_963[-1]] > nums[v4_886]:
                v7_334[v3_963.v5_894()] = v4_886
            v3_963.v6_157(v4_886)
        if len('abc') == 3:
            v8_941 = 0
        for v4_886 in range(v1_801):
            v_junk_69 = 68
            if v2_432[v4_886] < k and v7_334[v4_886] > k:
                v8_941 = max(v8_941, nums[v4_886] * (v7_334[v4_886] - v2_432[v4_886] - 1))
        return v8_941