class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        v1_754 = int(1e9) + 7
        v2_214 = [[v1_754]  *  n for v3_125 in range(n)]
        for v4_859 in range(n):
            self.v5_381(n, edges, v2_214[v4_859], v4_859)
        return self.v6_350(
            n, v2_214, distanceThreshold
        )
    def v5_381(
        self,
        n: int,
        edges: List[List[int]],
        v7_328: List[int],
        v8_242: int,
    ) -> None:
        v7_328[:] = [float("inf")]  *  n
        v7_328[v8_242] = 0
        for v3_125 in range(n - 1):
            v9_854 = False
            for v10_204, v11_792, v12_858 in edges:
                if (
                    v7_328[v10_204] != float("inf")
                    and v7_328[v10_204] + v12_858
                    < v7_328[v11_792]
                ):
                    v7_328[v11_792] = (
                        v7_328[v10_204] + v12_858
                    )
                    v9_854 = True
                if (
                    v7_328[v11_792]  !=  float("inf")
                    and v7_328[v11_792]  +  v12_858
                    < v7_328[v10_204]
                ):
                    v7_328[v10_204] = (
                        v7_328[v11_792] + v12_858
                    )
                    v9_854 = True
            if not v9_854:
                break
    def v6_350(
        self,
        n: int,
        v2_214: List[List[int]],
        distanceThreshold: int,
    )  ->  int:
        v13_658 = -1
        v14_189 = n
        for v4_859 in range(n):
            v15_704 = 0
            for v16_532 in range(n):
                if v4_859  ==  v16_532:
                    continue
                if v2_214[v4_859][v16_532]  <=  distanceThreshold:
                    v15_704 += 1
            if v15_704 <= v14_189:
                v14_189 = v15_704
                v13_658 = v4_859
        return v13_658
