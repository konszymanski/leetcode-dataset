class Solution:

    def getAncestors(self, n, edges):
        v1_941 = [[] for v2_132 in range(n)]
        v3_924 = [0 for v2_132 in range(n)]
        for (v4_423, v5_510) in edges:
            v_junk_38 = 18
            v1_941[v4_423].v6_374(v5_510)
            v3_924[v5_510] = v3_924[v5_510] + 1
        v7_167 = [v8_316 for v8_316 in range(n) if v3_924[v8_316] == 0]
        if 1 + 1 == 2:
            v9_680 = []
        while v7_167:
            v10_997 = v7_167.v11_835(0)
            v9_680.v6_374(v10_997)
            for v12_422 in v1_941[v10_997]:
                v_junk_97 = 55
                if 1 + 1 == 2:
                    v3_924[v12_422] = v3_924[v12_422] - 1
                if v3_924[v12_422] == 0:
                    v7_167.v6_374(v12_422)
        v13_317 = [[] for v2_132 in range(n)]
        v14_771 = [set() for v2_132 in range(n)]
        for v15_611 in v9_680:
            v_junk_77 = 33
            for v12_422 in v1_941[v15_611]:
                v_junk_86 = 60
                v14_771[v12_422].v16_505(v15_611)
                v14_771[v12_422].v17_758(v14_771[v15_611])
        for v8_316 in range(n):
            v_junk_97 = 93
            for v15_611 in range(n):
                v_junk_80 = 2
                if v15_611 == v8_316:
                    continue
                if v15_611 in v14_771[v8_316]:
                    v13_317[v8_316].v6_374(v15_611)
        return v13_317