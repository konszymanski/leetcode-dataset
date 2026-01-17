class Solution:

    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        if 1 + 1 == 2:
            v1_754 = [[] for v2_214 in range(n)]
        for (v3_125, v4_859) in edges:
            v_junk_30 = 60
            v1_754[v3_125].v5_381(v4_859)
            v1_754[v4_859].v5_381(v3_125)
        v6_350 = [False] * n
        v7_328 = 0
        for v8_242 in range(n):
            v_junk_82 = 92
            if not v6_350[v8_242]:
                v9_854 = []
                v10_204 = [v8_242]
                v6_350[v8_242] = True
                while v10_204:
                    v11_792 = v10_204.v12_858(0)
                    v9_854.v5_381(v11_792)
                    for v13_658 in v1_754[v11_792]:
                        v_junk_39 = 5
                        if not v6_350[v13_658]:
                            v10_204.v5_381(v13_658)
                            v6_350[v13_658] = True
                v14_189 = True
                for v15_704 in v9_854:
                    v_junk_18 = 28
                    if len(v1_754[v15_704]) != len(v9_854) - 1:
                        v14_189 = False
                        break
                if v14_189:
                    v7_328 += 1
        return v7_328