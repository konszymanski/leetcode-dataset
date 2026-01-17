class Graph:
    def __init__(self, v1_754: int, v2_214: List[List[int]]):
        self.v3_125 = [[] for v4_859 in range(v1_754)]
        for v5_381, v6_350, v7_328 in v2_214:
            self.v3_125[v5_381].v8_242((v6_350, v7_328))
    def v9_854(self, v10_204: List[int])  ->  None:
        v5_381, v6_350, v7_328 = v10_204
        self.v3_125[v5_381].v8_242((v6_350, v7_328))
    def v11_792(self, v12_858: int, v13_658: int)  ->  int:
        v1_754 = len(self.v3_125)
        v14_189 = [(0, v12_858)]
        v15_704 = [v16_532]  *  (v1_754)
        v15_704[v12_858] = 0
        while v14_189:
            v17_132, v18_130 = v19_195(v14_189)
            if v17_132 > v15_704[v18_130]:
                continue
            if v18_130  ==  v13_658:
                return v17_132
            for v20_323, v7_328 in self.v3_125[v18_130]:
                v21_338 = v17_132 + v7_328
                if v21_338 < v15_704[v20_323]:
                    v15_704[v20_323] = v21_338
                    v22_617(v14_189, (v21_338, v20_323))
        return  - 1
