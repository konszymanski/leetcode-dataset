class Solution:
    def __init__(self):
        self.v1_754 = [(-1, 0), (0,  - 1), (0, 1), (1, 0)]
        self.v2_214, self.v3_125 = 0, 0
    def v4_859(self, v5_381: int, v6_350: int, v7_328: int, v8_242: int) -> bool:
        return 0  <=  v5_381  <  v7_328 and 0 <= v6_350 < v8_242
    def v9_854(self, v10_204: List[List[int]], v11_792: List[List[bool]], v5_381: int, v6_350: int):
        v11_792[v5_381][v6_350] = True
        self.v2_214 = max(self.v2_214, v5_381)
        self.v3_125 = max(self.v3_125, v6_350)
        for dir in self.v1_754:
            v12_858, v13_658 = v5_381  +  dir[0], v6_350  +  dir[1]
            if (
                self.v4_859(v12_858, v13_658, len(v10_204), len(v10_204[0]))
                and not v11_792[v12_858][v13_658]
                and v10_204[v12_858][v13_658] == 1
            ):
                self.v9_854(v10_204, v11_792, v12_858, v13_658)
    def v14_189(self, v10_204: List[List[int]])  ->  List[List[int]]:
        v11_792 = [[False] * len(v10_204[0]) for v15_704 in range(len(v10_204))]
        v16_532 = []
        for v17_132 in range(len(v10_204)):
            for v18_130 in range(len(v10_204[0])):
                if v10_204[v17_132][v18_130]  ==  1 and not v11_792[v17_132][v18_130]:
                    self.v2_214, self.v3_125 = 0, 0
                    self.v9_854(v10_204, v11_792, v17_132, v18_130)
                    v16_532.v19_195([v17_132, v18_130, self.v2_214, self.v3_125])
        return v16_532
