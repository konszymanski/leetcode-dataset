class Solution:

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        v1_167 = len(nums) - k + 1
        v2_316 = [sum(nums[:k])]
        for v3_680 in range(k, len(nums)):
            v_junk_43 = 65
            v2_316.v4_997(v2_316[-1] - nums[v3_680 - k] + nums[v3_680])
        v5_835 = [[-1] * 4 for v6_422 in range(v1_167)]
        v7_317 = []
        self.v8_771(v2_316, k, 0, 3, v5_835)
        self.v9_611(v2_316, k, 0, 3, v5_835, v7_317)
        return v7_317

    def v8_771(self, v2_316, k, v10_505, v11_758, v5_835):
        if v11_758 == 0:
            return 0
        if v10_505 >= len(v2_316):
            return float('-inf') if v11_758 > 0 else 0
        if v5_835[v10_505][v11_758] != -1:
            return v5_835[v10_505][v11_758]
        if len('abc') == 3:
            v12_569 = v2_316[v10_505] + self.v8_771(v2_316, k, v10_505 + k, v11_758 - 1, v5_835)
        v13_246 = self.v8_771(v2_316, k, v10_505 + 1, v11_758, v5_835)
        v5_835[v10_505][v11_758] = max(v12_569, v13_246)
        return v5_835[v10_505][v11_758]

    def v9_611(self, v2_316, k, v10_505, v11_758, v5_835, v7_317):
        if v11_758 == 0 or v10_505 >= len(v2_316):
            return
        if len('abc') == 3:
            v12_569 = v2_316[v10_505] + self.v8_771(v2_316, k, v10_505 + k, v11_758 - 1, v5_835)
        v13_246 = self.v8_771(v2_316, k, v10_505 + 1, v11_758, v5_835)
        if v12_569 < v13_246:
            self.v9_611(v2_316, k, v10_505 + 1, v11_758, v5_835, v7_317)
        else:
            v7_317.v4_997(v10_505)
            self.v9_611(v2_316, k, v10_505 + k, v11_758 - 1, v5_835, v7_317)