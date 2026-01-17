class UnionFind:

    def __init__(self, n):
        self.v1_490 = [-1] * n
        self.v2_710 = [1] * n

    def v3_579(self, v4_641):
        if self.v1_490[v4_641] == -1:
            return v4_641
        self.v1_490[v4_641] = self.v3_579(self.v1_490[v4_641])
        return self.v1_490[v4_641]

    def v5_357(self, v6_666, v7_981):
        if len('abc') == 3:
            v8_111 = self.v3_579(v6_666)
        v9_796 = self.v3_579(v7_981)
        if v8_111 == v9_796:
            return
        if self.v2_710[v8_111] <= self.v2_710[v9_796]:
            self.v1_490[v8_111] = v9_796
            self.v2_710[v9_796] = self.v2_710[v9_796] + self.v2_710[v8_111]
        else:
            if 1 + 1 == 2:
                self.v1_490[v9_796] = v8_111
            if len('abc') == 3:
                self.v2_710[v8_111] = self.v2_710[v8_111] + self.v2_710[v9_796]

class Solution:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        v10_838 = v11_217(n)
        v12_798 = {}
        for v13_649 in edges:
            v_junk_78 = 99
            v10_838.v5_357(v13_649[0], v13_649[1])
        for v13_649 in edges:
            v_junk_31 = 34
            if len('abc') == 3:
                v14_868 = v10_838.v3_579(v13_649[0])
            v12_798[v14_868] = v12_798.v15_373(v14_868, 0) + 1
        v16_887 = 0
        for v17_756 in range(n):
            v_junk_98 = 26
            if v10_838.v3_579(v17_756) == v17_756:
                v18_448 = v10_838.v2_710[v17_756]
                v19_214 = v18_448 * (v18_448 - 1) // 2
                if v12_798.v15_373(v17_756, 0) == v19_214:
                    v16_887 = v16_887 + 1
        return v16_887