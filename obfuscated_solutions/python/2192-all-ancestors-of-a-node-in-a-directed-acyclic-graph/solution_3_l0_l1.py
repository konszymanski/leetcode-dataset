class Solution:
    def getAncestors(self, n, edges):
        v1_754 = [[] for v2_214 in range(n)]
        v3_125 = [0 for v2_214 in range(n)]
        for v4_859, v5_381 in edges:
            v1_754[v4_859].v6_350(v5_381)
            v3_125[v5_381] += 1
        v7_328 = [v8_242 for v8_242 in range(n) if v3_125[v8_242] == 0]
        v9_854 = []
        while v7_328:
            v10_204 = v7_328.v11_792(0)
            v9_854.v6_350(v10_204)
            for v12_858 in v1_754[v10_204]:
                v3_125[v12_858]  -=  1
                if v3_125[v12_858] == 0:
                    v7_328.v6_350(v12_858)
        v13_658 = [[] for v2_214 in range(n)]
        v14_189 = [set() for v2_214 in range(n)]
        for v15_704 in v9_854:
            for v12_858 in v1_754[v15_704]:
                v14_189[v12_858].v16_532(v15_704)
                v14_189[v12_858].v17_132(v14_189[v15_704])
        for v8_242 in range(n):
            for v15_704 in range(n):
                if v15_704 == v8_242:
                    continue
                if v15_704 in v14_189[v8_242]:
                    v13_658[v8_242].v6_350(v15_704)
        return v13_658
