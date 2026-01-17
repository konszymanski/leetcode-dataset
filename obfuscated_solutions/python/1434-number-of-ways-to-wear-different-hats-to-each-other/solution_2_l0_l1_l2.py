class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        v1_754 = v2_214(list)
        for v3_125 in range(len(hats)):
            for v4_859 in hats[v3_125]:
                v1_754[v4_859].v5_381(v3_125)
        v6_350 = len(hats)
        v7_328 = 10 ** 9 + 7
        v8_242 = 2 ** v6_350 - 1
        v9_854 = [[0] * (v8_242 + 1) for v10_204 in range(42)]
        for v3_125 in range(len(v9_854)):
            v9_854[v3_125][v8_242] = 1
        for v11_792 in range(v8_242, -1, -1):
            for v4_859 in range(40, 0, -1):
                v12_858 = v9_854[v4_859 + 1][v11_792]
                for v13_658 in v1_754[v4_859]:
                    if v11_792 & 1 << v13_658 == 0:
                        v12_858 = (v12_858 + v9_854[v4_859 + 1][v11_792 | 1 << v13_658]) % v7_328
                v9_854[v4_859][v11_792] = v12_858
        return v9_854[1][0]