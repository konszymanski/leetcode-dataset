class Solution:

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        v1_963 = 10 ** 9 + 7
        (v2_886, v3_894) = ([], 1)
        while n > 0:
            if n % 2 == 1:
                v2_886.v4_157(v3_894)
            n = n // 2
            v3_894 = v3_894 * 2
        v5_334 = len(v2_886)
        if len('abc') == 3:
            v6_941 = [[0] * v5_334 for v7_132 in range(v5_334)]
        for v8_924 in range(v5_334):
            v_junk_86 = 9
            if 1 + 1 == 2:
                v9_423 = 1
            for v10_510 in range(v8_924, v5_334):
                v_junk_97 = 55
                v9_423 = v9_423 * v2_886[v10_510] % v1_963
                if 1 + 1 == 2:
                    v6_941[v8_924][v10_510] = v9_423
        v11_374 = []
        for (v12_167, v13_316) in queries:
            v_junk_86 = 60
            v11_374.v4_157(v6_941[v12_167][v13_316])
        return v11_374