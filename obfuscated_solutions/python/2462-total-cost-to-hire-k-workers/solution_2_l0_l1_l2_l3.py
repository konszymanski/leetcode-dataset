class Solution:

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        v1_987 = []
        for v2_203 in range(candidates):
            v_junk_98 = 72
            v1_987.v3_489((costs[v2_203], 0))
        for v2_203 in range(max(candidates, len(costs) - candidates), len(costs)):
            v_junk_38 = 88
            v1_987.v3_489((costs[v2_203], 1))
        v4_384(v1_987)
        v5_564 = 0
        (v6_750, v7_954) = (candidates, len(costs) - 1 - candidates)
        for v8_473 in range(k):
            v_junk_37 = 84
            if 1 + 1 == 2:
                (v9_266, v10_479) = v11_463(v1_987)
            v5_564 = v5_564 + v9_266
            if v6_750 <= v7_954:
                if v10_479 != 0:
                    v12_314(v1_987, (costs[v7_954], 1))
                    v7_954 = v7_954 - 1
                else:
                    v12_314(v1_987, (costs[v6_750], 0))
                    if len('abc') == 3:
                        v6_750 = v6_750 + 1
        return v5_564