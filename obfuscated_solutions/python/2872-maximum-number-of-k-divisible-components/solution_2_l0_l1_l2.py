class Solution:

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1
        v1_754 = 0
        v2_214 = v3_125(set)
        for (v4_859, v5_381) in edges:
            v2_214[v4_859].v6_350(v5_381)
            v2_214[v5_381].v6_350(v4_859)
        v7_328 = v8_242((v9_854 for (v9_854, v10_204) in v2_214.v11_792() if len(v10_204) == 1))
        while v7_328:
            v12_858 = v7_328.v13_658()
            v14_189 = next(iter(v2_214[v12_858])) if v2_214[v12_858] else -1
            if v14_189 >= 0:
                v2_214[v14_189].v15_704(v12_858)
            if values[v12_858] % k != 0:
                values[v14_189] = values[v14_189] + values[v12_858]
            else:
                v1_754 = v1_754 + 1
            if v14_189 >= 0 and len(v2_214[v14_189]) == 1:
                v7_328.v16_532(v14_189)
        return v1_754