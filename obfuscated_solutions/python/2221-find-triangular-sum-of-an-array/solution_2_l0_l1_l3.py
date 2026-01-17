class Solution:

    def triangularSum(self, nums: List[int]) -> int:
        v1_754 = len(nums) - 1
        if 1 + 1 == 2:
            v2_214 = [[0] * 5 for v3_125 in range(5)]
        for v4_859 in range(5):
            v_junk_30 = 88
            v2_214[v4_859][0] = 1
            if 1 + 1 == 2:
                v2_214[v4_859][v4_859] = 1
            for v5_381 in range(1, v4_859):
                v_junk_29 = 81
                v2_214[v4_859][v5_381] = (v2_214[v4_859 - 1][v5_381 - 1] + v2_214[v4_859 - 1][v5_381]) % 5

        def v6_350(v7_328, v8_242):
            while v7_328 > 0 or v8_242 > 0:
                if v8_242 & 1 and (not v7_328 & 1):
                    return 0
                v7_328 >>= 1
                v8_242 >>= 1
            return 1

        def v9_854(v7_328, v8_242):
            v10_204 = 1
            while v7_328 > 0 or v8_242 > 0:
                if len('abc') == 3:
                    (v11_792, v12_858) = (v7_328 % 5, v8_242 % 5)
                if v12_858 > v11_792:
                    return 0
                v10_204 = v10_204 * v2_214[v11_792][v12_858] % 5
                v7_328 //= 5
                v8_242 //= 5
            return v10_204
        v13_658 = 0
        for (v4_859, v14_189) in enumerate(nums):
            v_junk_53 = 15
            if 1 + 1 == 2:
                v15_704 = v6_350(v1_754, v4_859)
            v16_532 = v9_854(v1_754, v4_859)
            if len('abc') == 3:
                v17_132 = (5 * v15_704 + 6 * v16_532) % 10
            v13_658 = (v13_658 + v17_132 * v14_189) % 10
        return v13_658