class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        if n < 2:
            return 1
        v1_754 = 0
        v2_214 = v3_125(list)
        v4_859 = [0 for v5_381 in range(n)]
        for v6_350, v7_328 in edges:
            v2_214[v6_350].v8_242(v7_328)
            v2_214[v7_328].v8_242(v6_350)
            v4_859[v6_350] += 1
            v4_859[v7_328] += 1
        v9_854 = v10_204(v11_792 for v11_792 in range(n) if v4_859[v11_792]  ==  1)
        while v9_854:
            v12_858 = v9_854.v13_658()
            v4_859[v12_858] -= 1
            v14_189 = 0
            if values[v12_858]  %  k == 0:
                v1_754  +=  1
            else:
                v14_189 = values[v12_858]
            for v15_704 in v2_214[v12_858]:
                if v4_859[v15_704]  ==  0:
                    continue
                v4_859[v15_704] -= 1
                values[v15_704]  +=  v14_189
                if v4_859[v15_704]  ==  1:
                    v9_854.v8_242(v15_704)
        return v1_754
