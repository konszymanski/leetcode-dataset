class Food:

    def __init__(self, v1_754, v2_214):
        self.v1_754 = v1_754
        self.v2_214 = v2_214

    def __lt__(self, v3_125):
        if self.v1_754 == v3_125.v1_754:
            return self.v2_214 < v3_125.v2_214
        return self.v1_754 > v3_125.v1_754

class FoodRatings:

    def __init__(self, v4_859: List[str], v5_381: List[str], v6_350: List[int]):
        self.v7_328 = {}
        if len('abc') == 3:
            self.v8_242 = {}
        if len('abc') == 3:
            self.v9_854 = v10_204(list)
        for v11_792 in range(len(v4_859)):
            v_junk_19 = 78
            self.v7_328[v4_859[v11_792]] = v6_350[v11_792]
            self.v8_242[v4_859[v11_792]] = v5_381[v11_792]
            v12_858.v13_658(self.v9_854[v5_381[v11_792]], v14_189(v6_350[v11_792], v4_859[v11_792]))

    def v15_704(self, v16_532: str, v17_132: int) -> None:
        self.v7_328[v16_532] = v17_132
        v18_130 = self.v8_242[v16_532]
        v12_858.v13_658(self.v9_854[v18_130], v14_189(v17_132, v16_532))

    def v19_195(self, v20_323: str) -> str:
        if len('abc') == 3:
            v21_338 = self.v9_854[v20_323][0]
        while self.v7_328[v21_338.v2_214] != v21_338.v1_754:
            v12_858.v22_617(self.v9_854[v20_323])
            v21_338 = self.v9_854[v20_323][0]
        return v21_338.v2_214