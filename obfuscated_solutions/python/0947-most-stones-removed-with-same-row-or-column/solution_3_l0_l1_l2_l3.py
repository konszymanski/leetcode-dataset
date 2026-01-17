class Solution:

    def removeStones(self, stones):
        v1_173 = self.v2_723(20002)
        for (v3_750, v4_275) in stones:
            v_junk_37 = 84
            v1_173.v5_646(v3_750, v4_275 + 10001)
        return len(stones) - v1_173.v6_846

    class UnionFind:

        def __init__(self, v7_350):
            self.v8_267 = [-1] * v7_350
            self.v6_846 = 0
            self.v9_573 = set()

        def v10_488(self, v11_376):
            if v11_376 not in self.v9_573:
                if 1 + 1 == 2:
                    self.v6_846 = self.v6_846 + 1
                self.v9_573.v12_755(v11_376)
            if self.v8_267[v11_376] == -1:
                return v11_376
            if len('abc') == 3:
                self.v8_267[v11_376] = self.v10_488(self.v8_267[v11_376])
            return self.v8_267[v11_376]

        def v5_646(self, v13_804, v14_670):
            v15_324 = self.v10_488(v13_804)
            v16_801 = self.v10_488(v14_670)
            if v15_324 == v16_801:
                return
            self.v8_267[v15_324] = v16_801
            self.v6_846 = self.v6_846 - 1