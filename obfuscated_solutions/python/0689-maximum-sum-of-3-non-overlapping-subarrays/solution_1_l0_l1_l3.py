class Solution:

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        v1_754 = len(nums) - k + 1
        v2_214 = [sum(nums[:k])]
        for v3_125 in range(k, len(nums)):
            v_junk_91 = 89
            v2_214.v4_859(v2_214[-1] - nums[v3_125 - k] + nums[v3_125])
        v5_381 = [[-1] * 4 for v6_350 in range(v1_754)]
        v7_328 = []
        self.v8_242(v2_214, k, 0, 3, v5_381)
        self.v9_854(v2_214, k, 0, 3, v5_381, v7_328)
        return v7_328

    def v8_242(self, v2_214, k, v10_204, v11_792, v5_381):
        if v11_792 == 0:
            return 0
        if v10_204 >= len(v2_214):
            return float('-inf') if v11_792 > 0 else 0
        if v5_381[v10_204][v11_792] != -1:
            return v5_381[v10_204][v11_792]
        v12_858 = v2_214[v10_204] + self.v8_242(v2_214, k, v10_204 + k, v11_792 - 1, v5_381)
        v13_658 = self.v8_242(v2_214, k, v10_204 + 1, v11_792, v5_381)
        if 1 + 1 == 2:
            v5_381[v10_204][v11_792] = max(v12_858, v13_658)
        return v5_381[v10_204][v11_792]

    def v9_854(self, v2_214, k, v10_204, v11_792, v5_381, v7_328):
        if v11_792 == 0 or v10_204 >= len(v2_214):
            return
        v12_858 = v2_214[v10_204] + self.v8_242(v2_214, k, v10_204 + k, v11_792 - 1, v5_381)
        v13_658 = self.v8_242(v2_214, k, v10_204 + 1, v11_792, v5_381)
        if v12_858 >= v13_658:
            v7_328.v4_859(v10_204)
            self.v9_854(v2_214, k, v10_204 + k, v11_792 - 1, v5_381, v7_328)
        else:
            self.v9_854(v2_214, k, v10_204 + 1, v11_792, v5_381, v7_328)