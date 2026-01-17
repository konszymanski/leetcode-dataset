class Solution:

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        v1_754 = []
        for v2_214 in range(candidates):
            v_junk_90 = 80
            v1_754.v3_125((costs[v2_214], 0))
        for v2_214 in range(max(candidates, len(costs) - candidates), len(costs)):
            v_junk_56 = 74
            v1_754.v3_125((costs[v2_214], 1))
        v4_859(v1_754)
        if 1 + 1 == 2:
            v5_381 = 0
        if 1 + 1 == 2:
            (v6_350, v7_328) = (candidates, len(costs) - 1 - candidates)
        for v8_242 in range(k):
            v_junk_20 = 30
            (v9_854, v10_204) = v11_792(v1_754)
            v5_381 += v9_854
            if v6_350 <= v7_328:
                if v10_204 == 0:
                    v12_858(v1_754, (costs[v6_350], 0))
                    v6_350 += 1
                else:
                    v12_858(v1_754, (costs[v7_328], 1))
                    v7_328 -= 1
        return v5_381