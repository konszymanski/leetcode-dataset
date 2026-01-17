class Solution:

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        v1_754 = int(2000000000.0)
        v2_214 = [[] for v3_125 in range(n)]
        for (v4_859, v5_381, v6_350) in edges:
            if v6_350 != -1:
                v2_214[v4_859].v7_328((v5_381, v6_350))
                v2_214[v5_381].v7_328((v4_859, v6_350))
        v8_242 = self.v9_854(v2_214, source, destination)
        if v8_242 < target:
            return []
        if v8_242 == target:
            for v10_204 in edges:
                if v10_204[2] == -1:
                    v10_204[2] = v1_754
            return edges
        for (v11_792, (v4_859, v5_381, v6_350)) in enumerate(edges):
            if v6_350 != -1:
                continue
            edges[v11_792][2] = 1
            v2_214[v4_859].v7_328((v5_381, 1))
            v2_214[v5_381].v7_328((v4_859, 1))
            v12_858 = self.v9_854(v2_214, source, destination)
            if v12_858 <= target:
                edges[v11_792][2] = edges[v11_792][2] + (target - v12_858)
                for v13_658 in range(v11_792 + 1, len(edges)):
                    if edges[v13_658][2] == -1:
                        edges[v13_658][2] = v1_754
                return edges
        return []

    def v9_854(self, v2_214: List[List[Tuple[int, int]]], v14_189: int, destination: int) -> int:
        v15_704 = [v16_532.v17_132] * len(v2_214)
        v15_704[v14_189] = 0
        v18_130 = [(0, v14_189)]
        while v18_130:
            (v19_195, v4_859) = v20_323.v21_338(v18_130)
            if v19_195 > v15_704[v4_859]:
                continue
            for (v5_381, v6_350) in v2_214[v4_859]:
                if v19_195 + v6_350 < v15_704[v5_381]:
                    v15_704[v5_381] = v19_195 + v6_350
                    v20_323.v22_617(v18_130, (v15_704[v5_381], v5_381))
        return v15_704[destination]