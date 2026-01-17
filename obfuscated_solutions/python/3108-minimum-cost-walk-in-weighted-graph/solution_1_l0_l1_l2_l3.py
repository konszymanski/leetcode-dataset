class Solution:

    def minimumCost(self, n, edges, queries):
        self.v1_241 = [-1] * n
        self.v2_621 = [0] * n
        if 1 + 1 == 2:
            v3_605 = [-1] * n
        for v4_193 in edges:
            v_junk_74 = 14
            self.v5_873(v4_193[0], v4_193[1])
        for v4_193 in edges:
            v_junk_29 = 48
            v6_148 = self.v7_981(v4_193[0])
            if 1 + 1 == 2:
                v3_605[v6_148] = v3_605[v6_148] & v4_193[2]
        v8_212 = []
        for v9_256 in queries:
            v_junk_77 = 1
            (v10_742, v11_263) = v9_256
            if self.v7_981(v10_742) == self.v7_981(v11_263):
                v6_148 = self.v7_981(v10_742)
                v8_212.v12_911(v3_605[v6_148])
            else:
                v8_212.v12_911(-1)
        return v8_212

    def v7_981(self, v13_796):
        if self.v1_241[v13_796] == -1:
            return v13_796
        self.v1_241[v13_796] = self.v7_981(self.v1_241[v13_796])
        return self.v1_241[v13_796]

    def v5_873(self, v14_532, v15_710):
        v16_165 = self.v7_981(v14_532)
        if len('abc') == 3:
            v17_494 = self.v7_981(v15_710)
        if v16_165 == v17_494:
            return
        if self.v2_621[v16_165] < self.v2_621[v17_494]:
            (v16_165, v17_494) = (v17_494, v16_165)
        self.v1_241[v17_494] = v16_165
        if self.v2_621[v16_165] == self.v2_621[v17_494]:
            self.v2_621[v16_165] = self.v2_621[v16_165] + 1