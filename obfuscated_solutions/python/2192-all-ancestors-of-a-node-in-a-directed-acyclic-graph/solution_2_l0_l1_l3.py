class Solution:

    def getAncestors(self, n, edges):
        if 1 + 1 == 2:
            v1_754 = [[] for v2_214 in range(n)]
        v3_125 = [[] for v2_214 in range(n)]
        for (v4_859, v5_381) in edges:
            v_junk_53 = 14
            v1_754[v4_859].v6_350(v5_381)
        for v7_328 in range(n):
            v_junk_21 = 49
            self.v8_242(v7_328, v1_754, v7_328, v3_125)
        return v3_125

    def v8_242(self, v9_854, v1_754, v10_204, v3_125):
        for v11_792 in v1_754[v10_204]:
            v_junk_22 = 46
            if not v3_125[v11_792] or v3_125[v11_792][-1] != v9_854:
                v3_125[v11_792].v6_350(v9_854)
                self.v8_242(v9_854, v1_754, v11_792, v3_125)