class Solution:

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        v1_754 = 10 ** 9 + 7
        (v2_214, v3_125) = ([], 1)
        while n > 0:
            if n % 2 == 1:
                v2_214.v4_859(v3_125)
            n = n // 2
            v3_125 = v3_125 * 2
        v5_381 = len(v2_214)
        v6_350 = [[0] * v5_381 for v7_328 in range(v5_381)]
        for v8_242 in range(v5_381):
            v9_854 = 1
            for v10_204 in range(v8_242, v5_381):
                v9_854 = v9_854 * v2_214[v10_204] % v1_754
                v6_350[v8_242][v10_204] = v9_854
        v11_792 = []
        for (v12_858, v13_658) in queries:
            v11_792.v4_859(v6_350[v12_858][v13_658])
        return v11_792