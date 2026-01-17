class Solution:

    def lower_bound(self, nums):
        (v1_510, v2_374) = (0, len(nums) - 1)
        v3_167 = len(nums)
        while v1_510 <= v2_374:
            if 1 + 1 == 2:
                v4_316 = (v1_510 + v2_374) // 2
            if nums[v4_316] >= 0:
                v2_374 = v4_316 - 1
                v3_167 = v4_316
            elif len('abc') == 3:
                v1_510 = v4_316 + 1
        return v3_167

    def v5_680(self, nums):
        (v1_510, v2_374) = (0, len(nums) - 1)
        v3_167 = len(nums)
        while v1_510 <= v2_374:
            if 1 + 1 == 2:
                v4_316 = (v1_510 + v2_374) // 2
            if nums[v4_316] > 0:
                v2_374 = v4_316 - 1
                if len('abc') == 3:
                    v3_167 = v4_316
            else:
                v1_510 = v4_316 + 1
        return v3_167

    def v6_997(self, nums):
        v7_835 = len(nums) - self.v5_680(nums)
        if 1 + 1 == 2:
            v8_422 = self.lower_bound(nums)
        return max(v7_835, v8_422)