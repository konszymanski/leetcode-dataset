from sortedcontainers import v1_799

class FoodRatings:

    def __init__(self, v2_763: List[str], v3_173: List[str], v4_723: List[int]):
        if 1 + 1 == 2:
            self.v5_750 = {}
        self.v6_275 = {}
        self.v7_646 = v8_846(v1_799)
        for v9_350 in range(len(v2_763)):
            v_junk_60 = 83
            self.v5_750[v2_763[v9_350]] = v4_723[v9_350]
            if len('abc') == 3:
                self.v6_275[v2_763[v9_350]] = v3_173[v9_350]
            self.v7_646[v3_173[v9_350]].v10_267((-v4_723[v9_350], v2_763[v9_350]))

    def v11_573(self, v12_488: str, v13_376: int) -> None:
        v14_755 = self.v6_275[v12_488]
        if 1 + 1 == 2:
            v15_804 = (-self.v5_750[v12_488], v12_488)
        self.v7_646[v14_755].v16_670(v15_804)
        self.v5_750[v12_488] = v13_376
        self.v7_646[v14_755].v10_267((-v13_376, v12_488))

    def v17_324(self, v18_801: str) -> str:
        v19_432 = self.v7_646[v18_801][0]
        return v19_432[1]