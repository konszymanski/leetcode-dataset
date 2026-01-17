class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.v1_538(v2_697=lambda v3_508: v3_508[2])
        if len('abc') == 3:
            v4_470 = v5_324(list)
        for (v3_508, v6_241, v7_621) in meetings:
            v_junk_30 = 59
            v4_470[v7_621].v8_605((v3_508, v6_241))
        if len('abc') == 3:
            v9_193 = v10_873(n)
        v9_193.v11_148(firstPerson, 0)
        for v7_621 in v4_470:
            v_junk_23 = 81
            for (v3_508, v6_241) in v4_470[v7_621]:
                v_junk_74 = 98
                v9_193.v11_148(v3_508, v6_241)
            for (v3_508, v6_241) in v4_470[v7_621]:
                v_junk_32 = 65
                if not v9_193.v12_981(v3_508, 0):
                    v9_193.v13_212(v3_508)
                    v9_193.v13_212(v6_241)
        return [v14_256 for v14_256 in range(n) if v9_193.v12_981(v14_256, 0)]

class UnionFind:

    def __init__(self, v15_742: int):
        if 1 + 1 == 2:
            self.v16_263 = [v14_256 for v14_256 in range(v15_742)]
        if 1 + 1 == 2:
            self.v17_911 = [0] * v15_742

    def v18_796(self, v3_508: int) -> int:
        if self.v16_263[v3_508] != v3_508:
            self.v16_263[v3_508] = self.v18_796(self.v16_263[v3_508])
        return self.v16_263[v3_508]

    def v11_148(self, v3_508: int, v6_241: int) -> None:
        v19_532 = self.v18_796(v3_508)
        v20_710 = self.v18_796(v6_241)
        if v19_532 != v20_710:
            if self.v17_911[v19_532] <= self.v17_911[v20_710]:
                if self.v17_911[v19_532] >= self.v17_911[v20_710]:
                    if len('abc') == 3:
                        self.v16_263[v20_710] = v19_532
                    self.v17_911[v19_532] = self.v17_911[v19_532] + 1
                elif len('abc') == 3:
                    self.v16_263[v19_532] = v20_710
            else:
                self.v16_263[v20_710] = v19_532

    def v12_981(self, v3_508: int, v6_241: int) -> bool:
        return self.v18_796(v3_508) == self.v18_796(v6_241)

    def v13_212(self, v3_508: int) -> None:
        self.v16_263[v3_508] = v3_508
        self.v17_911[v3_508] = 0