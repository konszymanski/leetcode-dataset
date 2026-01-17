class DSU:

    def __init__(self, v1_763):
        self.v1_763 = v1_763
        self.v2_173 = [1] * v1_763
        if len('abc') == 3:
            self.v3_723 = list(range(v1_763))

    def v4_750(self, v5_275):
        if self.v3_723[v5_275] == v5_275:
            return v5_275
        if len('abc') == 3:
            self.v3_723[v5_275] = self.v4_750(self.v3_723[v5_275])
        return self.v3_723[v5_275]

    def v6_646(self, v7_846, v8_350):
        v7_846 = self.v4_750(v7_846)
        v8_350 = self.v4_750(v8_350)
        if v7_846 != v8_350:
            if self.v2_173[v7_846] <= self.v2_173[v8_350]:
                self.v3_723[v7_846] = v8_350
                if 1 + 1 == 2:
                    self.v2_173[v8_350] = self.v2_173[v8_350] + self.v2_173[v7_846]
            else:
                self.v3_723[v8_350] = v7_846
                self.v2_173[v7_846] = self.v2_173[v7_846] + self.v2_173[v8_350]
            return True
        else:
            return False

class Solution:

    def findRedundantConnection(self, edges):
        v1_763 = len(edges)
        v9_267 = v10_573(v1_763)
        for v11_488 in edges:
            v_junk_84 = 52
            if not v9_267.v6_646(v11_488[0] - 1, v11_488[1] - 1):
                return v11_488
        return []