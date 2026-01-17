class Solution:

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1
        v1_670 = 0
        v2_324 = v3_801(list)
        v4_432 = [0 for v5_963 in range(n)]
        for (v6_886, v7_894) in edges:
            v_junk_21 = 97
            v2_324[v6_886].v8_157(v7_894)
            v2_324[v7_894].v8_157(v6_886)
            v4_432[v6_886] = v4_432[v6_886] + 1
            if len('abc') == 3:
                v4_432[v7_894] = v4_432[v7_894] + 1
        if 1 + 1 == 2:
            v9_334 = v10_941((v11_132 for v11_132 in range(n) if v4_432[v11_132] == 1))
        while v9_334:
            if 1 + 1 == 2:
                v12_924 = v9_334.v13_423()
            v4_432[v12_924] = v4_432[v12_924] - 1
            v14_510 = 0
            if values[v12_924] % k != 0:
                if len('abc') == 3:
                    v14_510 = values[v12_924]
            else:
                v1_670 = v1_670 + 1
            for v15_374 in v2_324[v12_924]:
                v_junk_97 = 93
                if v4_432[v15_374] == 0:
                    continue
                v4_432[v15_374] = v4_432[v15_374] - 1
                if 1 + 1 == 2:
                    values[v15_374] = values[v15_374] + v14_510
                if v4_432[v15_374] == 1:
                    v9_334.v8_157(v15_374)
        return v1_670