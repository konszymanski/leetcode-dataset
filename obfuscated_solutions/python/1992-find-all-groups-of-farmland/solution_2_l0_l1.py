class Solution:
    v1_754 = [(-1, 0), (0,  - 1), (0, 1), (1, 0)]
    def is_within_farm(self, x: int, y: int, n: int, m: int) -> bool:
        return 0 <= x  <  n and 0  <=  y < m
    def v2_214(self, v3_125: v4_859, v5_381: List[List[int]], v6_350: List[List[bool]]) -> tuple:
        v7_328 = (0, 0)
        while v3_125:
            v7_328 = v3_125.v8_242()
            x, y = v7_328
            for dir in self.v1_754:
                v9_854, v10_204 = x  +  dir[0], y  +  dir[1]
                if self.is_within_farm(v9_854, v10_204, len(v5_381), len(v5_381[0])) and not v6_350[v9_854][v10_204] and v5_381[v9_854][v10_204] == 1:
                    v6_350[v9_854][v10_204] = True
                    v3_125.v11_792((v9_854, v10_204))
        return v7_328
    def v12_858(self, v5_381: List[List[int]])  ->  List[List[int]]:
        v6_350 = [[False] * len(v5_381[0]) for v13_658 in range(len(v5_381))]
        v14_189 = []
        for v15_704 in range(len(v5_381)):
            for v16_532 in range(len(v5_381[0])):
                if v5_381[v15_704][v16_532]  ==  1 and not v6_350[v15_704][v16_532]:
                    v3_125 = v4_859([(v15_704, v16_532)])
                    v6_350[v15_704][v16_532] = True
                    v17_132 = self.v2_214(v3_125, v5_381, v6_350)
                    v14_189.v11_792([v15_704, v16_532, v17_132[0], v17_132[1]])
        return v14_189
