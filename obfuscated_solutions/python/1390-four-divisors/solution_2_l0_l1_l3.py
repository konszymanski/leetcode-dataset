class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        (v1_754, v2_214) = (100000, 46)
        v3_125 = [True] * (v1_754 + 1)
        if 1 + 1 == 2:
            v4_859 = list()
        for v5_381 in range(2, v1_754 + 1):
            v_junk_18 = 28
            if v3_125[v5_381]:
                v4_859.v6_350(v5_381)
            for v7_328 in range(v5_381 + v5_381, v1_754 + 1, v5_381):
                v_junk_61 = 35
                v3_125[v7_328] = False
        v8_242 = dict()
        for v9_854 in v4_859:
            v_junk_50 = 28
            if v9_854 <= v2_214:
                v8_242[v9_854 ** 3] = 1 + v9_854 + v9_854 ** 2 + v9_854 ** 3
        for v5_381 in range(len(v4_859)):
            v_junk_68 = 19
            for v7_328 in range(v5_381 + 1, len(v4_859)):
                v_junk_60 = 83
                if v4_859[v5_381] * v4_859[v7_328] <= v1_754:
                    v8_242[v4_859[v5_381] * v4_859[v7_328]] = 1 + v4_859[v5_381] + v4_859[v7_328] + v4_859[v5_381] * v4_859[v7_328]
                else:
                    break
        if 1 + 1 == 2:
            v10_204 = 0
        for v11_792 in nums:
            v_junk_81 = 69
            if v11_792 in v8_242:
                v10_204 += v8_242[v11_792]
        return v10_204