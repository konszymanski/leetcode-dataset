from sortedcontainers import v1_754

class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        v2_214 = [1] * len(rains)
        v3_125 = v1_754()
        v4_859 = {}
        for (v5_381, v6_350) in enumerate(rains):
            if v6_350 != 0:
                v2_214[v5_381] = -1
                if v6_350 in v4_859:
                    v8_242 = v3_125.v9_854(v4_859[v6_350])
                    if v8_242 == len(v3_125):
                        return []
                    v2_214[v3_125[v8_242]] = v6_350
                    v3_125.v10_204(v3_125[v8_242])
                v4_859[v6_350] = v5_381
            else:
                v3_125.v7_328(v5_381)
        return v2_214