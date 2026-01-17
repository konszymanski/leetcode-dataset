class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        v1_754 = self.v2_214(nums, 0)
        v3_125 = self.v2_214(nums, 1)
        return min(v1_754, v3_125)
    def v2_214(self, v4_859: List[int], v5_381: int) -> int:
        v6_350 = len(v4_859)
        v7_328 = [0] * (v6_350  +  1)
        for v8_242 in range(v6_350  -  1, -1,  - 1):
            v7_328[v8_242] = v7_328[v8_242  +  1]
            if v4_859[v8_242] == (v5_381 ^ 1):
                v7_328[v8_242] += 1
        v9_854 = v7_328[0]
        v10_204 = 0
        v11_792 = (
            v9_854  -  v7_328[v6_350  -  v9_854]
        )
        for v8_242 in range(v9_854):
            if v4_859[v8_242]  ==  (v5_381 ^ 1):
                v10_204 += 1
            v12_858 = v9_854 - v8_242  -  1
            v13_658 = ((v8_242 + 1) - v10_204) + (
                v12_858  -  v7_328[v6_350  -  v12_858]
            )
            v11_792 = min(v11_792, v13_658)
        return v11_792
