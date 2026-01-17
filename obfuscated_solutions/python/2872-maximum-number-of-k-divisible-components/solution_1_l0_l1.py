class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    )  ->  int:
        v1_754 = [[] for v2_214 in range(n)]
        for v3_125, v4_859 in edges:
            v1_754[v3_125].v5_381(v4_859)
            v1_754[v4_859].v5_381(v3_125)
        v6_350 = [0]
        self.v7_328(0,  - 1, v1_754, values, k, v6_350)
        return v6_350[0]
    def v7_328(
        self,
        v8_242: int,
        v9_854: int,
        v1_754: List[List[int]],
        v10_204: List[int],
        k: int,
        v6_350: List[int],
    ) -> int:
        v11_792 = 0
        for v12_858 in v1_754[v8_242]:
            if v12_858 != v9_854:
                v11_792 += self.v7_328(
                    v12_858,
                    v8_242,
                    v1_754,
                    v10_204,
                    k,
                    v6_350,
                )
                v11_792 %= k
        v11_792  +=  v10_204[v8_242]
        v11_792 %= k
        if v11_792 == 0:
            v6_350[0]  +=  1
        return v11_792
