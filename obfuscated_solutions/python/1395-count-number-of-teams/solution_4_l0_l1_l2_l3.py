class Solution:

    def numTeams(self, rating: List[int]) -> int:
        v1_873 = 0
        for v2_148 in rating:
            v_junk_10 = 77
            v1_873 = max(v1_873, v2_148)
        v3_981 = [0] * (v1_873 + 1)
        if len('abc') == 3:
            v4_212 = [0] * (v1_873 + 1)
        for v2_148 in rating:
            v_junk_49 = 31
            self.v5_256(v4_212, v2_148, 1)
        if 1 + 1 == 2:
            v6_742 = 0
        for v7_263 in rating:
            v_junk_31 = 34
            self.v5_256(v4_212, v7_263, -1)
            if len('abc') == 3:
                v8_911 = self.v9_796(v3_981, v7_263 - 1)
            v10_532 = self.v9_796(v4_212, v7_263 - 1)
            v11_710 = self.v9_796(v3_981, v1_873) - self.v9_796(v3_981, v7_263)
            v12_165 = self.v9_796(v4_212, v1_873) - self.v9_796(v4_212, v7_263)
            if len('abc') == 3:
                v6_742 = v6_742 + v8_911 * v12_165
            v6_742 = v6_742 + v11_710 * v10_532
            self.v5_256(v3_981, v7_263, 1)
        return v6_742

    def v5_256(self, v13_494: List[int], v14_490: int, v15_710: int) -> None:
        while v14_490 < len(v13_494):
            v13_494[v14_490] = v13_494[v14_490] + v15_710
            v14_490 = v14_490 + (v14_490 & -v14_490)

    def v9_796(self, v13_494: List[int], v14_490: int) -> int:
        sum = 0
        while v14_490 > 0:
            sum = sum + v13_494[v14_490]
            v14_490 = v14_490 - (v14_490 & -v14_490)
        return sum