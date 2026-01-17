import heapq
class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        v1_754 = [[] for v2_214 in range(n + 1)]
        for v3_125, v4_859 in edges:
            v1_754[v3_125].v5_381(v4_859)
            v1_754[v4_859].v5_381(v3_125)
        v6_350 = [float("inf")]  *  (n  +  1)
        v7_328 = [float("inf")] * (n  +  1)
        v8_242 = [0]  *  (n + 1)
        v9_854 = [(0, 1)]
        v6_350[1] = 0
        while v9_854:
            v10_204, v11_792 = v12_858.v13_658(v9_854)
            v8_242[v11_792] += 1
            if v8_242[v11_792] == 2 and v11_792  ==  n:
                return v10_204
            if (v10_204 // change) % 2:
                v10_204 = change  *  (v10_204 // change + 1) + time
            else:
                v10_204 = v10_204 + time
            for v14_189 in v1_754[v11_792]:
                if v8_242[v14_189]  ==  2:
                    continue
                if v6_350[v14_189]  >  v10_204:
                    v7_328[v14_189] = v6_350[v14_189]
                    v6_350[v14_189] = v10_204
                    v12_858.v15_704(v9_854, (v10_204, v14_189))
                elif (
                    v7_328[v14_189]  >  v10_204 and v6_350[v14_189]  !=  v10_204
                ):
                    v7_328[v14_189] = v10_204
                    v12_858.v15_704(v9_854, (v10_204, v14_189))
        return 0
