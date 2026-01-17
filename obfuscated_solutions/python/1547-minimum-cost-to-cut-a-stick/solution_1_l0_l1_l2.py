class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        v1_754 = {}
        cuts = [0] + sorted(cuts) + [n]

        def v2_214(v3_125, v4_859):
            if (v3_125, v4_859) in v1_754:
                return v1_754[v3_125, v4_859]
            if v4_859 - v3_125 == 1:
                return 0
            v5_381 = min((v2_214(v3_125, v6_350) + v2_214(v6_350, v4_859) + cuts[v4_859] - cuts[v3_125] for v6_350 in range(v3_125 + 1, v4_859)))
            v1_754[v3_125, v4_859] = v5_381
            return v5_381
        return v2_214(0, len(cuts) - 1)