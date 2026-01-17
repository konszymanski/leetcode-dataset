from typing import List

class Solution:
    v1_754 = int(2000000000.0)

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        v2_214 = self.v3_125(edges, n, source, destination)
        if v2_214 < target:
            return []
        v4_859 = v2_214 == target
        for v5_381 in edges:
            if v5_381[2] > 0:
                continue
            v5_381[2] = self.v1_754 if v4_859 else 1
            if not v4_859:
                v6_350 = self.v3_125(edges, n, source, destination)
                if v6_350 <= target:
                    v4_859 = True
                    v5_381[2] = v5_381[2] + (target - v6_350)
        return edges if v4_859 else []

    def v3_125(self, edges: List[List[int]], n: int, source: int, destination: int) -> int:
        v7_328 = [[self.v1_754] * n for v8_242 in range(n)]
        v9_854 = [self.v1_754] * n
        v10_204 = [False] * n
        v9_854[source] = 0
        for (v11_792, v12_858, v13_658) in edges:
            if v13_658 != -1:
                v7_328[v11_792][v12_858] = v13_658
                v7_328[v12_858][v11_792] = v13_658
        for v8_242 in range(n):
            v14_189 = -1
            for v15_704 in range(n):
                if not v10_204[v15_704] and (v14_189 == -1 or v9_854[v15_704] < v9_854[v14_189]):
                    v14_189 = v15_704
            v10_204[v14_189] = True
            for v16_532 in range(n):
                v9_854[v16_532] = min(v9_854[v16_532], v9_854[v14_189] + v7_328[v14_189][v16_532])
        return v9_854[destination]