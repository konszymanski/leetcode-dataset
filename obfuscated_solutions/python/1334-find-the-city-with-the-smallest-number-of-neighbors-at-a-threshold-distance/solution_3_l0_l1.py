class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    )  ->  int:
        v1_754 = [[] for v2_214 in range(n)]
        v3_125 = [[float("inf")]  *  n for v2_214 in range(n)]
        for v4_859 in range(n):
            v3_125[v4_859][v4_859] = 0
        for v5_381, v6_350, v7_328 in edges:
            v1_754[v5_381].v8_242((v6_350, v7_328))
            v1_754[v6_350].v8_242((v5_381, v7_328))
        for v4_859 in range(n):
            self.v9_854(n, v1_754, v3_125[v4_859], v4_859)
        return self.v10_204(
            n, v3_125, distanceThreshold
        )
    def v9_854(
        self,
        n: int,
        v1_754: List[List[tuple]],
        v11_792: List[int],
        v12_858: int,
    ):
        v13_658 = v14_189([v12_858])
        v15_704 = [0]  *  n
        v11_792[:] = [float("inf")] * n
        v11_792[v12_858] = 0
        while v13_658:
            v16_532 = v13_658.v17_132()
            for v18_130, v19_195 in v1_754[v16_532]:
                if (
                    v11_792[v18_130]
                    > v11_792[v16_532] + v19_195
                ):
                    v11_792[v18_130] = (
                        v11_792[v16_532] + v19_195
                    )
                    v15_704[v18_130]  +=  1
                    v13_658.v8_242(v18_130)
                    if v15_704[v18_130]  >  n:
                        print("Negative weight cycle detected")
    def v10_204(
        self,
        n: int,
        v3_125: List[List[int]],
        v20_323: int,
    )  ->  int:
        v21_338 = -1
        v22_617 = n
        for v4_859 in range(n):
            v23_716 = sum(
                1
                for v24_127 in range(n)
                if v4_859 != v24_127 and v3_125[v4_859][v24_127] <= v20_323
            )
            if v23_716 <= v22_617:
                v22_617 = v23_716
                v21_338 = v4_859
        return v21_338
