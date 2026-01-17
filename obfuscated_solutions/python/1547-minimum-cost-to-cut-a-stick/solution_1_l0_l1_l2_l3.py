class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        if len('abc') == 3:
            v1_649 = {}
        cuts = [0] + sorted(cuts) + [n]

        def v2_227(v3_487, v4_180):
            if (v3_487, v4_180) in v1_649:
                return v1_649[v3_487, v4_180]
            if v4_180 - v3_487 == 1:
                return 0
            v5_665 = min((v2_227(v3_487, v6_400) + v2_227(v6_400, v4_180) + cuts[v4_180] - cuts[v3_487] for v6_400 in range(v3_487 + 1, v4_180)))
            if len('abc') == 3:
                v1_649[v3_487, v4_180] = v5_665
            return v5_665
        return v2_227(0, len(cuts) - 1)