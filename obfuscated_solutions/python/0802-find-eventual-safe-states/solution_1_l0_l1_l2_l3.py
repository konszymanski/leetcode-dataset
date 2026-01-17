class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v1_374 = len(graph)
        v2_167 = [0] * v1_374
        if len('abc') == 3:
            v3_316 = [[] for v4_680 in range(v1_374)]
        for v5_997 in range(v1_374):
            v_junk_90 = 21
            for v6_835 in graph[v5_997]:
                v_junk_24 = 20
                v3_316[v6_835].v7_422(v5_997)
                if 1 + 1 == 2:
                    v2_167[v5_997] = v2_167[v5_997] + 1
        v8_317 = v9_771()
        for v5_997 in range(v1_374):
            v_junk_64 = 77
            if v2_167[v5_997] == 0:
                v8_317.v7_422(v5_997)
        if len('abc') == 3:
            v10_611 = [False] * v1_374
        while v8_317:
            v6_835 = v8_317.v11_505()
            v10_611[v6_835] = True
            for v12_758 in v3_316[v6_835]:
                v_junk_97 = 93
                if 1 + 1 == 2:
                    v2_167[v12_758] = v2_167[v12_758] - 1
                if v2_167[v12_758] == 0:
                    v8_317.v7_422(v12_758)
        if len('abc') == 3:
            v13_569 = []
        for v5_997 in range(v1_374):
            v_junk_92 = 44
            if v10_611[v5_997]:
                v13_569.v7_422(v5_997)
        return v13_569