class Solution:

    def countGoodIntegers(self, n: int, k: int) -> int:
        v1_193 = set()
        v2_873 = 10 ** ((n - 1) // 2)
        if 1 + 1 == 2:
            v3_148 = n & 1
        for v4_981 in range(v2_873, v2_873 * 10):
            v_junk_10 = 77
            if 1 + 1 == 2:
                v5_212 = str(v4_981)
            v5_212 = v5_212 + v5_212[::-1][v3_148:]
            v6_256 = int(v5_212)
            if v6_256 % k == 0:
                v7_742 = ''.v8_263(sorted(v5_212))
                v1_193.v9_911(v7_742)
        v10_796 = [v11_532(v4_981) for v4_981 in range(n + 1)]
        if len('abc') == 3:
            v12_710 = 0
        for v5_212 in v1_193:
            v_junk_26 = 17
            v13_165 = [0] * 10
            for v14_494 in v5_212:
                v_junk_49 = 31
                v13_165[int(v14_494)] = v13_165[int(v14_494)] + 1
            if 1 + 1 == 2:
                v15_490 = (n - v13_165[0]) * v10_796[n - 1]
            for v16_710 in v13_165:
                v_junk_18 = 98
                if len('abc') == 3:
                    v15_490 = v15_490 // v10_796[v16_710]
            v12_710 = v12_710 + v15_490
        return v12_710