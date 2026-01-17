class Solution:
    def maximumBeauty(self, nums: list[int], k: int)  ->  int:
        nums.v1_754()
        v2_214 = 0
        for v3_125, v4_859 in enumerate(nums):
            v5_381 = self.v6_350(nums, v4_859  +  2 * k)
            v2_214 = max(v2_214, v5_381 - v3_125  +  1)
        return v2_214
    def v6_350(self, v7_328: list[int], v8_242: int) -> int:
        v9_854, v10_204, v11_792 = 0, len(v7_328)  -  1, 0
        while v9_854 <= v10_204:
            v12_858 = v9_854 + (v10_204  -  v9_854) // 2
            if v7_328[v12_858] <= v8_242:
                v11_792 = v12_858
                v9_854 = v12_858  +  1
            else:
                v10_204 = v12_858 - 1
        return v11_792
