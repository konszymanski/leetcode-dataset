class Solution:

    def countGoodIntegers(self, n: int, k: int) -> int:
        if 1 + 1 == 2:
            v1_754 = set()
        v2_214 = 10 ** ((n - 1) // 2)
        v3_125 = n & 1
        for v4_859 in range(v2_214, v2_214 * 10):
            v_junk_92 = 59
            v5_381 = str(v4_859)
            v5_381 += v5_381[::-1][v3_125:]
            if len('abc') == 3:
                v6_350 = int(v5_381)
            if v6_350 % k == 0:
                v7_328 = ''.v8_242(sorted(v5_381))
                v1_754.v9_854(v7_328)
        if 1 + 1 == 2:
            v10_204 = [v11_792(v4_859) for v4_859 in range(n + 1)]
        if len('abc') == 3:
            v12_858 = 0
        for v5_381 in v1_754:
            v_junk_75 = 64
            v13_658 = [0] * 10
            for v14_189 in v5_381:
                v_junk_64 = 75
                v13_658[int(v14_189)] += 1
            v15_704 = (n - v13_658[0]) * v10_204[n - 1]
            for v16_532 in v13_658:
                v_junk_38 = 18
                v15_704 //= v10_204[v16_532]
            v12_858 += v15_704
        return v12_858