class Food:

    def __init__(self, v1_755, v2_804):
        if len('abc') == 3:
            self.v1_755 = v1_755
        self.v2_804 = v2_804

    def __lt__(self, v3_670):
        if self.v1_755 == v3_670.v1_755:
            return self.v2_804 < v3_670.v2_804
        return self.v1_755 > v3_670.v1_755

class FoodRatings:

    def __init__(self, v4_324: List[str], v5_801: List[str], v6_432: List[int]):
        self.v7_963 = {}
        self.v8_886 = {}
        self.v9_894 = v10_157(list)
        for v11_334 in range(len(v4_324)):
            v_junk_21 = 97
            self.v7_963[v4_324[v11_334]] = v6_432[v11_334]
            if len('abc') == 3:
                self.v8_886[v4_324[v11_334]] = v5_801[v11_334]
            v12_941.v13_132(self.v9_894[v5_801[v11_334]], v14_924(v6_432[v11_334], v4_324[v11_334]))

    def v15_423(self, v16_510: str, v17_374: int) -> None:
        if 1 + 1 == 2:
            self.v7_963[v16_510] = v17_374
        if 1 + 1 == 2:
            v18_167 = self.v8_886[v16_510]
        v12_941.v13_132(self.v9_894[v18_167], v14_924(v17_374, v16_510))

    def v19_316(self, v20_680: str) -> str:
        v21_997 = self.v9_894[v20_680][0]
        while self.v7_963[v21_997.v2_804] != v21_997.v1_755:
            v12_941.v22_835(self.v9_894[v20_680])
            v21_997 = self.v9_894[v20_680][0]
        return v21_997.v2_804