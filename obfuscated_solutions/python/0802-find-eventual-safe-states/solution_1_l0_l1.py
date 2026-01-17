class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v1_754 = len(graph)
        v2_214 = [0] * v1_754
        v3_125 = [[] for v4_859 in range(v1_754)]
        for v5_381 in range(v1_754):
            for v6_350 in graph[v5_381]:
                v3_125[v6_350].v7_328(v5_381)
                v2_214[v5_381] += 1
        v8_242 = v9_854()
        for v5_381 in range(v1_754):
            if v2_214[v5_381] == 0:
                v8_242.v7_328(v5_381)
        v10_204 = [False] * v1_754
        while v8_242:
            v6_350 = v8_242.v11_792()
            v10_204[v6_350] = True
            for v12_858 in v3_125[v6_350]:
                v2_214[v12_858] -= 1
                if v2_214[v12_858]  ==  0:
                    v8_242.v7_328(v12_858)
        v13_658 = []
        for v5_381 in range(v1_754):
            if v10_204[v5_381]:
                v13_658.v7_328(v5_381)
        return v13_658
