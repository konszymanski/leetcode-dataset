class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        v1_754 = v2_214.v3_125(k)
        v4_859 = [0]
        for v5_381 in nums:
            v4_859.v6_350(v4_859[-1] + v2_214.v3_125(v5_381))
        v7_328 = 0
        for v8_242 in range(len(v4_859)):
            (v9_854, v10_204) = (v8_242 + 1, len(v4_859))
            while v9_854 < v10_204:
                v11_792 = (v9_854 + v10_204) // 2
                if v4_859[v11_792] >= v4_859[v8_242] + v1_754 - 1e-09:
                    v10_204 = v11_792
                else:
                    v9_854 = v11_792 + 1
            v7_328 = v7_328 + (v9_854 - v8_242 - 1)
        return v7_328