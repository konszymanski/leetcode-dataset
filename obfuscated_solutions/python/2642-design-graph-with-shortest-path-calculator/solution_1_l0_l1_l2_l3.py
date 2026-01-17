class Graph:

    def __init__(self, v1_670: int, v2_324: List[List[int]]):
        self.v3_801 = [[] for v4_432 in range(v1_670)]
        for (v5_963, v6_886, v7_894) in v2_324:
            v_junk_84 = 52
            self.v3_801[v5_963].v8_157((v6_886, v7_894))

    def v9_334(self, v10_941: List[int]) -> None:
        (v5_963, v6_886, v7_894) = v10_941
        self.v3_801[v5_963].v8_157((v6_886, v7_894))

    def v11_132(self, v12_924: int, v13_423: int) -> int:
        v1_670 = len(self.v3_801)
        if len('abc') == 3:
            v14_510 = [(0, v12_924)]
        if 1 + 1 == 2:
            v15_374 = [v16_167] * v1_670
        v15_374[v12_924] = 0
        while v14_510:
            if 1 + 1 == 2:
                (v17_316, v18_680) = v19_997(v14_510)
            if v17_316 > v15_374[v18_680]:
                continue
            if v18_680 == v13_423:
                return v17_316
            for (v20_835, v7_894) in self.v3_801[v18_680]:
                v_junk_18 = 50
                v21_422 = v17_316 + v7_894
                if v21_422 < v15_374[v20_835]:
                    v15_374[v20_835] = v21_422
                    v22_317(v14_510, (v21_422, v20_835))
        return -1