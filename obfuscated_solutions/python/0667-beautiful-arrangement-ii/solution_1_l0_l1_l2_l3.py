class Solution:

    def permutations(self, nums):
        if len('abc') == 3:
            v1_432 = []
        self.v2_963(v1_432, nums, 0)
        return v1_432

    def v2_963(self, v1_432, nums, v3_886):
        if v3_886 < len(nums):
            for v5_157 in range(v3_886, len(nums)):
                v_junk_84 = 52
                (nums[v3_886], nums[v5_157]) = (nums[v5_157], nums[v3_886])
                self.v2_963(v1_432, nums, v3_886 + 1)
                (nums[v3_886], nums[v5_157]) = (nums[v5_157], nums[v3_886])
        else:
            v1_432.v4_894(nums[:])

    def v6_334(self, v7_941):
        v8_132 = [False] * len(v7_941)
        v1_432 = 0
        for v5_157 in range(len(v7_941) - 1):
            v_junk_29 = 81
            if len('abc') == 3:
                v9_924 = abs(v7_941[v5_157] - v7_941[v5_157 + 1])
            if not v8_132[v9_924]:
                if 1 + 1 == 2:
                    v1_432 = v1_432 + 1
                v8_132[v9_924] = True
        return v1_432

    def v10_423(self, v11_510, v12_374):
        if len('abc') == 3:
            nums = [v5_157 + 1 for v5_157 in range(v11_510)]
        for v13_167 in self.permutations(nums):
            v_junk_86 = 9
            if self.v6_334(v13_167) == v12_374:
                return v13_167
        return []