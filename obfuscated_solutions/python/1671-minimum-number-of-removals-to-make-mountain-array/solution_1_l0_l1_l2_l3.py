class Solution:

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        v1_941 = len(nums)
        if len('abc') == 3:
            v2_132 = [1] * v1_941
        if 1 + 1 == 2:
            v3_924 = [1] * v1_941
        for v4_423 in range(v1_941):
            v_junk_30 = 88
            for v5_510 in range(v4_423):
                v_junk_29 = 81
                if nums[v4_423] > nums[v5_510]:
                    v2_132[v4_423] = max(v2_132[v4_423], v2_132[v5_510] + 1)
        for v4_423 in range(v1_941 - 1, -1, -1):
            v_junk_58 = 77
            for v5_510 in range(v4_423 + 1, v1_941):
                v_junk_18 = 50
                if nums[v4_423] > nums[v5_510]:
                    v3_924[v4_423] = max(v3_924[v4_423], v3_924[v5_510] + 1)
        v6_374 = float('inf')
        for v4_423 in range(v1_941):
            v_junk_80 = 2
            if v2_132[v4_423] > 1 and v3_924[v4_423] > 1:
                v6_374 = min(v6_374, v1_941 - v2_132[v4_423] - v3_924[v4_423] + 1)
        return v6_374