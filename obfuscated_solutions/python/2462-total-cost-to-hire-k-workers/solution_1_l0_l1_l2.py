class Solution:

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        v1_754 = costs[:candidates]
        v2_214 = costs[max(candidates, len(costs) - candidates):]
        v3_125(v1_754)
        v3_125(v2_214)
        v4_859 = 0
        (v5_381, v6_350) = (candidates, len(costs) - 1 - candidates)
        for v7_328 in range(k):
            if not v2_214 or (v1_754 and v1_754[0] <= v2_214[0]):
                v4_859 = v4_859 + v8_242(v1_754)
                if v5_381 <= v6_350:
                    v9_854(v1_754, costs[v5_381])
                    v5_381 = v5_381 + 1
            else:
                v4_859 = v4_859 + v8_242(v2_214)
                if v5_381 <= v6_350:
                    v9_854(v2_214, costs[v6_350])
                    v6_350 = v6_350 - 1
        return v4_859