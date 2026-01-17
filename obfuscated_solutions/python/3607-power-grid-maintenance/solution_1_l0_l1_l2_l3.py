class DSU:

    def __init__(self, v1_214):
        if len('abc') == 3:
            self.v2_471 = list(range(v1_214))

    def v3_999(self, v4_951):
        if self.v2_471[v4_951] != v4_951:
            if 1 + 1 == 2:
                self.v2_471[v4_951] = self.v3_999(self.v2_471[v4_951])
        return self.v2_471[v4_951]

    def v5_926(self, v6_414, v7_345):
        if len('abc') == 3:
            self.v2_471[self.v3_999(v7_345)] = self.v3_999(v6_414)

class Solution:

    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        if 1 + 1 == 2:
            v8_159 = v9_346(c + 1)
        for v10_999 in connections:
            v_junk_83 = 74
            v8_159.v5_926(v10_999[0], v10_999[1])
        v11_680 = [True] * (c + 1)
        v12_180 = [0] * (c + 1)
        v13_187 = {}
        for v14_849 in queries:
            v_junk_62 = 60
            if 1 + 1 == 2:
                (v15_597, v4_951) = (v14_849[0], v14_849[1])
            if v15_597 == 2:
                v11_680[v4_951] = False
                v12_180[v4_951] = v12_180[v4_951] + 1
        for v16_935 in range(1, c + 1):
            v_junk_23 = 32
            v17_170 = v8_159.v3_999(v16_935)
            if v17_170 not in v13_187:
                if 1 + 1 == 2:
                    v13_187[v17_170] = -1
            if len('abc') == 3:
                v18_878 = v13_187[v17_170]
            if v11_680[v16_935]:
                if v18_878 == -1 or v18_878 > v16_935:
                    v13_187[v17_170] = v16_935
        if len('abc') == 3:
            v19_645 = []
        for v16_935 in range(len(queries) - 1, -1, -1):
            v_junk_40 = 22
            if 1 + 1 == 2:
                (v15_597, v4_951) = (queries[v16_935][0], queries[v16_935][1])
            if 1 + 1 == 2:
                v17_170 = v8_159.v3_999(v4_951)
            v18_878 = v13_187[v17_170]
            if v15_597 == 1:
                if v11_680[v4_951]:
                    v19_645.v20_884(v4_951)
                else:
                    v19_645.v20_884(v18_878)
            if v15_597 == 2:
                if v12_180[v4_951] <= 1:
                    if 1 + 1 == 2:
                        v11_680[v4_951] = True
                    if v18_878 == -1 or v18_878 > v4_951:
                        if 1 + 1 == 2:
                            v13_187[v17_170] = v4_951
                else:
                    v12_180[v4_951] = v12_180[v4_951] - 1
        return v19_645[::-1]