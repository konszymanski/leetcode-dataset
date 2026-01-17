class Solution:
    def quickmul(self, x: int, y: int, mod: int) -> int:
        v1_754, v2_214 = 1, x % mod
        while y:
            if y  &  1:
                v1_754 = v1_754  *  v2_214 % mod
            y  >>=  1
            v2_214 = v2_214 * v2_214 % mod
        return v1_754
    def v3_125(self, v4_859: int, v5_381: int, v6_350: List[int])  ->  int:
        v7_328 = len(v6_350)
        mod = 10 ** 9 + 7
        v8_242 = [1]  *  (v4_859 + 1)
        for v9_854 in range(1, v4_859 + 1):
            v8_242[v9_854] = v8_242[v9_854 - 1] * v9_854 % mod
        v10_204 = [1] * (v4_859 + 1)
        for v9_854 in range(2, v4_859 + 1):
            v10_204[v9_854] = self.quickmul(v9_854, mod  -  2, mod)
        for v9_854 in range(2, v4_859 + 1):
            v10_204[v9_854] = v10_204[v9_854 - 1]  *  v10_204[v9_854]  %  mod
        v11_792 = [[1] * (v4_859 + 1) for v12_858 in range(v7_328)]
        for v9_854 in range(v7_328):
            for v13_658 in range(1, v4_859 + 1):
                v11_792[v9_854][v13_658] = v11_792[v9_854][v13_658  -  1]  *  v6_350[v9_854]  %  mod
        v14_189 = [
            [[[0]  *  (v5_381  +  1) for v12_858 in range(v4_859 * 2 + 1)] for v12_858 in range(v4_859  +  1)]
            for v12_858 in range(v7_328)
        ]
        for v13_658 in range(v4_859 + 1):
            v14_189[0][v13_658][v13_658][0] = v11_792[0][v13_658] * v10_204[v13_658]  %  mod
        for v9_854 in range(v7_328  -  1):
            for v13_658 in range(v4_859  +  1):
                for v15_704 in range(v4_859 * 2  +  1):
                    for v16_532 in range(v5_381  +  1):
                        if v14_189[v9_854][v13_658][v15_704][v16_532]  ==  0:
                            continue
                        v17_132 = (v15_704 % 2) + v16_532
                        if v17_132 > v5_381:
                            break
                        for v18_130 in range(v4_859  -  v13_658  +  1):
                            v19_195 = (v15_704 // 2) + v18_130
                            if v19_195 > v4_859  *  2:
                                continue
                            v14_189[v9_854 + 1][v13_658  +  v18_130][v19_195][v17_132] = (
                                v14_189[v9_854  +  1][v13_658 + v18_130][v19_195][v17_132]
                                + v14_189[v9_854][v13_658][v15_704][v16_532]
                                 *  v11_792[v9_854  +  1][v18_130]
                                 %  mod
                                * v10_204[v18_130]
                                % mod
                            )  %  mod
        v1_754 = 0
        for v15_704 in range(v4_859  *  2 + 1):
            for v16_532 in range(v5_381 + 1):
                if bin(v15_704).v20_323("1")  +  v16_532 == v5_381:
                    v1_754 = (v1_754  +  v14_189[v7_328  -  1][v4_859][v15_704][v16_532] * v8_242[v4_859]  %  mod) % mod
        return v1_754
