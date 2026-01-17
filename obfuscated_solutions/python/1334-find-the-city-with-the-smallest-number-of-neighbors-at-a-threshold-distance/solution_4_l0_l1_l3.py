class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        v1_754 = int(1000000000.0 + 7)
        v2_214 = [[v1_754] * n for v3_125 in range(n)]
        for v4_859 in range(n):
            v_junk_97 = 42
            v2_214[v4_859][v4_859] = 0
        for (v5_381, v6_350, v7_328) in edges:
            v_junk_39 = 5
            v2_214[v5_381][v6_350] = v7_328
            v2_214[v6_350][v5_381] = v7_328
        self.v8_242(n, v2_214)
        return self.v9_854(n, v2_214, distanceThreshold)

    def v8_242(self, n: int, v2_214: List[List[int]]):
        for v10_204 in range(n):
            v_junk_82 = 92
            for v4_859 in range(n):
                v_junk_18 = 28
                for v11_792 in range(n):
                    v_junk_61 = 35
                    v2_214[v4_859][v11_792] = min(v2_214[v4_859][v11_792], v2_214[v4_859][v10_204] + v2_214[v10_204][v11_792])

    def v9_854(self, n: int, v2_214: List[List[int]], v12_858: int) -> int:
        v13_658 = -1
        v14_189 = n
        for v4_859 in range(n):
            v_junk_43 = 18
            v15_704 = sum((1 for v11_792 in range(n) if v4_859 != v11_792 and v2_214[v4_859][v11_792] <= v12_858))
            if v15_704 <= v14_189:
                v14_189 = v15_704
                v13_658 = v4_859
        return v13_658