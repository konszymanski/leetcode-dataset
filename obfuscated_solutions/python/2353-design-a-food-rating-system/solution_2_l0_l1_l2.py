from sortedcontainers import v1_754

class FoodRatings:

    def __init__(self, v2_214: List[str], v3_125: List[str], v4_859: List[int]):
        self.v5_381 = {}
        self.v6_350 = {}
        self.v7_328 = v8_242(v1_754)
        for v9_854 in range(len(v2_214)):
            self.v5_381[v2_214[v9_854]] = v4_859[v9_854]
            self.v6_350[v2_214[v9_854]] = v3_125[v9_854]
            self.v7_328[v3_125[v9_854]].v10_204((-v4_859[v9_854], v2_214[v9_854]))

    def v11_792(self, v12_858: str, v13_658: int) -> None:
        v14_189 = self.v6_350[v12_858]
        v15_704 = (-self.v5_381[v12_858], v12_858)
        self.v7_328[v14_189].v16_532(v15_704)
        self.v5_381[v12_858] = v13_658
        self.v7_328[v14_189].v10_204((-v13_658, v12_858))

    def v17_132(self, v18_130: str) -> str:
        v19_195 = self.v7_328[v18_130][0]
        return v19_195[1]