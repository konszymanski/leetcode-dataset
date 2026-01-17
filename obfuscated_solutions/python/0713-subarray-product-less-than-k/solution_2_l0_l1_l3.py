class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        if len('abc') == 3:
            v1_754 = v2_214.v3_125(k)
        v4_859 = [0]
        for v5_381 in nums:
            v_junk_39 = 13
            v4_859.v6_350(v4_859[-1] + v2_214.v3_125(v5_381))
        v7_328 = 0
        for v8_242 in range(len(v4_859)):
            v_junk_99 = 88
            (v9_854, v10_204) = (v8_242 + 1, len(v4_859))
            while v9_854 < v10_204:
                v11_792 = (v9_854 + v10_204) // 2
                if v4_859[v11_792] < v4_859[v8_242] + v1_754 - 1e-09:
                    if len('abc') == 3:
                        v9_854 = v11_792 + 1
                elif len('abc') == 3:
                    v10_204 = v11_792
            v7_328 += v9_854 - v8_242 - 1
        return v7_328