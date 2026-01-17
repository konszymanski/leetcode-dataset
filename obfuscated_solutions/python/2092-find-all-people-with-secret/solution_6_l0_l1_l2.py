class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.v1_754(v2_214=lambda v3_125: v3_125[2])
        v4_859 = v5_381(list)
        for (v3_125, v6_350, v7_328) in meetings:
            v4_859[v7_328].v8_242((v3_125, v6_350))
        v9_854 = v10_204(n)
        v9_854.v11_792(firstPerson, 0)
        for v7_328 in v4_859:
            for (v3_125, v6_350) in v4_859[v7_328]:
                v9_854.v11_792(v3_125, v6_350)
            for (v3_125, v6_350) in v4_859[v7_328]:
                if not v9_854.v12_858(v3_125, 0):
                    v9_854.v13_658(v3_125)
                    v9_854.v13_658(v6_350)
        return [v14_189 for v14_189 in range(n) if v9_854.v12_858(v14_189, 0)]

class UnionFind:

    def __init__(self, v15_704: int):
        self.v16_532 = [v14_189 for v14_189 in range(v15_704)]
        self.v17_132 = [0] * v15_704

    def v18_130(self, v3_125: int) -> int:
        if self.v16_532[v3_125] != v3_125:
            self.v16_532[v3_125] = self.v18_130(self.v16_532[v3_125])
        return self.v16_532[v3_125]

    def v11_792(self, v3_125: int, v6_350: int) -> None:
        v19_195 = self.v18_130(v3_125)
        v20_323 = self.v18_130(v6_350)
        if v19_195 != v20_323:
            if self.v17_132[v19_195] <= self.v17_132[v20_323]:
                if self.v17_132[v19_195] >= self.v17_132[v20_323]:
                    self.v16_532[v20_323] = v19_195
                    self.v17_132[v19_195] = self.v17_132[v19_195] + 1
                else:
                    self.v16_532[v19_195] = v20_323
            else:
                self.v16_532[v20_323] = v19_195

    def v12_858(self, v3_125: int, v6_350: int) -> bool:
        return self.v18_130(v3_125) == self.v18_130(v6_350)

    def v13_658(self, v3_125: int) -> None:
        self.v16_532[v3_125] = v3_125
        self.v17_132[v3_125] = 0